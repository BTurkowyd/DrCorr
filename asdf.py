# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bead_analyzer_skeleton.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.analayzeBeads = QtWidgets.QPushButton(self.centralwidget)
        self.analayzeBeads.setGeometry(QtCore.QRect(10, 520, 96, 32))
        self.analayzeBeads.setObjectName("analayzeBeads")
        self.quiteBeadsAnal = QtWidgets.QPushButton(self.centralwidget)
        self.quiteBeadsAnal.setGeometry(QtCore.QRect(290, 520, 96, 32))
        self.quiteBeadsAnal.setObjectName("quiteBeadsAnal")
        self.listOfFiducials = QtWidgets.QFrame(self.centralwidget)
        self.listOfFiducials.setGeometry(QtCore.QRect(10, 10, 381, 441))
        self.listOfFiducials.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listOfFiducials.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listOfFiducials.setObjectName("listOfFiducials")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.listOfFiducials)
        self.verticalScrollBar.setGeometry(QtCore.QRect(360, 0, 16, 441))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.checkBox = QtWidgets.QCheckBox(self.listOfFiducials)
        self.checkBox.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.checkBox.setObjectName("checkBox")
        self.selectAll = QtWidgets.QPushButton(self.centralwidget)
        self.selectAll.setGeometry(QtCore.QRect(10, 460, 96, 32))
        self.selectAll.setObjectName("selectAll")
        self.applyDriftCorr = QtWidgets.QPushButton(self.centralwidget)
        self.applyDriftCorr.setGeometry(QtCore.QRect(120, 520, 96, 32))
        self.applyDriftCorr.setObjectName("applyDriftCorr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.analayzeBeads.setText(_translate("MainWindow", "Analyze"))
        self.quiteBeadsAnal.setText(_translate("MainWindow", "Quit"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.selectAll.setText(_translate("MainWindow", "Select All"))
        self.applyDriftCorr.setText(_translate("MainWindow", "Apply dr. corr."))

