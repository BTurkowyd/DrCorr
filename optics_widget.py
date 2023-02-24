# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optics_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

import optics

class Ui_OPTICSanalysis(QtWidgets.QMainWindow):
    def setupUi(self, image, particles, fileFormat, OPTICSanalysis):
        OPTICSanalysis.setObjectName("OPTICSanalysis")
        OPTICSanalysis.resize(400, 300)
        self.image = image
        self.fileFormat = fileFormat
        self.particles = particles

        self.centralwidget = QtWidgets.QWidget(OPTICSanalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.runOPTICS = QtWidgets.QPushButton(self.centralwidget)
        self.runOPTICS.setGeometry(QtCore.QRect(230, 30, 150, 150))
        self.runOPTICS.setObjectName("runOPTICS")
        self.runOPTICS.clicked.connect(self.run_optics)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(35, 200, 350, 40))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.epsilonLabel = QtWidgets.QLabel(self.centralwidget)
        self.epsilonLabel.setGeometry(QtCore.QRect(20, 10, 150, 40))
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.minPtsField = QtWidgets.QTextEdit(self.centralwidget)
        self.minPtsField.setGeometry(QtCore.QRect(20, 130, 150, 40))
        self.minPtsField.setObjectName("minPtsField")
        self.epsilonField = QtWidgets.QTextEdit(self.centralwidget)
        self.epsilonField.setGeometry(QtCore.QRect(20, 50, 150, 40))
        self.epsilonField.setObjectName("epsilonField")
        self.minPtsLabel = QtWidgets.QLabel(self.centralwidget)
        self.minPtsLabel.setGeometry(QtCore.QRect(20, 90, 150, 40))
        self.minPtsLabel.setObjectName("minPtsLabel")
        OPTICSanalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OPTICSanalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        OPTICSanalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OPTICSanalysis)
        self.statusbar.setObjectName("statusbar")
        OPTICSanalysis.setStatusBar(self.statusbar)

        self.retranslateUi(OPTICSanalysis)
        QtCore.QMetaObject.connectSlotsByName(OPTICSanalysis)

    def retranslateUi(self, OPTICSanalysis):
        _translate = QtCore.QCoreApplication.translate
        OPTICSanalysis.setWindowTitle(_translate("OPTICSanalysis", "OPTICS analysis"))
        self.runOPTICS.setText(_translate("OPTICSanalysis", "Run OPTICS"))
        self.epsilonLabel.setText(_translate("OPTICSanalysis", "Upper limit (nm)"))
        self.minPtsField.setHtml(_translate("OPTICSanalysis", "10"))
        self.epsilonField.setHtml(_translate("OPTICSanalysis", "1000"))
        self.minPtsLabel.setText(_translate("OPTICSanalysis", "Min pts (>1)"))

    def run_optics(self):
        self.clusters = [optics.OPTICS_class(r, self.particles, float(self.minPtsField.toPlainText()), float(self.epsilonField.toPlainText()), self.fileFormat) for r in self.image.selected_regions]

        for i, cluster in enumerate(self.clusters):
            cluster.run_optics()
            cluster.write(i)