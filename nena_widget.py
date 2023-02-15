
from PyQt5 import QtCore, QtWidgets

import optics

class Ui_NeNA(QtWidgets.QMainWindow):
    def setupUi(self, image, fileFormat, NeNAanalysis):
        NeNAanalysis.setObjectName("NeNAanalysis")
        NeNAanalysis.resize(300, 140)
        self.image = image
        self.fileFormat = fileFormat

        self.centralwidget = QtWidgets.QWidget(NeNAanalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.runNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.runNeNA.setGeometry(QtCore.QRect(180, 80, 90, 30))
        self.runNeNA.setObjectName("runNeNA")
        self.runNeNA.clicked.connect(self.run_nena)
        self.setDefaults = QtWidgets.QPushButton(self.centralwidget)
        self.setDefaults.setGeometry(QtCore.QRect(30, 80, 90, 30))
        self.setDefaults.setObjectName("setDefaults")
        self.setDefaults.clicked.connect(self.set_defaults)
        self.lowerBoundLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowerBoundLabel.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.lowerBoundLabel.setObjectName("lowerBoundLabel")
        self.lowerBoundValue = QtWidgets.QTextEdit(self.centralwidget)
        self.lowerBoundValue.setGeometry(QtCore.QRect(10, 40, 60, 30))
        self.lowerBoundValue.setObjectName("lowerBoundValue")
        self.initialLabel = QtWidgets.QLabel(self.centralwidget)
        self.initialLabel.setGeometry(QtCore.QRect(110, 10, 80, 30))
        self.initialLabel.setObjectName("initialLabel")
        self.initialValue = QtWidgets.QTextEdit(self.centralwidget)
        self.initialValue.setGeometry(QtCore.QRect(110, 40, 60, 30))
        self.initialValue.setObjectName("initialValue")
        self.upperBoundLabel = QtWidgets.QLabel(self.centralwidget)
        self.upperBoundLabel.setGeometry(QtCore.QRect(210, 10, 80, 30))
        self.upperBoundLabel.setObjectName("upperBoundLabel")
        self.upperBoundValue = QtWidgets.QTextEdit(self.centralwidget)
        self.upperBoundValue.setGeometry(QtCore.QRect(210, 40, 60, 30))
        self.upperBoundValue.setObjectName("upperBoundValue")
        NeNAanalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NeNAanalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        NeNAanalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NeNAanalysis)
        self.statusbar.setObjectName("statusbar")
        NeNAanalysis.setStatusBar(self.statusbar)

        self.retranslateUi(NeNAanalysis)
        QtCore.QMetaObject.connectSlotsByName(NeNAanalysis)

    def retranslateUi(self, NeNAanalysis):
        _translate = QtCore.QCoreApplication.translate
        NeNAanalysis.setWindowTitle(_translate("NeNAanalysis", "NeNA analysis"))
        self.runNeNA.setText(_translate("NeNAanalysis", "Compute NeNA"))
        self.setDefaults.setText(_translate("NeNAanalysis", "Reset Values"))
        self.lowerBoundLabel.setText(_translate("NeNAanalysis", "Lower Bound"))
        self.lowerBoundValue.setHtml(_translate("NeNAanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.initialLabel.setText(_translate("NeNAanalysis", "Initial Value"))
        self.initialValue.setHtml(_translate("NeNAanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25</p></body></html>"))
        self.upperBoundLabel.setText(_translate("NeNAanalysis", "Upper Bound"))
        self.upperBoundValue.setHtml(_translate("NeNAanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))

    def run_nena(self):
        pass
        # self.clusters = [optics.OPTICS_class(r, float(self.initialValue.toPlainText()), float(self.lowerBoundValue.toPlainText()), self.fileFormat) for r in self.image.selected_regions]

        # for i, cluster in enumerate(self.clusters):
        #     cluster.run_optics()
        #     cluster.write(i)
    
    def set_defaults(self):
        self.lowerBoundValue.setPlainText("10")
        self.initialValue.setPlainText("10")
        self.upperBoundValue.setPlainText("10")