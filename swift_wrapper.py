# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swift_wrapper.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_swift_wrapper(QtWidgets.QMainWindow):
    def setupUi(self, swift_wrapper):
        swift_wrapper.setObjectName("swift_wrapper")
        swift_wrapper.resize(700, 380)
        self.centralwidget = QtWidgets.QWidget(swift_wrapper)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 40))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 200, 40))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 300, 40))
        self.label_3.setObjectName("label_3")
        self.swiftEXE = QtWidgets.QTextEdit(self.centralwidget)
        self.swiftEXE.setGeometry(QtCore.QRect(200, 10, 350, 40))
        self.swiftEXE.setObjectName("swiftEXE")
        self.swiftConfig = QtWidgets.QTextEdit(self.centralwidget)
        self.swiftConfig.setGeometry(QtCore.QRect(200, 60, 350, 40))
        self.swiftConfig.setObjectName("swiftConfig")
        self.swiftInputParams = QtWidgets.QTextEdit(self.centralwidget)
        self.swiftInputParams.setGeometry(QtCore.QRect(200, 110, 350, 80))
        self.swiftInputParams.setObjectName("swiftInputParams")
        self.findCli = QtWidgets.QPushButton(self.centralwidget)
        self.findCli.setGeometry(QtCore.QRect(610, 10, 75, 40))
        self.findCli.setObjectName("findCli")
        self.findConfig = QtWidgets.QPushButton(self.centralwidget)
        self.findConfig.setGeometry(QtCore.QRect(610, 60, 75, 40))
        self.findConfig.setObjectName("findConfig")
        self.findInputFile = QtWidgets.QPushButton(self.centralwidget)
        self.findInputFile.setGeometry(QtCore.QRect(610, 200, 75, 40))
        self.findInputFile.setObjectName("findInputFile")
        self.inputFile = QtWidgets.QTextEdit(self.centralwidget)
        self.inputFile.setGeometry(QtCore.QRect(200, 200, 350, 40))
        self.inputFile.setObjectName("inputFile")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 200, 40))
        self.label_4.setObjectName("label_4")
        self.runSwift_cli = QtWidgets.QPushButton(self.centralwidget)
        self.runSwift_cli.setGeometry(QtCore.QRect(200, 280, 300, 40))
        self.runSwift_cli.setObjectName("runSwift_cli")
        swift_wrapper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(swift_wrapper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        swift_wrapper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(swift_wrapper)
        self.statusbar.setObjectName("statusbar")
        swift_wrapper.setStatusBar(self.statusbar)

        self.retranslateUi(swift_wrapper)
        QtCore.QMetaObject.connectSlotsByName(swift_wrapper)

    def retranslateUi(self, swift_wrapper):
        _translate = QtCore.QCoreApplication.translate
        swift_wrapper.setWindowTitle(_translate("swift_wrapper", "SWIFT"))
        self.label.setText(_translate("swift_wrapper", "swift_cli.exe path:"))
        self.label_2.setText(_translate("swift_wrapper", "swift config (json):"))
        self.label_3.setText(_translate("swift_wrapper", "Parameters:"))
        self.findCli.setText(_translate("swift_wrapper", "Search"))
        self.findConfig.setText(_translate("swift_wrapper", "Search"))
        self.findInputFile.setText(_translate("swift_wrapper", "Search"))
        self.label_4.setText(_translate("swift_wrapper", "Input loc. file:"))
        self.runSwift_cli.setText(_translate("swift_wrapper", "Run swift"))

