import os
import json

from constants import CACHED

class Caching:
    def __init__(self, fileName: str):
        self.fileName = f"{CACHED}/{fileName}"

    def write_to_json(self, data: dict) -> None:
        with open(self.fileName, "w") as file:
            json.dump(data, file, indent=2)
        
    def read_from_json(self) -> dict:
        if not os.path.exists(self.fileName):
            return {}
        
        with open(self.fileName, "r") as file:
            return json.load(file)