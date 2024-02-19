import os
import cv2
import rawpy
import numpy as np

from caching import Caching
from constants import TIFF_CACHED_DIR

class Align():
    def __init__(self, filesPath, savingDirectory, progressed):
        self.filesPath = filesPath
        self.progressed = progressed
        self.savingDirectory = savingDirectory

        if not os.path.exists(TIFF_CACHED_DIR):
            os.mkdir(TIFF_CACHED_DIR)        

    def raw_to_tiff(self, rawPath):
        CACHED_FILE = "tiff_caching.json"

        fileName = self._get_name_from_path(rawPath) + ".tif"
        outputPath = f"{TIFF_CACHED_DIR}/{fileName}"
        cache = Caching(CACHED_FILE, rawPath, outputPath)

        if cache.cached():
            print(f"Using cached for {rawPath}")
            return cache.read_from_json()[rawPath]
        
        def _do_conversion():
            print("converting to tiff ....")
            with rawpy.imread(rawPath) as raw:
                image = raw.postprocess(use_camera_wb=True, no_auto_bright=True)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                cv2.imwrite(outputPath, image)

        _do_conversion()
        cache.store_cache()

        return outputPath
    
    def raw_to_tiffs(self):
        def update_progress_and_convert(path, i):
            self.progressed.emit(((i+1)*100)//30)
            return self.raw_to_tiff(path)

        return [update_progress_and_convert(path, i) for i, path in enumerate(self.filesPath)]
    
    def cv_mats_to_tiffs(self, alignedImages):
        for i, image, rawPath in zip(range(len(alignedImages)), alignedImages, self.filesPath):
            fileName = self._get_name_from_path(rawPath)
            _savingPath = f"{self.savingDirectory}/{fileName}_ALIGNED.tif"

            print(_savingPath)
            
            cv2.imwrite(_savingPath, image)
            self.progressed.emit(((i)*100)//len(alignedImages)+30)

        return self.savingDirectory

    
    def align(self):
        imageFiles = self.raw_to_tiffs()

        # Initialize variables
        alignedImages = []
        # set the reference image to the first image
        refrenceImage = cv2.cvtColor(cv2.imread(imageFiles[0]), cv2.COLOR_BGR2RGB)
        alignedImages.append(refrenceImage)

        # Loop through each image and align with the reference image
        for i in range(1, len(imageFiles)):

            # align the current image with the reference image
            image = cv2.cvtColor(cv2.imread(imageFiles[i]), cv2.COLOR_BGR2RGB)

            # Use OpenCV feature matching to find corresponding keypoints in the images
            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(refrenceImage, None)
            kp2, des2 = orb.detectAndCompute(image, None)
            # Initialize the Flann-Based matcher
            FLANN_INDEX_LSH = 6
            indexParams = dict(algorithm=FLANN_INDEX_LSH,
                                table_number=6,
                                key_size=12,
                                multi_probe_level=1)
            searchParams = dict(checks=50)
            flann = cv2.FlannBasedMatcher(indexParams, searchParams)
            
            # Match the descriptors
            matches = flann.knnMatch(des1, des2, k=2)
            matches = [cv2.DMatch(m[0].queryIdx, m[0].trainIdx, m[0].distance) for m in matches if m]
            matches = sorted(matches, key=lambda x: x.distance)

            # Use affine transformation to warp the image and align it with the reference image
            sroucePoints = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            distinationPoints = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
            M, _ = cv2.estimateAffinePartial2D(distinationPoints, sroucePoints)
            aligned_image = cv2.warpAffine(image, M, (refrenceImage.shape[1], refrenceImage.shape[0]))
            alignedImages.append(aligned_image)

        return self.cv_mats_to_tiffs(alignedImages)

    def _get_name_from_path(self, rawPath):
        fileName = os.path.split(rawPath)[-1]
        fileName = os.path.splitext(fileName)[0]

        return fileName



