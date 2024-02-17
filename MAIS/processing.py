import time
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from threading import Thread

from compress.compress import *
from images import Image
from align.align import Align
from stack.stack import Stack
from constants import *

class StartProcessing:
    def __init__(self, window, image: Image):
        if not isinstance(window, QMainWindow):
            raise ValueError("window must be of type QMainWindow")
        
        self.window = window
        self.image = image
        self.processStatusBar = window.processStatusBar
        

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
        self.savingDirectory = self.savingDirectory.path()
        print("\033[1;31m", self.savingDirectory, "\033[1;0m")

        def run_task_on_thread(target):
            def thread():
                msg = target()
                msg = f"Saved Successfully at {msg}"
                # mb = QMessageBox(parent=self.window, text=msg)
                # mb.show()
                # try:
                #     mb.exec_()
                # except: ...

            t = Thread(target=thread)
            t.start()

        if not self.image.filesPath or not self.savingDirectory:
            return 
        
        if self.taskIndex == COMPRESS and self.algorithmIndex == JPEG:
            run_task_on_thread(self._convert_to_jpeg)

        if self.taskIndex == COMPRESS and self.algorithmIndex == PNG:
            run_task_on_thread(self._convert_to_png)
        
        if self.taskIndex == COMPRESS and self.algorithmIndex == GIF:
            run_task_on_thread(self._convert_to_gif)

        if self.taskIndex == ALIGN:
            run_task_on_thread(self._align)
        
        if self.taskIndex == STACK and self.algorithmIndex == MEDIAN:
            run_task_on_thread(self._stack)
            

    
    def _convert_to_jpeg(self):
        return RawToJpeg(self.image.filesPath[self.image.imageIndex], self.savingDirectory, False)\
        .convert_to_jpeg()

    def _convert_to_png(self):
        return RawToPNG(self.image.filesPath[self.image.imageIndex], self.savingDirectory, self.processStatusBar)\
        .convert_to_png()
    
    def _convert_to_gif(self):
        return RawtoGIF(self.image.filesPath, self.savingDirectory, self.processStatusBar)\
        .convert_to_gif()

    def _align(self):
        return Align(self.image.filesPath, self.savingDirectory, self.processStatusBar)\
        .align()
    
    def _stack(self):
        return Stack(self.image.filesPath, self.savingDirectory, self.processStatusBar)\
        .stack()