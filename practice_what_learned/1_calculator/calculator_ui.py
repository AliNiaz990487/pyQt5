# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/aliniaz/Desktop/pyQt5/practice_what_learned/1_calculator/calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(358, 284)
        calculator.setMinimumSize(QtCore.QSize(0, 284))
        calculator.setMaximumSize(QtCore.QSize(358, 284))
        calculator.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setText("")
        self.result.setObjectName("result")
        self.horizontalLayout.addWidget(self.result)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setObjectName("btn0")
        self.gridLayout_2.addWidget(self.btn0, 3, 1, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setObjectName("btn5")
        self.gridLayout_2.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setObjectName("btn9")
        self.gridLayout_2.addWidget(self.btn9, 2, 2, 1, 1)
        self.btnDot = QtWidgets.QPushButton(self.centralwidget)
        self.btnDot.setObjectName("btnDot")
        self.gridLayout_2.addWidget(self.btnDot, 3, 2, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setObjectName("btn7")
        self.gridLayout_2.addWidget(self.btn7, 2, 0, 1, 1)
        self.btnMinus = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinus.setObjectName("btnMinus")
        self.gridLayout_2.addWidget(self.btnMinus, 3, 3, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setObjectName("btn6")
        self.gridLayout_2.addWidget(self.btn6, 1, 2, 1, 1)
        self.btnPlus = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlus.setObjectName("btnPlus")
        self.gridLayout_2.addWidget(self.btnPlus, 2, 3, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.gridLayout_2.addWidget(self.btn2, 0, 1, 1, 1)
        self.btnMultiply = QtWidgets.QPushButton(self.centralwidget)
        self.btnMultiply.setObjectName("btnMultiply")
        self.gridLayout_2.addWidget(self.btnMultiply, 1, 3, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setObjectName("btn8")
        self.gridLayout_2.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setObjectName("btn1")
        self.gridLayout_2.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setObjectName("btn4")
        self.gridLayout_2.addWidget(self.btn4, 1, 0, 1, 1)
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setObjectName("btnDel")
        self.gridLayout_2.addWidget(self.btnDel, 3, 0, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setObjectName("btn3")
        self.gridLayout_2.addWidget(self.btn3, 0, 2, 1, 1)
        self.btnDivide = QtWidgets.QPushButton(self.centralwidget)
        self.btnDivide.setObjectName("btnDivide")
        self.gridLayout_2.addWidget(self.btnDivide, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.btnCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName("btnCalculate")
        self.verticalLayout.addWidget(self.btnCalculate)
        calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 358, 22))
        self.menubar.setObjectName("menubar")
        calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(calculator)
        self.statusbar.setObjectName("statusbar")
        calculator.setStatusBar(self.statusbar)

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "MainWindow"))
        self.btn0.setText(_translate("calculator", "0"))
        self.btn5.setText(_translate("calculator", "5"))
        self.btn9.setText(_translate("calculator", "9"))
        self.btnDot.setText(_translate("calculator", "."))
        self.btn7.setText(_translate("calculator", "7"))
        self.btnMinus.setText(_translate("calculator", "-"))
        self.btn6.setText(_translate("calculator", "6"))
        self.btnPlus.setText(_translate("calculator", "+"))
        self.btn2.setText(_translate("calculator", "2"))
        self.btnMultiply.setText(_translate("calculator", "*"))
        self.btn8.setText(_translate("calculator", "8"))
        self.btn1.setText(_translate("calculator", "1"))
        self.btn4.setText(_translate("calculator", "4"))
        self.btnDel.setText(_translate("calculator", "DEL"))
        self.btn3.setText(_translate("calculator", "3"))
        self.btnDivide.setText(_translate("calculator", "/"))
        self.btnCalculate.setText(_translate("calculator", "Calculate"))
