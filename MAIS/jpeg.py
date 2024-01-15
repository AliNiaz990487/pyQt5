from PIL import Image
import os
import json

from caching import Caching
from constants import JPEG_CACHED

CACHED_FILE = "jpeg_caching.json"

class RawToJpeg:
    def __init__(
            self, 
            rawImagePath: str,
            jpegImagePath: str = JPEG_CACHED
        ):
        self.caching = Caching(CACHED_FILE)
        self.cache = self.caching.read_from_json()
        self.rawImagePath = rawImagePath
        self.jpegImagePath = jpegImagePath

        
    def convert_to_jpeg(self):
        # Check if the converted image is already in the cache
        if self.rawImagePath in self.cache and\
                os.path.exists(self.cache[self.rawImagePath]):
            
            print(f"Using cached JPEG for {self.rawImagePath}")
            return self.cache[self.rawImagePath]

        # If not in the cache, convert the raw image to JPEG
        self._do_conversion()

        # Store the converted image path in the cache
        self.cache[self.rawImagePath] = self.jpegImagePath
        

        self.caching.write_to_json(self.cache)

        return self.jpegImagePath

    def _do_conversion(self):
        print("converting to jpeg...")
        rawImage = Image.open(self.rawImagePath)
        jpegImageName = os.path.split(self.rawImagePath)[-1]
        jpegImageName = os.path.splitext(jpegImageName)[0] + ".jpg"
        self.jpegImagePath = f"{self.jpegImagePath}/{jpegImageName}"

        rawImage.save(self.jpegImagePath, 'JPEG')

# Example usage:
# converter = RawToJpeg()

# Convert raw images to JPEG, and subsequent calls will use the cached results
# jpeg_image1 = RawToJpeg('/home/aliniaz/Desktop/pyQt5/raw/IMG_4209.CR2').convert_to_jpeg()
# jpeg_image2 = RawToJpeg('/home/aliniaz/Desktop/pyQt5/raw/IMG_4210.CR2').convert_to_jpeg()
# jpeg_image3 = RawToJpeg('/home/aliniaz/Desktop/pyQt5/raw/IMG_4211.CR2').convert_to_jpeg()  # Using cached result

# print(jpeg_image1, jpeg_image2, jpeg_image3)


