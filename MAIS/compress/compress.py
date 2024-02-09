import os

from caching import Caching

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