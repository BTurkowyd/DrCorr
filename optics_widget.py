# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optics_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OPTICSanalysis(QtWidgets.QMainWindow):
    def setupUi(self, OPTICSanalysis):
        OPTICSanalysis.setObjectName("OPTICSanalysis")
        OPTICSanalysis.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(OPTICSanalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.runDBSCAN = QtWidgets.QPushButton(self.centralwidget)
        self.runDBSCAN.setGeometry(QtCore.QRect(230, 30, 150, 150))
        self.runDBSCAN.setObjectName("runDBSCAN")
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
        self.runDBSCAN.setText(_translate("OPTICSanalysis", "Run OPTICS"))
        self.epsilonLabel.setText(_translate("OPTICSanalysis", "Upper limit (nm)"))
        self.minPtsField.setHtml(_translate("OPTICSanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.epsilonField.setHtml(_translate("OPTICSanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1000</p></body></html>"))
        self.minPtsLabel.setText(_translate("OPTICSanalysis", "Upper limit (nm)"))

