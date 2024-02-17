from PIL import Image
import os

from caching import Caching
from constants import JPEG_CACHED_DIR

class Compress:
    def __init__(
            self, 
            compressDirectory: str, 
            cachedFile: str, 
            rawImagePath: str,
            compressImagePath: str, 
            compressFileExt: str
        ):
        self.compressFileExt = compressFileExt
        self.caching = Caching(
            cachedFile, 
            rawImagePath, 
            self.cancate_compress_name(compressImagePath, rawImagePath)
        )
        self.cache = self.caching.read_from_json()
        
        if not os.path.exists(compressDirectory):
            os.mkdir(compressDirectory)

    def cancate_compress_name(self, compressPath, rawPath):
        compressImageName = os.path.split(rawPath)[-1]
        compressImageName = os.path.splitext(compressImageName)[0] + self.compressFileExt
        self.compressImagePath = f"{compressPath}/{compressImageName}"

        return self.compressImagePath
    
    def _do_conversion(self):
        raise NotImplementedError("should be implemented by child classes")


class RawToJpeg(Compress):
    def __init__(self, rawImagePath, jpegImagePath = None, useCache = True):
        if jpegImagePath is None:
            jpegImagePath = JPEG_CACHED_DIR
        
        CACHED_FILE = "jpeg_caching.json"
        super().__init__(JPEG_CACHED_DIR, CACHED_FILE, rawImagePath, jpegImagePath, ".jpg")
        self.rawImagePath = rawImagePath
        self.jpegImagePath = jpegImagePath
        self.useCache = useCache

    def convert_to_jpeg(self):
        # Check if the converted image is already in the cache
        if self.caching.cached() and self.useCache:
            print(f"Using cached JPEG for {self.rawImagePath}")
            return self.cache[self.rawImagePath]

        # If not in the cache, convert the raw image to JPEG
        self._do_conversion()

        if self.useCache:
            # Store the converted image path in the cache
            self.caching.store_cache()

        return self.jpegImagePath

    def _do_conversion(self):
        print("converting to jpeg...")
        rawImage = Image.open(self.rawImagePath)

        self.jpegImagePath = self.cancate_compress_name(self.jpegImagePath, self.rawImagePath)
        rawImage.save(self.jpegImagePath, 'JPEG')


class RawToPNG:
    def __init__(self, rawImagePath, pngImagePath, processStatusBar):

        self.rawImagePath = rawImagePath
        self.pngImagePath = pngImagePath
        self.processStatusBar = processStatusBar

    def convert_to_png(self):
        self._do_conversion()

        return self.pngImagePath

    def _do_conversion(self):
        print("converting to png...")
        self.processStatusBar.show()
        self.processStatusBar.setValue(50)
        rawImage = Image.open(self.rawImagePath)

        pngImageName = os.path.split(self.rawImagePath)[-1]
        pngImageName = os.path.splitext(pngImageName)[0] + ".png"
        self.pngImagePath = f"{self.pngImagePath}/{pngImageName}"

        rawImage.save(self.pngImagePath, 'PNG')
        self.processStatusBar.setValue(100)
        self.processStatusBar.hide()


class RawtoGIF:
    def __init__(self, rawPaths, compressDirectory, progressStatusBar):
        print("#"*100)
        self.jpegPaths = [
            RawToJpeg(rawPath).convert_to_jpeg()
            for rawPath in rawPaths
        ]
        self.compressDirectory = compressDirectory
        self.progressStatusBar = progressStatusBar
    
    def convert_to_gif(self):
        self.progressStatusBar.show()

        def open_image_update_progress(path, i):
            self.progressStatusBar.setValue(((i+1)*100)//50)
            return Image.open(path)

        frames = [open_image_update_progress(path, i) for i, path in enumerate(self.jpegPaths)]
        for i, frame in enumerate(frames):
            x, y = frame.size
            frames[i] = frames[i].resize([x//4, y//4])
        frameOne = frames[0]

        
        gifName = os.path.split(self.jpegPaths[0])[-1]
        gifName = os.path.splitext(gifName)[0] + ".gif"

        self.compressDirectory = f"{self.compressDirectory}/{gifName}"

        frameOne.save(self.compressDirectory, "GIF", optimize=True, save_all=True, append_images=frames, duration=100, loop=0)
        self.progressStatusBar.setValue(100)
        self.progressStatusBar.hide()
        return self.compressDirectory
