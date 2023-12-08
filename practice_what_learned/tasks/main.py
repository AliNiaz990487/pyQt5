import sys
from PyQt5.QtWidgets import *

from login import *
from create_account import *

tasks = QApplication(sys.argv)

createAccountWin = CreateAccountWindow()
logInWin = LogInWindow(createAccountWin)


logInWin.show()
# createAccountWin.show()


sys.exit(tasks.exec_())