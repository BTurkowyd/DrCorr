# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from particle import Particle
import sys
import methods
import dbscan_widget
import optics_widget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DrCorr 3")
        MainWindow.resize(700, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inputFormat = QtWidgets.QComboBox(self.centralwidget)
        self.inputFormat.setGeometry(QtCore.QRect(20, 20, 200, 40))
        self.inputFormat.setObjectName("inputFormat")
        self.inputFormat.addItem("")
        self.inputFormat.addItem("")

        self.fiducialThreshold = QtWidgets.QTextEdit(self.centralwidget)
        self.fiducialThreshold.setGeometry(QtCore.QRect(20, 120, 200, 40))
        self.fiducialThreshold.setObjectName("fiducialThreshold")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 700, 600, 40))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.fiducialThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.fiducialThresholdLabel.setGeometry(QtCore.QRect(20, 70, 200, 40))
        self.fiducialThresholdLabel.setObjectName("fiducialThresholdLabel")

        self.loadData = QtWidgets.QPushButton(self.centralwidget)
        self.loadData.setGeometry(QtCore.QRect(20, 170, 200, 40))
        self.loadData.setObjectName("loadData")
        self.loadData.clicked.connect(self.getFiles)
        self.loadData.setToolTip("Click this button to select localization and image files")

        self.delLastROI = QtWidgets.QPushButton(self.centralwidget)
        self.delLastROI.setGeometry(QtCore.QRect(20, 270, 200, 40))
        self.delLastROI.setObjectName("delLastROI")
        self.delLastROI.clicked.connect(self.run_remove_single_roi)
        self.delLastROI.setDisabled(True)

        self.delAllROIs = QtWidgets.QPushButton(self.centralwidget)
        self.delAllROIs.setGeometry(QtCore.QRect(20, 320, 200, 40))
        self.delAllROIs.setObjectName("delAllROIs")
        self.delAllROIs.clicked.connect(self.runremove_all_rois)
        self.delAllROIs.setDisabled(True)

        self.driftCorrection = QtWidgets.QPushButton(self.centralwidget)
        self.driftCorrection.setGeometry(QtCore.QRect(20, 370, 200, 40))
        self.driftCorrection.setObjectName("driftCorrection")
        self.driftCorrection.clicked.connect(self.run_dr_corr)
        self.driftCorrection.setDisabled(True)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 450, 400, 40))
        self.checkBox.setObjectName("checkBox")

        self.calculateNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.calculateNeNA.setGeometry(QtCore.QRect(20, 500, 200, 40))
        self.calculateNeNA.setObjectName("calculateNeNA")
        self.calculateNeNA.clicked.connect(self.run_nena)
        self.calculateNeNA.setDisabled(True)

        self.calculateTemporalNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.calculateTemporalNeNA.setGeometry(QtCore.QRect(20, 550, 200, 40))
        self.calculateTemporalNeNA.setObjectName("calculateTemporalNeNA")
        self.calculateTemporalNeNA.setDisabled(True)

        self.calculateDBSCAN = QtWidgets.QPushButton(self.centralwidget)
        self.calculateDBSCAN.setGeometry(QtCore.QRect(20, 630, 200, 40))
        self.calculateDBSCAN.setObjectName("calculateDBSCAN")
        self.calculateDBSCAN.clicked.connect(self.run_DBSCAN)
        self.calculateDBSCAN.setDisabled(True)

        self.calculateOPTICS = QtWidgets.QPushButton(self.centralwidget)
        self.calculateOPTICS.setGeometry(QtCore.QRect(250, 630, 200, 40))
        self.calculateOPTICS.setObjectName("calculateOPTICS")
        self.calculateOPTICS.clicked.connect(self.run_OPTICS)
        self.calculateOPTICS.setDisabled(True)

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(480, 630, 200, 40))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.close_program)

        self.imageDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.imageDisplay.setGeometry(QtCore.QRect(20, 220, 200, 40))
        self.imageDisplay.setToolTip("")
        self.imageDisplay.setToolTipDuration(-1)
        self.imageDisplay.setObjectName("imageDisplay")
        self.imageDisplay.clicked.connect(self.run_display_image)
        self.imageDisplay.setDisabled(True)

        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(150, 750, 400, 40))
        self.statusBar.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar.setObjectName("statusBar")  
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)      

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DrCorr 3.0"))
        self.inputFormat.setItemText(0, _translate("MainWindow", "RapidSTORM"))
        self.inputFormat.setItemText(1, _translate("MainWindow", "ThunderSTORM"))
        self.fiducialThreshold.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10000</p></body></html>"))
        self.fiducialThresholdLabel.setText(_translate("MainWindow", "Fiducial Threshold:"))
        self.loadData.setText(_translate("MainWindow", "Load data"))
        self.delLastROI.setText(_translate("MainWindow", "Delete last ROI"))
        self.delAllROIs.setText(_translate("MainWindow", "Delete all ROIs"))
        self.driftCorrection.setText(_translate("MainWindow", "Drift correction"))
        self.checkBox.setText(_translate("MainWindow", "No corr. terms in NeNA"))
        self.calculateNeNA.setText(_translate("MainWindow", "Calculate NeNA"))
        self.calculateTemporalNeNA.setText(_translate("MainWindow", "Calc. temp. NeNA"))
        self.calculateDBSCAN.setText(_translate("MainWindow", "DBSCAN"))
        self.calculateOPTICS.setText(_translate("MainWindow", "OPTICS"))
        self.exitButton.setText(_translate("MainWindow", "Quit"))
        self.imageDisplay.setText(_translate("MainWindow", "Select ROIs"))
        self.statusBar.setText(_translate("MainWindow", "Hi!"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def getFiles(self):
        if self.inputFormat.currentText() == "RapidSTORM":
            self.openFile = QtWidgets.QWidget()
            self.locfileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the localization file", "","TXT Files (*.txt) ;;All Files (*)")
        else:
            self.openFile = QtWidgets.QWidget()
            self.locfileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the localization file", "","CSV Files (*.csv) ;;All Files (*)")
        self.imgFileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the image reconstruction", "","PNG Files (*.PNG) ;; All Files (*)")

        if self.locfileName and self.imgFileName:
            print(self.locfileName)
            methods.refPt = []
            self.imageDisplay.setDisabled(False)
            self.delLastROI.setDisabled(False)
            self.delAllROIs.setDisabled(False)
            self.driftCorrection.setDisabled(False)
            self.calculateNeNA.setDisabled(False)
            self.calculateTemporalNeNA.setDisabled(False)
            self.calculateDBSCAN.setDisabled(False)
            self.calculateOPTICS.setDisabled(False)
            print("Data loaded")
        else:
            print("No data")

    def close_program(self):
        sys.exit(self)

    def run_dr_corr(self):
        # try:
        self.fidu_intensity = float(self.fiducialThreshold.toPlainText())
        methods.dr_corr(self)
        # except:
        #     print("Please select ROI first")

    def run_remove_single_roi(self):
        try:
            methods.remove_single_roi()
        except:
            print("There is no ROIs")

    def runremove_all_rois(self):
        try:
            methods.remove_all_rois()
        except:
            print("There is no ROIs")
    
    def run_display_image(self):
        methods.display_image(self)
    
    def run_nena(self):
        methods.neNa(self, self.locfileName, self.imgFileName)
    
    def run_DBSCAN(self):
        self.dbscan = dbscan_widget.Ui_DBSCANanalysis()
        self.dbscan.setupUi(self.dbscan)
        self.dbscan.show()

    def run_OPTICS(self):
        self.optics = optics_widget.Ui_OPTICSanalysis()
        self.optics.setupUi(self.optics)
        self.optics.show()
