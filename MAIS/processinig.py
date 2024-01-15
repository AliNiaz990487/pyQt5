from PyQt5.QtWidgets import QMainWindow, QFileDialog

class StartProcessing:
    def __init__(self, window):
        if not isinstance(window, QMainWindow):
            raise ValueError("window must be of type QMainWindow")
        
        self.window = window

    def start_processing(self):
        self.save_image()
    
    def save_image(self):
        fileDialog = QFileDialog()
        self.savingDirectory = fileDialog.getExistingDirectoryUrl(
            self.window, 
            "Save Image",
        )
        # if not len(self.savingDirectory):
        #     return

        print(self.savingDirectory.url())