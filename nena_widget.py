from PyQt5 import QtCore, QtWidgets
import nena

class Ui_NeNA(QtWidgets.QMainWindow):
    def setupUi(self, image, fileFormat, NeNAAnalysis):
        NeNAAnalysis.setObjectName("NeNAanalysis")
        NeNAAnalysis.resize(300,403)
        self.image = image
        self.fileFormat = fileFormat

        self.centralwidget = QtWidgets.QWidget(NeNAAnalysis)
        self.centralwidget.setObjectName("centralwidget")

        self.runNeNA = QtWidgets.QPushButton(self.centralwidget)
        self.runNeNA.setGeometry(QtCore.QRect(180,80,90,30))
        self.runNeNA.setObjectName("runNeNA")
        self.runNeNA.clicked.connect(self.run_nena)

        self.setDefaults = QtWidgets.QPushButton(self.centralwidget)
        self.setDefaults.setGeometry(QtCore.QRect(30,80,90,30))
        self.setDefaults.setObjectName("setDefaults")
        self.setDefaults.clicked.connect(self.set_defaults)

        self.lowerBoundLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowerBoundLabel.setGeometry(QtCore.QRect(10,10,80,30))
        self.lowerBoundLabel.setObjectName("lowerBoundLabel")

        self.initialLabel = QtWidgets.QLabel(self.centralwidget)
        self.initialLabel.setGeometry(QtCore.QRect(110,10,80,30))
        self.initialLabel.setObjectName("initialLabel")
        
        self.upperBoundLabel = QtWidgets.QLabel(self.centralwidget)
        self.upperBoundLabel.setGeometry(QtCore.QRect(210,10,80,30))
        self.upperBoundLabel.setObjectName("upperBoundLabel")
        
        self.lowerBoundValue = QtWidgets.QTextEdit(self.centralwidget)
        self.lowerBoundValue.setGeometry(QtCore.QRect(10,40,60,30))
        self.lowerBoundValue.setObjectName("lowerBoundValue")

        self.initialValue = QtWidgets.QTextEdit(self.centralwidget)
        self.initialValue.setGeometry(QtCore.QRect(110,40,60,30))
        self.initialValue.setObjectName("initialValue")
        
        self.upperBoundValue = QtWidgets.QTextEdit(self.centralwidget)
        self.upperBoundValue.setGeometry(QtCore.QRect(210,40,60,30))
        self.upperBoundValue.setObjectName("upperBoundValue")
        
        self.retranslateUi(NeNAAnalysis)
        QtCore.QMetaObject.connectSlotsByName(NeNAAnalysis)

    def retranslateUi(self, NeNAAnalysis):
        _translate = QtCore.QCoreApplication.translate
        NeNAAnalysis.setWindowTitle(_translate("NeNAAnalysis", "NeNA analysis"))
        self.setDefaults.setText(_translate("NeNAanalysis", "Set Defaults"))
        self.runNeNA.setText(_translate("NeNAanalysis", "Compute NeNA"))
        self.lowerBoundLabel.setText(_translate("NeNAAnalysis", "Lower Bound"))
        self.lowerBoundValue.setHtml(_translate("NeNAanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.initialLabel.setText(_translate("NeNAAnalysis", "Initial Value"))
        self.initialValue.setHtml(_translate("NeNAanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">25</p></body></html>"))
        self.upperBoundLabel.setText(_translate("NeNAAnalysis", "Upper Bound"))
        self.upperBoundValue.setHtml(_translate("NeNAanalysis", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.875pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50</p></body></html>"))

    
    def run_nena():
        pass

    def set_defaults():
        pass