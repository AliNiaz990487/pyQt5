from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic



class LogInWindow(QMainWindow):
    def __init__(self, createAccountWin):
        super().__init__()
        self.createAccountWin = createAccountWin

        uic.loadUi("ui/login_window.ui", self)

        self.dontAnyAccountBtn.clicked.connect(self.show_create_account)

    def show_create_account(self):
        self.createAccountWin.show()
    
