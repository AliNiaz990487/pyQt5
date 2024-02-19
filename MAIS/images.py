import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap

from compress.compress import RawToJpeg
from constants import PLACEHOLDER_IMAGE, STACK

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
        """
        The class is intended to set images on both secondary and primary labels.
        When any RAW image/images is selected it first convert it into JPG and set it on lables.
        """
        if not isinstance(window, QMainWindow):
            raise ValueError("window must be of type QMainWindow")
        
        self.window = window
        self.imageIndex = None
        self.filesPath = None
        self.primaryLabelHeight = self.window.primaryLabel.height()
        self.secondaryLabelWidth = self.window.secondaryLabel.width()
        self.secondaryLabelHeight = self.window.secondaryLabel.height()
        self.placeholderImage = QPixmap(str(PLACEHOLDER_IMAGE))

        self.set_secondary_placeholder()
        self.set_primary_placeholder()

    def set_primary_placeholder(self):
        """Set placeholder image on primary label"""
        self.window.primaryLabel.setPixmap(self.placeholderImage)
    
    def set_secondary_placeholder(self):
        """Set placeholder image on secondary label"""
        self.window.secondaryLabel.setPixmap(self.placeholderImage)
        

    def browse(self):
        """Opens up browse dialog to browse for images."""
        fileDialog = QFileDialog()
        self.clear_previous()

        taskIndex = self.window.taskSelection.currentIndex()
        
        self.filesPath, _ = fileDialog.getOpenFileNames(
            self.window, 
            "Open RAW Images",
            filter=r"*.tif" if taskIndex == STACK else r"*.CR2"
        )
        if not self.filesPath:
            return
        
        self.imageIndex = len(self.filesPath)-1
        self.set_image_on_labels()
        self.window.set_count(self.window.totalImages, f"{len(self.filesPath)}")
        self.window.set_count(self.window.selectedCount, f"{len(self.filesPath)}")

    def set_image_on_labels(self, index: int = -1):
        """Convert RAW image into jpg and set it on lables based on index."""
        jpeg = RawToJpeg(self.filesPath[index]).convert_to_jpeg()
        image = QPixmap(jpeg)
        
        pl = self.window.primaryLabel
        sl = self.window.secondaryLabel
        imageName = os.path.split(self.filesPath[index])[-1]
        pl.setPixmap(image.scaled(pl.size(), aspectRatioMode=True))
        sl.setPixmap(image.scaled(sl.size(), aspectRatioMode=True))
        self.window.imageName.setText(imageName)

    def next_image(self):
        """Proceed to next image, increase count and responsible to check for reach end."""
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
        """Proceed to previous image, decrease count, and responsible to check for reach start."""
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

    def clear_previous(self):
        """Clear the loaded images."""
        if self.filesPath is not None:
            self.filesPath.clear()


