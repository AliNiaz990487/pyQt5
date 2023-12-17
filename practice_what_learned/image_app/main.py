import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

class ImageDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentDisplayedImage = None
        uic.loadUi("ui/main_window.ui", self)

        self.init_ui()

    def init_ui(self):
        self.placeHolder = QPixmap('images/placeholder.png')

        self.imageLabel.setPixmap(self.placeHolder)
        self.browseBtn.clicked.connect(self.browse_image)
        self.nextBtn.clicked.connect(lambda: self.display_image(True))
        self.previousBtn.clicked.connect(lambda: self.display_image(False))

    def browse_image(self):
        fileDialog = QFileDialog()
        self.filesPath, _ = fileDialog.getOpenFileNames(self, 'Open Image File', '', 'images (*.png *.jpg *.jpeg *.bmp *.gif)')

        if not self.__validate_paths():
            self.imageLabel.setText("Please select only images")
            self.filesPath.clear()
            return 


        if self.filesPath[-1]:
            pixmap = QPixmap(self.filesPath[-1])
            self.imageLabel.setPixmap(
                pixmap
                .scaled(
                    self.placeHolder.width(), 
                    self.placeHolder.height()
                )
            )
            self.currentDisplayedImage = len(self.filesPath)-1
        else:
            self.imageLabel.setPixmap(QPixmap('images/placeholder.png'))  # Reset to placeholder if no image selected
    
    def display_image(self, next: bool):
        def show_img(index: int):
            pixmap = QPixmap(self.filesPath[index])
            self.imageLabel.setPixmap(
                pixmap
                .scaled(
                    self.placeHolder.width(), 
                    self.placeHolder.height()
                )
            )
        dispImg = self.currentDisplayedImage
        if dispImg is None: dispImg = 0


        if next:
            dispImg += 1 if dispImg < len(self.filesPath)-1 else 0
            print(f"len {len(self.filesPath)}")
            print(f"index {dispImg}")
            show_img(dispImg)
            self.currentDisplayedImage = dispImg
        else:
            dispImg -= 1 if dispImg > 0 else dispImg
            show_img(dispImg)
            self.currentDisplayedImage = dispImg


    
    def __validate_paths(self):
        for path in self.filesPath:
            i = len(path)-1
            while (path[i] != "."): i -= 1
            print(path[i::])
            if (
                path[i::] != ".png" and
                path[i::] != ".jpg" and
                path[i::] != ".jpg" and
                path[i::] != ".jpeg" and
                path[i::] != ".bmp" and
                path[i::] != ".gif"
            ): return False
        return True

app = QApplication(sys.argv)
window = ImageDisplayApp()


window.show()
sys.exit(app.exec_())
