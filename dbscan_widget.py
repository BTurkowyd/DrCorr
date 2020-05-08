# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbscan_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from numpy import shape

import dbscan
import methods
import rois

class Ui_DBSCANanalysis(QtWidgets.QMainWindow):
    def setupUi(self, image, fileFormat, DBSCANanalysis):
        DBSCANanalysis.setObjectName("DBSCANanalysis")
        DBSCANanalysis.resize(400, 300)

        self.image = image
        self.fileFormat = fileFormat
        self.dbscanWidget = QtWidgets.QWidget(DBSCANanalysis)
        self.dbscanWidget.setObjectName("dbscanWidget")
        self.progressBar = QtWidgets.QProgressBar(self.dbscanWidget)
        self.progressBar.setGeometry(QtCore.QRect(25, 200, 350, 40))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.minPtsField = QtWidgets.QTextEdit(self.dbscanWidget)
        self.minPtsField.setGeometry(QtCore.QRect(20, 130, 150, 40))
        self.minPtsField.setObjectName("minPtsField")
        self.minPtsLabel = QtWidgets.QLabel(self.dbscanWidget)
        self.minPtsLabel.setGeometry(QtCore.QRect(20, 90, 150, 40))
        self.minPtsLabel.setObjectName("minPtsLabel")
        self.epsilonField = QtWidgets.QTextEdit(self.dbscanWidget)
        self.epsilonField.setGeometry(QtCore.QRect(20, 50, 150, 40))
        self.epsilonField.setObjectName("epsilonField")
        self.epsilonLabel = QtWidgets.QLabel(self.dbscanWidget)
        self.epsilonLabel.setGeometry(QtCore.QRect(20, 10, 150, 40))
        self.epsilonLabel.setObjectName("epsilonLabel")
        self.runDBSCAN = QtWidgets.QPushButton(self.dbscanWidget)
        self.runDBSCAN.setGeometry(QtCore.QRect(220, 30, 150, 150))
        self.runDBSCAN.setObjectName("runDBSCAN")
        self.runDBSCAN.clicked.connect(self.run_dbscan)
        DBSCANanalysis.setCentralWidget(self.dbscanWidget)
        self.menubar = QtWidgets.QMenuBar(DBSCANanalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        DBSCANanalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DBSCANanalysis)
        self.statusbar.setObjectName("statusbar")
        DBSCANanalysis.setStatusBar(self.statusbar)

        self.retranslateUi(DBSCANanalysis)
        QtCore.QMetaObject.connectSlotsByName(DBSCANanalysis)

    def retranslateUi(self, DBSCANanalysis):
        _translate = QtCore.QCoreApplication.translate
        DBSCANanalysis.setWindowTitle(_translate("DBSCANanalysis", "DBSCAN analysis"))
        self.minPtsField.setHtml(_translate("DBSCANanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2</p></body></html>"))
        self.minPtsLabel.setText(_translate("DBSCANanalysis", "MinPts (min. 2)"))
        self.epsilonField.setHtml(_translate("DBSCANanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50</p></body></html>"))
        self.epsilonLabel.setText(_translate("DBSCANanalysis", "Epsilon (radius) (nm)"))
        self.runDBSCAN.setText(_translate("DBSCANanalysis", "Run DBSCAN"))
    
    def run_dbscan(self):
        self.clusters = [dbscan.DBSCAN_class(r, float(self.epsilonField.toPlainText()), float(self.minPtsField.toPlainText()), self.fileFormat) for r in self.image.selected_regions]

        for i, cluster in enumerate(self.clusters):
            cluster.run_dbscan()
            cluster.write(i)

