from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from constants import PLACEHOLDER_IMAGE

def calculate_aspect(width: int, height: int) -> str:
    def gcd(a, b):
        """The GCD (greatest common divisor) is the highest number that evenly divides both width and height."""
        return a if b == 0 else gcd(b, a % b)

    r = gcd(width, height)
    x = int(width / r)
    y = int(height / r)

    return {"width": x, "height": y}


class Image:
    def __init__(self, window: QMainWindow):
        if not isinstance(window, QMainWindow):
            raise ValueError("window must be of type QMainWindow")
        
        self.window = window
        self.imageIndex = None
        self.secondaryLabelWidth = self.window.secondaryLabel.width()
        self.secondaryLabelHeight = self.window.secondaryLabel.height()
        self.placeholderImage = QPixmap(str(PLACEHOLDER_IMAGE))

        self.set_secondary_placeholder()
        self.set_primary_placeholder()

    def set_primary_placeholder(self):
        self.window.primaryLabel.setPixmap(self.placeholderImage)
    
    def set_secondary_placeholder(self):
        self.window.secondaryLabel.setPixmap(self.placeholderImage)
        

    
    def browse(self):
        fileDialog = QFileDialog()
        self.filesPath, _ = fileDialog.getOpenFileNames(
            self.window, 
            "Open Image Files",
        )
        if not len(self.filesPath):
            return
        
        self.imageIndex = len(self.filesPath)-1
        self.set_image_on_labels()
        self.window.set_count(self.window.totalImages, f"{len(self.filesPath)}")
        self.window.set_count(self.window.selectedCount, f"{len(self.filesPath)}")

    def set_image_on_labels(self, index: int = -1):
        image = QPixmap(self.filesPath[index])
        self.window.primaryLabel.setPixmap(image)

        image = image.scaledToHeight(self.secondaryLabelHeight)
        self.window.secondaryLabel.setPixmap(image)

    def next_image(self):
        if self.imageIndex is None:
            return
        
        if self.imageIndex == len(self.filesPath) - 1:
            self.window.make_indicator_visible(
                self.window.endIndicator
            )
            self.imageIndex = len(self.filesPath) - 1
            return
        
        self.imageIndex += 1
        self.window.make_indicators_invisible()
        self.set_image_on_labels(self.imageIndex)
        self.window.set_count(self.window.selectedCount, f"{self.imageIndex+1}")

    
    def previous_image(self):
        if self.imageIndex is None:
            return
        
        if self.imageIndex == 0:
            self.window.make_indicator_visible(
                self.window.startIndicator
            )
            self.imageIndex = 0
            return

        self.imageIndex -= 1
        self.window.make_indicators_invisible()
        self.set_image_on_labels(self.imageIndex)
        self.window.set_count(self.window.selectedCount, f"{self.imageIndex+1}")

