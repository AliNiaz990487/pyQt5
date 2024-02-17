import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QComboBox, QShortcut, QLabel
)
from PyQt5.QtGui import QKeySequence
from PyQt5 import uic

from images import Image
from processinig import StartProcessing
from constants import (
    ALIGN, BLACKED, COMPRESS, GRAYED, STACK, 
    UI, VISIBLE_INDICATOR, INVISIBLE_INDICATOR
)

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        """
        The class defines main window of the application.
        """
        super().__init__(**kwargs)
        uic.loadUi(UI, self) # load UI
        
        self.image = Image(self)
        self.startProcessing = StartProcessing(self, self.image)
        self.secondaryLabel.setMargin(8)
        self.primaryLabel.setMargin(10)

        def task_selection():
            """Select a task from the drop down list."""
            def hide_unnecessary():
                self.stackAlgorithms.hide()
                self.compressAlgorithms.hide()
                self.algorithmsLabel.setStyleSheet(GRAYED)

            def show_on_selection(index: int):
                """Show only selected algorithm based on selected task, and remove others."""
                hide_unnecessary()
                if index == COMPRESS:
                    self.compressAlgorithms.show()
                    self.algorithmsLabel.setStyleSheet(BLACKED)
                elif index == STACK:
                    self.stackAlgorithms.show()
                    self.algorithmsLabel.setStyleSheet(BLACKED)

            hide_unnecessary()


            self.taskSelection.currentIndexChanged.connect(show_on_selection)

        task_selection()
        self.processStatusBar.hide()

        # buttons functionalities
        self.browseBtn.clicked.connect(self.image.browse)
        self.nextImage.clicked.connect(self.image.next_image)
        self.previousImage.clicked.connect(self.image.previous_image)
        self.startProcessingBtn.clicked.connect(self.startProcessing.start_processing)

        # keyboard shortcuts
        QShortcut(QKeySequence("Shift+Left"), self)\
            .activated.connect(self.image.previous_image)
        QShortcut(QKeySequence("Shift+Right"), self)\
            .activated.connect(self.image.next_image)
        QShortcut(QKeySequence("Ctrl+b"), self)\
            .activated.connect(self.image.browse)
        QShortcut(QKeySequence("Ctrl+Shift+a"), self)\
            .activated.connect(
                lambda: self.taskSelection.setCurrentIndex(ALIGN)
            )
        QShortcut(QKeySequence("Ctrl+Shift+c"), self)\
            .activated.connect(
                lambda: self.taskSelection.setCurrentIndex(COMPRESS)
            )
        QShortcut(QKeySequence("Ctrl+Shift+s"), self)\
            .activated.connect(
                lambda: self.taskSelection.setCurrentIndex(STACK)
            )


    def make_indicator_visible(self, indicator: QLabel):
        indicator.setStyleSheet(VISIBLE_INDICATOR)
    
    def make_indicator_invisible(self, indicator: QLabel):
        indicator.setStyleSheet(INVISIBLE_INDICATOR)
    
    def set_count(self, label: QLabel, text: str):
        label.setText(text)
    
    def make_indicators_invisible(self):
        self.make_indicator_invisible(self.startIndicator)
        self.make_indicator_invisible(self.endIndicator)


app = QApplication(sys.argv)
mainWindow = MainWindow() # instantiate the app


mainWindow.show() # show the main window
sys.exit(app.exec_())

