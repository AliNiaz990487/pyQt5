import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

def add_text(label, text):
    result = label.text()+text
    label.setText(result)

app = QApplication(sys.argv)
calculator = QMainWindow()
ui = uic.loadUi("calculator.ui", calculator)

calculator.show()

calculator.btn0.clicked.connect(lambda: add_text(calculator.result, calculator.btn0.text()))
calculator.btn1.clicked.connect(lambda: add_text(calculator.result, calculator.btn1.text()))
calculator.btn2.clicked.connect(lambda: add_text(calculator.result, calculator.btn2.text()))
calculator.btn3.clicked.connect(lambda: add_text(calculator.result, calculator.btn3.text()))
calculator.btn4.clicked.connect(lambda: add_text(calculator.result, calculator.btn4.text()))
calculator.btn5.clicked.connect(lambda: add_text(calculator.result, calculator.btn5.text()))
calculator.btn6.clicked.connect(lambda: add_text(calculator.result, calculator.btn6.text()))
calculator.btn7.clicked.connect(lambda: add_text(calculator.result, calculator.btn7.text()))
calculator.btn8.clicked.connect(lambda: add_text(calculator.result, calculator.btn8.text()))
calculator.btn9.clicked.connect(lambda: add_text(calculator.result, calculator.btn9.text()))

calculator.btnDivide.clicked.connect(lambda: add_text(calculator.result, calculator.btnDivide.text()))
calculator.btnMultiply.clicked.connect(lambda: add_text(calculator.result, calculator.btnMultiply.text()))
calculator.btnMinus.clicked.connect(lambda: add_text(calculator.result, calculator.btnMinus.text()))
calculator.btnPlus.clicked.connect(lambda: add_text(calculator.result, calculator.btnPlus.text()))
calculator.btnDot.clicked.connect(lambda: add_text(calculator.result, calculator.btnDot.text()))

calculator.btnDel.clicked.connect(lambda: calculator.result.setText(""))


def get_result():
    return f"{eval(calculator.result.text())}"


calculator.btnCalculate.clicked.connect(lambda: calculator.result.setText(get_result()))


sys.exit(app.exec_())


