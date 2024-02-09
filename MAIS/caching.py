import os
import json

from constants import CACHED_DIR

class Caching:
    def __init__(
            self, 
            fileName: str,
            rawImagePath: str, 
            compressImagePath: str
        ):
        def create_cached_directory():
            if not os.path.exists(CACHED_DIR):
                os.mkdir(CACHED_DIR)
        
        create_cached_directory()
        self.filePath = f"{CACHED_DIR}/{fileName}"
        self.rawImagePath = rawImagePath
        self.compressImagePath = compressImagePath
        self.cache = self.read_from_json()

    def write_to_json(self, data: dict) -> None:
        with open(self.filePath, "w") as file:
            json.dump(data, file, indent=2)
        
    def read_from_json(self) -> dict:
        if not os.path.exists(self.filePath):
            return {}
        
        with open(self.filePath, "r") as file:
            return json.load(file)
    
    def cached(self):
        return self.rawImagePath in self.read_from_json() and \
            os.path.exists(self.cache[self.rawImagePath])
    
    def store_cache(self):
        self.cache[self.rawImagePath] = self.compressImagePath
        self.write_to_json(self.cache)