# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 850)
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
        self.loadData.setToolTip("")
        self.loadData.setProperty("toolTipDuration", -1)
        self.loadData.setObjectName("loadData")
        self.delLastROI = QtWidgets.QPushButton(self.centralwidget)
        self.delLastROI.setGeometry(QtCore.QRect(20, 270, 200, 40))
        self.delLastROI.setObjectName("delLastROI")
        self.delAllROIs = QtWidgets.QPushButton(self.centralwidget)
        self.delAllROIs.setGeometry(QtCore.QRect(20, 320, 200, 40))
        self.delAllROIs.setObjectName("delAllROIs")
        self.driftCorrection = QtWidgets.QPushButton(self.centralwidget)
        self.driftCorrection.setGeometry(QtCore.QRect(20, 370, 200, 40))
        self.driftCorrection.setObjectName("driftCorrection")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 450, 400, 40))
        self.checkBox.setObjectName("checkBox")
        self.calculateNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.calculateNeNA.setGeometry(QtCore.QRect(20, 500, 200, 40))
        self.calculateNeNA.setObjectName("calculateNeNA")
        self.calculateTemporalNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.calculateTemporalNeNA.setGeometry(QtCore.QRect(20, 550, 200, 40))
        self.calculateTemporalNeNA.setObjectName("calculateTemporalNeNA")
        self.calculateDBSCAN = QtWidgets.QPushButton(self.centralwidget)
        self.calculateDBSCAN.setGeometry(QtCore.QRect(20, 630, 200, 40))
        self.calculateDBSCAN.setObjectName("calculateDBSCAN")
        self.calculateOPTICS = QtWidgets.QPushButton(self.centralwidget)
        self.calculateOPTICS.setGeometry(QtCore.QRect(250, 630, 200, 40))
        self.calculateOPTICS.setObjectName("calculateOPTICS")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(480, 630, 200, 40))
        self.exitButton.setObjectName("exitButton")
        self.imageDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.imageDisplay.setGeometry(QtCore.QRect(20, 220, 200, 40))
        self.imageDisplay.setToolTip("")
        self.imageDisplay.setProperty("toolTipDuration", -1)
        self.imageDisplay.setObjectName("imageDisplay")
        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(250, 760, 200, 40))
        self.statusBar.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar.setObjectName("statusBar")
        self.analyzeFiducials = QtWidgets.QPushButton(self.centralwidget)
        self.analyzeFiducials.setGeometry(QtCore.QRect(230, 320, 200, 40))
        self.analyzeFiducials.setObjectName("analyzeFiducials")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 22))
        self.menubar.setObjectName("menubar")
        self.menuPlot = QtWidgets.QMenu(self.menubar)
        self.menuPlot.setObjectName("menuPlot")
        self.menuSWIFT = QtWidgets.QMenu(self.menubar)
        self.menuSWIFT.setObjectName("menuSWIFT")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionBefore_correction = QtWidgets.QAction(MainWindow)
        self.actionBefore_correction.setObjectName("actionBefore_correction")
        self.actionAfter_correction = QtWidgets.QAction(MainWindow)
        self.actionAfter_correction.setObjectName("actionAfter_correction")
        self.actionBEfire_and_after_correction = QtWidgets.QAction(MainWindow)
        self.actionBEfire_and_after_correction.setObjectName("actionBEfire_and_after_correction")
        self.actionRun_SWIFT = QtWidgets.QAction(MainWindow)
        self.actionRun_SWIFT.setObjectName("actionRun_SWIFT")
        self.menuPlot.addAction(self.actionBefore_correction)
        self.menuPlot.addAction(self.actionAfter_correction)
        self.menuPlot.addAction(self.actionBEfire_and_after_correction)
        self.menuSWIFT.addAction(self.actionRun_SWIFT)
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuSWIFT.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputFormat.setItemText(0, _translate("MainWindow", "RapidSTORM"))
        self.inputFormat.setItemText(1, _translate("MainWindow", "ThunderSTORM"))
        self.fiducialThreshold.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">10000</span></p></body></html>"))
        self.fiducialThresholdLabel.setText(_translate("MainWindow", "Fiducial Threshold:"))
        self.loadData.setText(_translate("MainWindow", "Load data"))
        self.delLastROI.setText(_translate("MainWindow", "Delete last ROI"))
        self.delAllROIs.setText(_translate("MainWindow", "Delete all ROIs"))
        self.driftCorrection.setText(_translate("MainWindow", "Drift correction"))
        self.checkBox.setText(_translate("MainWindow", "Ignore correction terms in NeNA"))
        self.calculateNeNA.setText(_translate("MainWindow", "Calculate NeNA"))
        self.calculateTemporalNeNA.setText(_translate("MainWindow", "Calculate temp. NeNA"))
        self.calculateDBSCAN.setText(_translate("MainWindow", "DBSCAN"))
        self.calculateOPTICS.setText(_translate("MainWindow", "OPTICS"))
        self.exitButton.setText(_translate("MainWindow", "Quit"))
        self.imageDisplay.setText(_translate("MainWindow", "Image display"))
        self.statusBar.setText(_translate("MainWindow", "Hi!"))
        self.analyzeFiducials.setText(_translate("MainWindow", "Analyze fiducials"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot"))
        self.menuSWIFT.setTitle(_translate("MainWindow", "SWIFT"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionBefore_correction.setText(_translate("MainWindow", "Before correction"))
        self.actionAfter_correction.setText(_translate("MainWindow", "After correction"))
        self.actionBEfire_and_after_correction.setText(_translate("MainWindow", "Before and after correction"))
        self.actionRun_SWIFT.setText(_translate("MainWindow", "Run SWIFT"))

