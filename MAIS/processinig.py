from PyQt5.QtWidgets import QMainWindow, QFileDialog, QComboBox, QMessageBox
from compress.compress import *
from images import Image
from constants import *

class StartProcessing:
    def __init__(self, window, image: Image):
        if not isinstance(window, QMainWindow):
            raise ValueError("window must be of type QMainWindow")
        
        self.window = window
        self.image = image
        

    def start_processing(self):
        if not self.image.filesPath:
            return
        
        self.taskIndex = self.window.taskSelection.currentIndex()
        self.algorithmIndex = self.window.compressAlgorithms.currentIndex()
        self.save_image()
    
    def save_image(self):
        fileDialog = QFileDialog()
        self.savingDirectory = fileDialog.getExistingDirectoryUrl(
            self.window, 
            "Save Image",
        )
        print(self.savingDirectory.path())
        print(f"\033[1;31m {self.savingDirectory.path()}  \033[0m")

        if not self.image.filesPath or not self.savingDirectory.path():
            return 
        
        if self.taskIndex == COMPRESS and self.algorithmIndex == JPEG:
            imagePath = self._convert_to_jpeg()

        if self.taskIndex == COMPRESS and self.algorithmIndex == PNG:
            imagePath = self._convert_to_png()
        
        if self.taskIndex == COMPRESS and self.algorithmIndex == GIF:
            imagePath = self._convert_to_gif()

        msg = f"Saved Successfully at {imagePath}"
        mb = QMessageBox(parent=self.window, text=msg)
        mb.show()

    
    def _convert_to_jpeg(self):
        return RawToJpeg(self.image.filesPath[self.image.imageIndex], self.savingDirectory.path(), False)\
        .convert_to_jpeg()

    def _convert_to_png(self):
        return RawToPNG(self.image.filesPath[self.image.imageIndex], self.savingDirectory.path())\
        .convert_to_png()
    
    def _convert_to_gif(self):
        return RawtoGIF(self.image.filesPath, self.savingDirectory.path())\
        .convert_to_gif()