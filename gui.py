# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import sys
import methods
import dbscan_widget
import nena_widget
import optics_widget
import swift_wrapper
import bead_analyzer
from image_reconstruction2 import ImageReconstruction
import numpy as np
import pandas as pd

from particle import Particle

refPt = list()
resize = None
image = None
particles = []


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
        self.delAllROIs.clicked.connect(self.run_remove_all_rois)
        self.delAllROIs.setDisabled(True)

        self.beadAnalyzer = QtWidgets.QPushButton(self.centralwidget)
        self.beadAnalyzer.setGeometry(QtCore.QRect(20, 370, 200, 40))
        self.beadAnalyzer.setObjectName("analyzeFiducials")
        self.beadAnalyzer.clicked.connect(self.analyze_beads)
        self.beadAnalyzer.setDisabled(True)

        self.loadROIs = QtWidgets.QPushButton(self.centralwidget)
        self.loadROIs.setGeometry(QtCore.QRect(230, 170, 200, 40))
        self.loadROIs.setObjectName("loadROIs")
        self.loadROIs.clicked.connect(self.load_ROIS)
        self.loadROIs.setDisabled(True)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 450, 400, 40))
        self.checkBox.setObjectName("checkBox")

        self.calculateNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.calculateNeNA.setGeometry(QtCore.QRect(20, 500, 200, 40))
        self.calculateNeNA.setObjectName("calculateNeNA")
        self.calculateNeNA.clicked.connect(self.run_nena)
        self.calculateNeNA.setDisabled(False)

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

        self.menuPlot = QtWidgets.QMenu(self.menubar)
        self.menuPlot.setObjectName("menuPlot")
        self.menuSWIFT = QtWidgets.QMenu(self.menubar)
        self.menuSWIFT.setObjectName("menuSWIFT")
        self.actionBefore_correction = QtWidgets.QAction(MainWindow)
        self.actionBefore_correction.setObjectName("actionBefore_correction")
        self.actionAfter_correction = QtWidgets.QAction(MainWindow)
        self.actionAfter_correction.setObjectName("actionAfter_correction")
        self.actionBefore_and_after_correction = QtWidgets.QAction(MainWindow)
        self.actionBefore_and_after_correction.setObjectName("actionBefore_and_after_correction")
        self.actionRun_SWIFT = QtWidgets.QAction(MainWindow)
        self.actionRun_SWIFT.setObjectName("actionRun_SWIFT")
        self.actionRun_SWIFT.triggered.connect(self.run_swift)
        self.menuPlot.addAction(self.actionBefore_correction)
        self.menuPlot.addAction(self.actionAfter_correction)
        self.menuPlot.addAction(self.actionBefore_and_after_correction)
        self.menuSWIFT.addAction(self.actionRun_SWIFT)
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuSWIFT.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.image_recon = None
        self.particles = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DrCorr 3.0"))
        self.inputFormat.setItemText(0, _translate("MainWindow", "RapidSTORM"))
        self.inputFormat.setItemText(1, _translate("MainWindow", "ThunderSTORM"))
        self.fiducialThreshold.setHtml(_translate("MainWindow", "10000"))
        self.fiducialThresholdLabel.setText(_translate("MainWindow", "Fiducial Threshold:"))
        self.loadData.setText(_translate("MainWindow", "Load data"))
        self.delLastROI.setText(_translate("MainWindow", "Delete last ROI"))
        self.delAllROIs.setText(_translate("MainWindow", "Delete all ROIs"))
        self.beadAnalyzer.setText(_translate("MainWindow", "Bead analyzer + Dr. corr."))
        self.loadROIs.setText(_translate("MainWindow", "Load ROIs"))
        self.checkBox.setText(_translate("MainWindow", "No corr. terms in NeNA"))
        self.calculateNeNA.setText(_translate("MainWindow", "Calculate NeNA"))
        self.calculateTemporalNeNA.setText(_translate("MainWindow", "Calc. temp. NeNA"))
        self.calculateDBSCAN.setText(_translate("MainWindow", "DBSCAN"))
        self.calculateOPTICS.setText(_translate("MainWindow", "OPTICS"))
        self.exitButton.setText(_translate("MainWindow", "Quit"))
        self.imageDisplay.setText(_translate("MainWindow", "Select ROIs"))
        self.statusBar.setText(_translate("MainWindow", "Hi!"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot"))
        self.menuSWIFT.setTitle(_translate("MainWindow", "SWIFT"))
        self.actionBefore_correction.setText(_translate("MainWindow", "Before correction"))
        self.actionAfter_correction.setText(_translate("MainWindow", "After correction"))
        self.actionBefore_and_after_correction.setText(_translate("MainWindow", "Before and after correction"))
        self.actionRun_SWIFT.setText(_translate("MainWindow", "Run SWIFT"))

    def load_particles(self):
        try:
            global image, resize, refPt, particles

            if self.inputFormat.currentText() == "RapidSTORM":
                loc = np.loadtxt(self.locfileName)
                self.particles = [Particle(p[0], p[1], p[2], p[3]) for p in loc]
            else:
                loc = pd.read_csv(self.locfileName)
                self.particles = [Particle(p[2], p[3], p[1], p[5], p[0], p[4], p[6], p[7], p[8], p[9]) for p in loc.values]
        except:
            print("Localization file not loaded")

    def getFiles(self):
        if self.inputFormat.currentText() == "RapidSTORM":
            self.openFile = QtWidgets.QWidget()
            self.locfileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the localization file", "","TXT Files (*.txt) ;;All Files (*)")
        else:
            self.openFile = QtWidgets.QWidget()
            self.locfileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the localization file", "","CSV Files (*.csv) ;;All Files (*)")
        # self.imgFileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the image reconstruction", "","PNG Files (*.PNG) ;; All Files (*)")

        if self.locfileName:
            print(self.locfileName)
            methods.refPt = []
            self.load_particles()
            self.imageDisplay.setDisabled(False)
            self.delLastROI.setDisabled(False)
            self.delAllROIs.setDisabled(False)
            # self.analyzeFiducials.setDisabled(False)
            self.beadAnalyzer.setDisabled(False)
            self.loadROIs.setDisabled(False)
            # self.driftCorrection.setDisabled(False)
            self.calculateNeNA.setDisabled(False)
            self.calculateTemporalNeNA.setDisabled(False)
            self.calculateDBSCAN.setDisabled(False)
            self.calculateOPTICS.setDisabled(False)
            print("Data loaded")
        else:
            print("No data")

    def close_program(self):
        sys.exit(self)

    def analyze_beads(self):
        print(self.fidu_intensity)
        self.fidu_intensity = float(self.fiducialThreshold.toPlainText())
        self.anal_beads = bead_analyzer.Ui_BeadAnalyzer()
        self.image_recon.create_fiducials(self.fidu_intensity)
        self.anal_beads.setupUi(self.anal_beads, self, self.image_recon.selections, self.particles)
        self.anal_beads.show()

    def load_ROIS(self):
        try:
            self.openROIs = QtWidgets.QWidget()
            self.ROIsFile, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the ROIs file", "","ROI Files (*.roi) ;;All Files (*)")

            methods.load_ROIS(self)

        except:
            print("There is no ROIs")

    def run_remove_single_roi(self):
        try:
            self.image_recon.del_last_selection()
        except:
            print("There are no ROIs")

    def run_remove_all_rois(self):
        try:
            self.image_recon.del_all_selections()
        except:
            print("There are no ROIs")

    def run_display_image(self):
        self.imageDisplay.setDisabled(True)
        self.fidu_intensity = float(self.fiducialThreshold.toPlainText())
        self.image_recon = ImageReconstruction(self.locfileName, self.fidu_intensity, self.inputFormat.currentText())
        self.imageDisplay.setDisabled(False)

    def run_nena(self):
        try:
            self.image_recon.create_fiducials(0)
            for i, sele in enumerate(self.image_recon.selections):
                self.nena = nena_widget.Ui_NeNA()
                self.nena.setupUi(sele, self.nena, i+1)
                self.nena.show()
                # self.runNena = methods.NeNACalculation(self, self, self.image_recon, self.locfileName)
            # self.runNena.run()
        except AttributeError:
            print('Please select ROIs.')
        # methods.neNa(self, self.locfileName, self.imgFileName)

    def run_DBSCAN(self):
        self.dbscan = dbscan_widget.Ui_DBSCANanalysis()
        self.dbscan.setupUi(self.image_recon, self.inputFormat.currentText(), self.dbscan)
        self.dbscan.show()

    def run_OPTICS(self):
        self.optics = optics_widget.Ui_OPTICSanalysis()
        self.optics.setupUi(self.image_recon, self.inputFormat.currentText() ,self.optics)
        self.optics.show()

    def run_swift(self):
        self.swift = swift_wrapper.Ui_swift_wrapper()
        self.swift.setupUi(self.swift)
        self.swift.show()