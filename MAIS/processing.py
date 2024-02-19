from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, QThread

from compress.compress import RawtoGIF, RawToJpeg, RawToPNG
from images import Image
from align.align import Align
from stack.stack import Stack
from constants import ALIGN, COMPRESS, JPEG, PNG, GIF, STACK, MEDIAN

class StartProcessing:
    def __init__(self, window, image: Image):
        if not isinstance(window, QMainWindow):
            raise ValueError("window must be of type QMainWindow")
        
        self.window = window
        self.image = image
        self.processStatusBar = window.processStatusBar
        self.processingThread = window.processingThread
        self.worker = None
        

    def start_processing(self):
        if not self.image.filesPath:
            return
        
        self.taskIndex = self.window.taskSelection.currentIndex()
        self.compressIndex = self.window.compressAlgorithms.currentIndex()
        self.stackIndex = self.window.stackAlgorithms.currentIndex()
        self.save_image()
        # self.window.setEnabled(False)

    
    def save_image(self):
        fileDialog = QFileDialog()
        self.savingDirectory = fileDialog.getExistingDirectoryUrl(
            self.window, 
            "Save Images" if self.taskIndex == ALIGN else "Save Image",
        )
        self.savingDirectory = self.savingDirectory.path()

        def run_task_on_thread(target):
            def show_msg(msg):
                if msg == "error": 
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText('Only "tif" images can be stacked')
                    msg.setWindowTitle("Error")
                    msg.show()
                    msg.exec_() 
                    return 
                mb = QMessageBox(parent=self.window, text=f"{msg}")
                mb.show()
                mb.exec_()

            if not self.processingThread.isRunning():
                processingThread = QThread()
                self.worker = Worker(target)
                self.worker.moveToThread(processingThread)

                processingThread.worker = self.worker
                processingThread.started.connect(self.worker.run)
                def on_thread_start():
                    self.processStatusBar.setValue(0)
                    self.processStatusBar.show()
                self.worker.started.connect(on_thread_start)
                
                def on_thread_finished():
                    self.processStatusBar.hide()
                    # self.window.setEnabled(True)
                    processingThread.quit()
                self.worker.finished.connect(on_thread_finished)

                self.worker.messaged.connect(lambda msg: show_msg(msg))
                self.worker.progressed.connect(lambda value: self.update_progress(value))

                self.processingThread = processingThread
                self.processingThread.start()

        if not self.image.filesPath or not self.savingDirectory:
            return 
        

        if self.taskIndex == COMPRESS and self.compressIndex == JPEG:
            run_task_on_thread(self._convert_to_jpeg)

        elif self.taskIndex == COMPRESS and self.compressIndex == PNG:
            run_task_on_thread(self._convert_to_png)
        
        elif self.taskIndex == COMPRESS and self.compressIndex == GIF:
            run_task_on_thread(self._convert_to_gif)

        elif self.taskIndex == ALIGN:
            run_task_on_thread(self._align)
        
        elif self.taskIndex == STACK and self.stackIndex == MEDIAN:
            run_task_on_thread(self._stack)
            

    
    def _convert_to_jpeg(self):
        return RawToJpeg(self.image.filesPath[self.image.imageIndex], self.savingDirectory, False)\
        .convert_to_jpeg()

    def _convert_to_png(self):
        return RawToPNG(self.image.filesPath[self.image.imageIndex], self.savingDirectory, self.worker.progressed)\
        .convert_to_png()
    
    def _convert_to_gif(self):
        return RawtoGIF(self.image.filesPath, self.savingDirectory, self.worker.progressed)\
        .convert_to_gif()

    def _align(self):
        return Align(self.image.filesPath, self.savingDirectory, self.worker.progressed)\
        .align()
    
    def _stack(self):
        if ".CR2" in self.image.filesPath[0]:
            return "error"

        return Stack(self.image.filesPath, self.savingDirectory, self.worker.progressed)\
        .stack()
    

    def update_progress(self, value: int):
        self.processStatusBar.setValue(value)
        
    

class Worker(QObject):
    started = pyqtSignal()
    progressed = pyqtSignal(int)
    messaged = pyqtSignal(str)
    finished = pyqtSignal()
    
    def __init__(self, target):
        super().__init__()
        self.target = target



    def run(self):
        self.started.emit()
        msg = self.target()
        self.messaged.emit(f"{msg}")
        self.finished.emit()