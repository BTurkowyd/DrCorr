# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bead_analyzer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import methods


class Ui_BeadAnalyzer(QtWidgets.QMainWindow):
    def setupUi(self, BeadAnalyzer, app, fiducials, particles):
        try:
            self.fiducials = fiducials
            self.particles = particles
            
        except AttributeError:
            print('No ROIs selected')

        self.mother_app = app

        BeadAnalyzer.setObjectName("Bead Analyzer")
        BeadAnalyzer.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(BeadAnalyzer)
        self.centralwidget.setObjectName("beadAnalyzerWidget")

        self.analayzeBeads = QtWidgets.QPushButton(self.centralwidget)
        self.analayzeBeads.setGeometry(QtCore.QRect(10, 520, 96, 32))
        self.analayzeBeads.setObjectName("analayzeBeads")
        self.analayzeBeads.clicked.connect(self.analyze_fiducials)

        self.applyDriftCorr = QtWidgets.QPushButton(self.centralwidget)
        self.applyDriftCorr.setGeometry(QtCore.QRect(120, 520, 96, 32))
        self.applyDriftCorr.setObjectName("applyDriftCorr")
        self.applyDriftCorr.clicked.connect(self.apply_drift_corr)

        self.quiteBeadsAnal = QtWidgets.QPushButton(self.centralwidget)
        self.quiteBeadsAnal.setGeometry(QtCore.QRect(290, 520, 96, 32))
        self.quiteBeadsAnal.setObjectName("quiteBeadsAnal")
        self.quiteBeadsAnal.clicked.connect(self.close)
        
        self.listOfFiducials = QtWidgets.QFrame(self.centralwidget)
        self.listOfFiducials.setGeometry(QtCore.QRect(10, 10, 381, 441))
        self.listOfFiducials.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listOfFiducials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listOfFiducials.setObjectName("listOfFiducials")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.listOfFiducials)
        self.verticalScrollBar.setGeometry(QtCore.QRect(360, 0, 16, 441))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.fiducialCheckBoxes = []

        try:
            for i, _ in enumerate(self.fiducials):
                self.fiducialCheckBoxes.append(QtWidgets.QCheckBox(self.listOfFiducials))
                if i < 14:
                    self.fiducialCheckBoxes[-1].setGeometry(QtCore.QRect(10, 10 + i*30, 90, 20))
                elif i >= 14 and i < 28:
                    self.fiducialCheckBoxes[-1].setGeometry(QtCore.QRect(110, 10 + (i-14)*30, 90, 20))
                else:
                    self.fiducialCheckBoxes[-1].setGeometry(QtCore.QRect(210, 10 + (i-28)*30, 90, 20))

                self.fiducialCheckBoxes[-1].setObjectName("Fiducial" + str(i+1))
                self.fiducialCheckBoxes[-1].setChecked(True)
        except AttributeError:
            print('No ROIs selected')

        self.selectAll = QtWidgets.QPushButton(self.centralwidget)
        self.selectAll.setGeometry(QtCore.QRect(10, 460, 96, 32))
        self.selectAll.setObjectName("selectAll")
        self.selectAll.clicked.connect(self.select_all)
        self.on = True

        BeadAnalyzer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BeadAnalyzer)
        self.statusbar.setObjectName("statusbar")
        BeadAnalyzer.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(BeadAnalyzer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        BeadAnalyzer.setMenuBar(self.menubar)

        self.retranslateUi(BeadAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(BeadAnalyzer)

    def retranslateUi(self, BeadAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        BeadAnalyzer.setWindowTitle(_translate("BeadAnalyzer", "BeadAnalyzer"))
        self.analayzeBeads.setText(_translate("BeadAnalyzer", "Analyze"))
        self.quiteBeadsAnal.setText(_translate("BeadAnalyzer", "Close"))

        for i, f in enumerate(self.fiducialCheckBoxes):
            f.setText(_translate("BeadAnalyzer", "Fiducial " + str(i+1)))

        self.selectAll.setText(_translate("BeadAnalyzer", "Select All"))
        self.applyDriftCorr.setText(_translate("MainWindow", "Apply dr. corr."))

    
    def select_all(self):
        if self.on:
            for f in self.fiducialCheckBoxes:
                f.setChecked(False)
            self.on = False
        else:
            for f in self.fiducialCheckBoxes:
                f.setChecked(True)
            self.on = True
    
    def apply_drift_corr(self):
        self.selected_fiducials = []
        self.ids = []

        n = 1
        for f,ff in zip(self.fiducials, self.fiducialCheckBoxes):
                if ff.isChecked():
                    self.selected_fiducials.append(f)
                    self.ids.append(n)
                n += 1

        methods.dr_corr_2(self.mother_app, self.selected_fiducials, self.particles, self.ids)
    
    def analyze_fiducials(self):
        self.selected_fiducials = []
        self.ids = []

        n = 1
        for f,ff in zip(self.fiducials, self.fiducialCheckBoxes):
                if ff.isChecked():
                    self.selected_fiducials.append(f)
                    self.ids.append(n)
                n += 1

        methods.analyze_fiducials_2(self.mother_app, self.selected_fiducials, self.ids)

