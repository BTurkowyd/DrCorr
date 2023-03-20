from PyQt5 import QtCore, QtWidgets
import sys
import modules.dbscan_widget as dbscan_widget
import modules.nena_widget as nena_widget
import modules.optics_widget as optics_widget
import modules.bead_analyzer as bead_analyzer
from modules.image_reconstruction2 import ImageReconstruction
import numpy as np
import pandas as pd
import os

from modules.particle import Particle

refPt = list()
resize = None
image = None
particles = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DrCorr 3")
        MainWindow.resize(420, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.inputFormat = QtWidgets.QComboBox(self.centralwidget)
        self.inputFormat.setGeometry(QtCore.QRect(20, 20, 120, 30))
        self.inputFormat.setObjectName("inputFormat")
        self.inputFormat.addItem("")
        self.inputFormat.addItem("")

        self.fiducialThresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.fiducialThresholdLabel.setGeometry(QtCore.QRect(20, 60, 120, 30))
        self.fiducialThresholdLabel.setObjectName("fiducialThresholdLabel")

        self.fiducialThreshold = QtWidgets.QTextEdit(self.centralwidget)
        self.fiducialThreshold.setGeometry(QtCore.QRect(20, 90, 120, 30))
        self.fiducialThreshold.setObjectName("fiducialThreshold")

        self.loadData = QtWidgets.QPushButton(self.centralwidget)
        self.loadData.setGeometry(QtCore.QRect(20, 130, 120, 30))
        self.loadData.setObjectName("loadData")
        self.loadData.clicked.connect(self.getFiles)
        self.loadData.setToolTip("Click this button to select localization and image files")

        self.imageDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.imageDisplay.setGeometry(QtCore.QRect(20, 170, 120, 30))
        self.imageDisplay.setToolTip("")
        self.imageDisplay.setToolTipDuration(-1)
        self.imageDisplay.setObjectName("imageDisplay")
        self.imageDisplay.clicked.connect(self.run_display_image)
        self.imageDisplay.setDisabled(True)

        self.delLastROI = QtWidgets.QPushButton(self.centralwidget)
        self.delLastROI.setGeometry(QtCore.QRect(20, 210, 120, 30))
        self.delLastROI.setObjectName("delLastROI")
        self.delLastROI.clicked.connect(self.run_remove_single_roi)
        self.delLastROI.setDisabled(True)

        self.delAllROIs = QtWidgets.QPushButton(self.centralwidget)
        self.delAllROIs.setGeometry(QtCore.QRect(20, 250, 120, 30))
        self.delAllROIs.setObjectName("delAllROIs")
        self.delAllROIs.clicked.connect(self.run_remove_all_rois)
        self.delAllROIs.setDisabled(True)

        self.beadAnalyzer = QtWidgets.QPushButton(self.centralwidget)
        self.beadAnalyzer.setGeometry(QtCore.QRect(20, 290, 120, 30))
        self.beadAnalyzer.setObjectName("analyzeFiducials")
        self.beadAnalyzer.clicked.connect(self.analyze_beads)
        self.beadAnalyzer.setDisabled(True)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 330, 200, 30))
        self.checkBox.setObjectName("checkBox")

        self.calculateNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.calculateNeNA.setGeometry(QtCore.QRect(20, 370, 120, 30))
        self.calculateNeNA.setObjectName("calculateNeNA")
        self.calculateNeNA.clicked.connect(self.run_nena)
        self.calculateNeNA.setDisabled(False)

        self.calculateTemporalNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.calculateTemporalNeNA.setGeometry(QtCore.QRect(20, 410, 120, 30))
        self.calculateTemporalNeNA.setObjectName("calculateTemporalNeNA")
        self.calculateTemporalNeNA.setDisabled(True)

        self.calculateDBSCAN = QtWidgets.QPushButton(self.centralwidget)
        self.calculateDBSCAN.setGeometry(QtCore.QRect(20, 470, 120, 30))
        self.calculateDBSCAN.setObjectName("calculateDBSCAN")
        self.calculateDBSCAN.clicked.connect(self.run_DBSCAN)
        self.calculateDBSCAN.setDisabled(True)

        self.calculateOPTICS = QtWidgets.QPushButton(self.centralwidget)
        self.calculateOPTICS.setGeometry(QtCore.QRect(150, 470, 120, 30))
        self.calculateOPTICS.setObjectName("calculateOPTICS")
        self.calculateOPTICS.clicked.connect(self.run_OPTICS)
        self.calculateOPTICS.setDisabled(True)

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(280, 470, 120, 30))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.close_program)

        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(20, 510, 380, 30))
        self.statusBar.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar.setObjectName("statusBar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 550, 380, 30))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.actionBefore_correction = QtWidgets.QAction(MainWindow)
        self.actionBefore_correction.setObjectName("actionBefore_correction")
        self.actionAfter_correction = QtWidgets.QAction(MainWindow)
        self.actionAfter_correction.setObjectName("actionAfter_correction")
        self.actionBefore_and_after_correction = QtWidgets.QAction(MainWindow)
        self.actionBefore_and_after_correction.setObjectName("actionBefore_and_after_correction")


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
        self.beadAnalyzer.setText(_translate("MainWindow", "Dr. corr."))
        self.checkBox.setText(_translate("MainWindow", "No corr. terms in NeNA"))
        self.calculateNeNA.setText(_translate("MainWindow", "Calculate NeNA"))
        self.calculateTemporalNeNA.setText(_translate("MainWindow", "Calc. temp. NeNA"))
        self.calculateDBSCAN.setText(_translate("MainWindow", "DBSCAN"))
        self.calculateOPTICS.setText(_translate("MainWindow", "OPTICS"))
        self.exitButton.setText(_translate("MainWindow", "Quit"))
        self.imageDisplay.setText(_translate("MainWindow", "Select ROIs"))
        self.statusBar.setText(_translate("MainWindow", "Hi!"))
        self.actionBefore_correction.setText(_translate("MainWindow", "Before correction"))
        self.actionAfter_correction.setText(_translate("MainWindow", "After correction"))
        self.actionBefore_and_after_correction.setText(_translate("MainWindow", "Before and after correction"))

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
            self.currentDirectory = os.path.dirname(self.locfileName)

        else:
            self.openFile = QtWidgets.QWidget()
            self.locfileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the localization file", "","CSV Files (*.csv) ;;All Files (*)")
            self.currentDirectory = os.path.dirname(self.locfileName)


        if self.locfileName:
            print(self.locfileName)
            self.load_particles()
            self.imageDisplay.setDisabled(False)
            self.delLastROI.setDisabled(False)
            self.delAllROIs.setDisabled(False)
            self.beadAnalyzer.setDisabled(False)
            self.calculateNeNA.setDisabled(False)
            self.calculateTemporalNeNA.setDisabled(False)
            self.calculateDBSCAN.setDisabled(False)
            self.calculateOPTICS.setDisabled(False)
            self.run_display_image()
            print("Data loaded")
        else:
            print("No data")

    def close_program(self):
        sys.exit(self)

    def analyze_beads(self):
        try:
            self.fidu_intensity = float(self.fiducialThreshold.toPlainText())
            self.anal_beads = bead_analyzer.Ui_BeadAnalyzer()
            self.image_recon.create_fiducials(self.fidu_intensity)
            self.anal_beads.setupUi(self.anal_beads, self, self.image_recon.selections, self.particles)
            self.anal_beads.show()
        except AttributeError:
            print("No fiducials selected")

    def load_ROIS(self):
        try:
            self.openROIs = QtWidgets.QWidget()
            self.ROIsFile, _ = QtWidgets.QFileDialog.getOpenFileName(self.openFile,"Select the ROIs file", "","ROI Files (*.roi) ;;All Files (*)")
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
            self.nena = nena_widget.Ui_NeNA()
            self.nena.setupUi(self.image_recon.selections, self.currentDirectory, self.nena, 1)
            self.nena.show()
        except (AttributeError, IndexError):
            print('Please select ROIs.')

    def run_DBSCAN(self):
        self.dbscan = dbscan_widget.Ui_DBSCANanalysis()
        self.dbscan.setupUi(self.image_recon, self.particles, self.inputFormat.currentText(), self.dbscan)
        self.dbscan.show()

    def run_OPTICS(self):
        self.optics = optics_widget.Ui_OPTICSanalysis()
        self.optics.setupUi(self.image_recon, self.particles, self.inputFormat.currentText() ,self.optics)
        self.optics.show()
