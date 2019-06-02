# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'swift_wrapper.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import subprocess

class Ui_swift_wrapper(QtWidgets.QMainWindow):
    def setupUi(self, swift_wrapper):
        swift_wrapper.setObjectName("swift_wrapper")
        swift_wrapper.resize(1200, 380)
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
        self.swiftEXE.setGeometry(QtCore.QRect(200, 10, 880, 40))
        self.swiftEXE.setObjectName("swiftEXE")
        self.swiftEXE.setDisabled(True)
        self.swiftConfig = QtWidgets.QTextEdit(self.centralwidget)
        self.swiftConfig.setGeometry(QtCore.QRect(200, 60, 880, 40))
        self.swiftConfig.setObjectName("swiftConfig")
        self.swiftConfig.setDisabled(True)
        self.swiftInputParams = QtWidgets.QTextEdit(self.centralwidget)
        self.swiftInputParams.setGeometry(QtCore.QRect(200, 110, 880, 80))
        self.swiftInputParams.setObjectName("swiftInputParams")
        self.findCli = QtWidgets.QPushButton(self.centralwidget)
        self.findCli.setGeometry(QtCore.QRect(1110, 10, 75, 40))
        self.findCli.setObjectName("findCli")
        self.findCli.clicked.connect(self.get_swift_cli)
        self.findConfig = QtWidgets.QPushButton(self.centralwidget)
        self.findConfig.setGeometry(QtCore.QRect(1110, 60, 75, 40))
        self.findConfig.setObjectName("findConfig")
        self.findConfig.clicked.connect(self.get_swift_config)
        self.findInputFile = QtWidgets.QPushButton(self.centralwidget)
        self.findInputFile.setGeometry(QtCore.QRect(1110, 200, 75, 40))
        self.findInputFile.setObjectName("findInputFile")
        self.findInputFile.clicked.connect(self.open_loc_file)
        self.inputFile = QtWidgets.QTextEdit(self.centralwidget)
        self.inputFile.setGeometry(QtCore.QRect(200, 200, 880, 40))
        self.inputFile.setObjectName("inputFile")
        self.inputFile.setDisabled(True)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 200, 40))
        self.label_4.setObjectName("label_4")
        self.runSwift_cli = QtWidgets.QPushButton(self.centralwidget)
        self.runSwift_cli.setGeometry(QtCore.QRect(450, 280, 300, 40))
        self.runSwift_cli.setObjectName("runSwift_cli")
        self.runSwift_cli.clicked.connect(self.run_tracking)
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

        try:
            with open("swift_configuration.json", "r") as f:
                self.swift_configuration = json.load(f)
                self.swiftEXE.setText(self.swift_configuration["swift_cli.exe path"])
                self.swiftConfig.setText(self.swift_configuration["swift config (json)"])
                self.swiftInputParams.setText(self.swift_configuration["Parameters"])
        except FileNotFoundError:
            print("Config not found")

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

    def get_swift_cli(self):
        self.openFile = QtWidgets.QWidget()
        self.cliFileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the swift_cli.exe file", self.swift_configuration["swift_cli.exe path"],"EXE Files (*.exe) ;;All Files (*)")
        self.swiftEXE.setText(self.cliFileName)
        self.swift_configuration["swift_cli.exe path"] = self.cliFileName

        with open("swift_configuration.json", "w") as f:
            json.dump(self.swift_configuration, f)

    def get_swift_config(self):
        self.openFile = QtWidgets.QWidget()
        self.swiftCfgName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the config (JSON) file", self.swift_configuration["swift config (json)"],"JSON Files (*.JSON) ;;All Files (*)")
        self.swiftConfig.setText(self.swiftCfgName)
        self.swift_configuration["swift config (json)"] = self.swiftCfgName

        with open("swift_configuration.json", "w") as f:
            json.dump(self.swift_configuration, f)
    
    def open_loc_file(self):
        self.openFile = QtWidgets.QWidget()
        self.locfileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the localization file", "","TXT Files (*.txt) ;; CSV Files (*.csv) ;; All Files (*)")
        self.inputFile.setText(self.locfileName)
    
    def run_tracking(self):
        subprocess.run(
            self.swiftEXE.toPlainText() + " " + self.inputFile.toPlainText() + " -c " + self.swiftConfig.toPlainText()
        )