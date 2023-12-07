from PyQt5.QtWidgets import QApplication, QLabel
# import what we need

app = QApplication([])
# creates the main window of the application
# receives command line arguments but just leave it blank fon now.


label = QLabel("Hello World!")
# A text on the window
label = QLabel("<font size=160 color=red>Hello World!</font>")
# we can also use the html syntex here
label.show()
# show the label on the window

app.exec()
# main loop of the program to keep it stay until we want
# by removing it, the application is build run but suddenly disappears
# and we were not able to just see it.


###################### A BIT ADVANCE VERSION ##############################################
from PyQt5.QtWidgets import QWidget

def window():
   app = QApplication([])
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(500, 500, 200, 400)
   # 1. xPosition (initial display position)
   # 2. yPosition (initial display position)
   # 3. width (width of the window)
   # 4. height (height of the window)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()

   app.exec_()


window()
