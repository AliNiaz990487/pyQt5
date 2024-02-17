import numpy as np
import cv2 as cv
import os

class Stack:
    def __init__(self, filesPath, savingDirectory, processStatusBar):
        self.filesPath = filesPath
        self.savingDirectory = savingDirectory
        self.processStatusBar = processStatusBar
    
    def stack(self):
        self.processStatusBar.show()
        
        def read_image_and_update_progress(path, i):
            self.processStatusBar.setValue(((i+1)*100)//50)
            img = cv.imread(path)
            return img
        
        alignedImages = [read_image_and_update_progress(path, i) for i, path in enumerate(self.filesPath)]
        alignedImages = [img for img in alignedImages if img is not None]

        minWidth = min(img.shape[1] for img in alignedImages)
        self.processStatusBar.setValue(55)
        minHeight = min(img.shape[0] for img in alignedImages)
        self.processStatusBar.setValue(60)

        alignedImages = [cv.resize(img, (minWidth, minHeight)) for img in alignedImages]
        self.processStatusBar.setValue(65)
        
        alignedImages = np.array(alignedImages)

        # Stack the aligned images together using a median filter
        medianImage = np.median(alignedImages, axis=0)
        medianImage = medianImage[5:-5, 5:-5]
        self.processStatusBar.setValue(70)

        # Scale the values to the range [0, 255]
        scaledImage = (medianImage - medianImage.min()) / (medianImage.max() - medianImage.min()) * 255
        self.processStatusBar.setValue(75)

        # Round the values to the nearest integer
        roundedImage = np.round(scaledImage)
        self.processStatusBar.setValue(80)

        # Convert the values to uint8
        uint8_image = np.clip(roundedImage, 0, 255).astype(np.uint8)
        self.processStatusBar.setValue(90)
        # Save the stacked image
        uint8_image = cv.cvtColor(uint8_image, cv.COLOR_BGR2RGB)

        self.savingDirectory = self._get_stacked_tif_path(self.filesPath[0])
        cv.imwrite(self.savingDirectory, uint8_image)
        self.processStatusBar.setValue(100)
        self.processStatusBar.hide()

        return self.savingDirectory


    def _get_stacked_tif_path(self, path):
        fileName = os.path.split(path)[-1]
        fileName = os.path.splitext(fileName)[0]

        if 'ALIGNED' in fileName:
            fileName = fileName.replace('ALIGNED', 'STACKED')

        
        return f"{self.savingDirectory}/{fileName}.tif"
