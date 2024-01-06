import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QShortcut, QLabel
from PyQt5.QtGui import QKeySequence
import PyQt5.QtCore
from PyQt5 import uic

from images import Image
from constants import BLACKED, GRAYED, UI, VISIBLE_INDICATOR, INVISIBLE_INDICATOR

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        uic.loadUi(UI, self)
        
        self.image = Image(self)
        self.secondaryLabel.setMargin(8)
        self.primaryLabel.setMargin(10)

        def task_selection():
            def hide_unnecessary():
                self.stackAlgorithms.hide()
                self.compressAlgorithms.hide()
                self.algorithmsLabel.setStyleSheet(GRAYED)

            def show_on_selection(index: int):
                hide_unnecessary()
                if index == 1:
                    self.stackAlgorithms.show()
                    self.algorithmsLabel.setStyleSheet(BLACKED)
                elif index == 2:
                    self.compressAlgorithms.show()
                    self.algorithmsLabel.setStyleSheet(BLACKED)

            hide_unnecessary()


            self.taskSelection.currentIndexChanged.connect(show_on_selection)

        task_selection()

        self.browseBtn.clicked.connect(self.image.browse)
        self.nextImage.clicked.connect(self.image.next_image)
        self.previousImage.clicked.connect(self.image.previous_image)

        # keyboard shortcuts
        QShortcut(QKeySequence("Shift+Left"), self)\
            .activated.connect(self.image.previous_image)
        QShortcut(QKeySequence("Shift+Right"), self)\
            .activated.connect(self.image.next_image)
        QShortcut(QKeySequence("Ctrl+b"), self)\
            .activated.connect(self.image.browse)
        QShortcut(QKeySequence("Ctrl+Shift+a"), self)\
            .activated.connect(lambda: self.taskSelection.setCurrentIndex(0))
        QShortcut(QKeySequence("Ctrl+Shift+c"), self)\
            .activated.connect(lambda: self.taskSelection.setCurrentIndex(1))
        QShortcut(QKeySequence("Ctrl+Shift+s"), self)\
            .activated.connect(lambda: self.taskSelection.setCurrentIndex(2))


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
mainWindow = MainWindow()

QComboBox().currentIndex


mainWindow.show()
sys.exit(app.exec_())



"""
define a function cancate <-- function name
    that takes two strings and
    returns the cancatination of the two strings

    
make a python fucntion named sort
    that takes a list and sort it 
    accending order.
    returns the sorted list


define a function named is_allowed 
    that takes a user age and 
    check it he/she is older than 18
    return true if older than 18
    return false if not older than 18


define a function named user_info
    that takes 
        user name
        email
        age 
        gender
        height
    
Sample input:
    user_info("Ibad", "ibad@gmail.com", 22, "male", "5'2\"")
    user_info("Gulalam", "gulalam@gmail.com", 22, "male", "5'3\"")
    user_info("Doctor", "doctor@gmail.com", 20, "female", "4'9\"")

Sample output:
    Name: Ibad
    Email: ibad@gmail.com
    Age: 22
    Gender: male
    Height: 5'2"
    =================================
    Name: Gulalam
    Email: gulalam@gmail.com
    Age: 22
    Gender: male
    Height: 5'3"
    =================================
    Name: Doctor
    Email: doctor@gmail.com
    Age: 20
    Gender: female
    Height: 4'9"
    =================================

You have to create 2 functions in this task.
1. a function named find_gender:
    takes a variable gender
    returns 'he' if gender is male
    returns 'she' if gender is female

2. define a function named is_older 
    that takes a user age, and gender 
    check if he/she is older than 18
    return true if older than 18
    return false if not older than 18
    use the find_gender function to print 
    sutiable pronoun he for male she for female
Sample input:
    is_older(20, "male")
    is_older(17, "female")
Sample output:
    He is older than 18
    She is not older than 18
"""