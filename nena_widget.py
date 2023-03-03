
from PyQt5 import QtCore, QtWidgets
import numpy as np
from scipy import spatial
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Ui_NeNA(QtWidgets.QMainWindow):
    def setupUi(self, selection, NeNAanalysis, count):
        NeNAanalysis.setObjectName("NeNAanalysis")
        NeNAanalysis.resize(500, 140)
        self.selection = selection
        self.number_of_selections = len(self.selection)

        self.centralwidget = QtWidgets.QWidget(NeNAanalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.prepare_NNs(self.selection[0])

        self.runNeNA = []
        self.setDefaults = []
        self.lowerBoundValue = []
        self.initialValue = []
        self.upperBoundValue = []

        for i in range(self.number_of_selections):
            self.lowerBoundValue.append(QtWidgets.QTextEdit(self.centralwidget))
            self.lowerBoundValue[i].setGeometry(QtCore.QRect(10, i*50 + 40, 60, 30))
            self.lowerBoundValue[i].setObjectName("lowerBoundValue {}".format(i))

            self.initialValue.append(QtWidgets.QTextEdit(self.centralwidget))
            self.initialValue[i].setGeometry(QtCore.QRect(110, i*50 + 40, 60, 30))
            self.initialValue[i].setObjectName("initialValue {}".format(i))

            self.upperBoundValue.append(QtWidgets.QTextEdit(self.centralwidget))
            self.upperBoundValue[i].setGeometry(QtCore.QRect(210, i*50 + 40, 60, 30))
            self.upperBoundValue[i].setObjectName("upperBoundValue {}".format(i))

            self.runNeNA.append(QtWidgets.QPushButton(self.centralwidget))
            self.runNeNA[i].setGeometry(QtCore.QRect(390, i*50 + 40, 90, 30))
            self.runNeNA[i].setObjectName("runNeNA {}".format(i))
            self.runNeNA[i].clicked.connect(self.compute_nena)

            self.setDefaults.append(QtWidgets.QPushButton(self.centralwidget))
            self.setDefaults[i].setGeometry(QtCore.QRect(290, i*50 + 40, 90, 30))
            self.setDefaults[i].setObjectName("setDefaults {}".format(i))
            self.setDefaults[i].clicked.connect(lambda: self.set_defaults(i))

        self.lowerBoundLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowerBoundLabel.setGeometry(QtCore.QRect(10, 10, 80, 30))
        self.lowerBoundLabel.setObjectName("lowerBoundLabel")
        self.initialLabel = QtWidgets.QLabel(self.centralwidget)
        self.initialLabel.setGeometry(QtCore.QRect(110, 10, 80, 30))
        self.initialLabel.setObjectName("initialLabel")
        self.upperBoundLabel = QtWidgets.QLabel(self.centralwidget)
        self.upperBoundLabel.setGeometry(QtCore.QRect(210, 10, 80, 30))
        self.upperBoundLabel.setObjectName("upperBoundLabel")
        NeNAanalysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NeNAanalysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        NeNAanalysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NeNAanalysis)
        self.statusbar.setObjectName("statusbar")
        NeNAanalysis.setStatusBar(self.statusbar)

        self.retranslateUi(NeNAanalysis, count)
        # self.initialize_nena()
        QtCore.QMetaObject.connectSlotsByName(NeNAanalysis)
        # check in methods.calc_NeNA how to procedd further

    def retranslateUi(self, NeNAanalysis, count):
        _translate = QtCore.QCoreApplication.translate
        NeNAanalysis.setWindowTitle(_translate("NeNAanalysis", "NeNA analysis {}".format(count)))
        self.lowerBoundLabel.setText(_translate("NeNAanalysis", "Lower Bound"))
        self.initialLabel.setText(_translate("NeNAanalysis", "Initial Value"))
        self.upperBoundLabel.setText(_translate("NeNAanalysis", "Upper Bound"))

        for i in range(self.number_of_selections):
            self.runNeNA[i].setText(_translate("NeNAanalysis", "Compute NeNA"))
            self.setDefaults[i].setText(_translate("NeNAanalysis", "Set Defaults"))
            self.lowerBoundValue[i].setHtml(_translate("NeNAanalysis", "3"))
            self.initialValue[i].setHtml(_translate("NeNAanalysis", "{}".format(int(self.x[np.argmax(self.y)]))))
            self.upperBoundValue[i].setHtml(_translate("NeNAanalysis", "100"))

    def compute_nena(self):
        # plt.close()
        self.x = np.arange(self.minDist, self.maxDist, self.int, dtype='float')
        self.y = np.histogram(self.NeNADist, bins=int(self.inc), range=(self.minDist, self.maxDist), density=True)[0]
        self.acc, self.acc_err = self.CFit_resultsCorr(self.x, self.y, self.initialValue.toPlainText(), self.lowerBoundValue.toPlainText(), self.upperBoundValue.toPlainText())
        print(np.round(self.acc[0],2))
        self.nenaFit = self.cFunc_2dCorr(self.x, *self.acc)
        plt.style.use('default')
        plt.rcParams['font.family'] = 'Arial'
        plt.figure()
        plt.bar(self.x, self.y, color='gray', edgecolor='black')
        plt.plot(self.x, self.nenaFit, color='red')
        plt.xlabel("Distance (nm)")
        plt.ylabel("Probability")
        plt.title('NeNA: {} nm'.format(np.round(self.acc[0],2)))
        plt.show(block=False)
    
    def set_defaults(self, index):
        print(index)
        self.lowerBoundValue[index].setPlainText("3")
        self.initialValue[index].setPlainText("{}".format(int(self.x[np.argmax(self.y)])))
        self.upperBoundValue[index].setPlainText("100")
    
    def min_dist(self, point, locs):
        d = np.sqrt(np.square(locs[:, 0] - point[0]) + np.square(locs[:, 1] - point[1]))
        return np.min(d)
    
    def compute_area(self, r, y):
        areaF = abs(np.trapz(y, r))
        return areaF

    def cFunc_2dCorr(self, x, dSMLM, xc, w, A2, A1, A3):
        #dSMLM is the value which you wanna get out of it
        y = (x / (2 * dSMLM * dSMLM)) * np.exp((-1) * x * x / (4 * dSMLM * dSMLM)) * A1 + (A2 / (w * np.sqrt(np.pi * 2))) * np.exp(-0.5 * ((x - xc) / w) * ((x - xc) / w)) + A3 * x
        return y
    
    def CFit_resultsCorr(self, x, y, initialValue, lowerBound, upperBound):
        A = self.compute_area(x, y)
        print(A)
        p0 = np.array([initialValue, 15, 100, (A / 2), (A / 2), ((y[98] / 200))])
        bounds = ([lowerBound,0,0,0,0,0],[upperBound,1000,1000,1,1,1])
        popt, pcov = curve_fit(self.cFunc_2dCorr, x, y, p0=p0, bounds=bounds)
        return popt, pcov
    
    def prepare_NNs(self, selection):
        self.selection = selection
        self.selectionArray = np.asarray(self.selection.fiducial)
        self.maxFrame = np.max(self.selectionArray[:,2])
        self.length = np.shape(self.selectionArray)[0]
        self.frames = np.zeros([self.length, 2])
        self.frames[:, 1] = self.selectionArray[:, 2]
        self.tree = spatial.KDTree(self.frames[:, 0:2])
        self.d = np.zeros([self.length, 1])
        self.p = -1
        for i in range(self.length - 1):
            self.o = self.selectionArray[i, 2]
            # j muss angeben,ob nächster Frame existent ist
            self.j = self.selectionArray[i + 1, 2] - self.selectionArray[i, 2]
            if self.selectionArray[i, 2] < self.maxFrame and self.o == self.p:
                self.d[i] = self.min_dist(self.selectionArray[i, 0:3], self.tempLocs)
                self.p = self.o
            elif self.selectionArray[i, 2] < self.maxFrame and self.o > self.p:
                self.tempLocs = self.selectionArray[self.tree.query_ball_point([0, self.o + 1], 0.1), 0:2]
                if np.shape(self.tempLocs)[0] > 0:
                    self.d[i] = self.min_dist(self.selectionArray[i, 0:3], self.tempLocs)
                    self.p = self.o
            elif self.selectionArray[i, 2] == self.maxFrame:
                break
        print('\n')
        self.idx = self.d > 0
        self.NeNADist = self.d[self.idx]
        self.minDist = 0
        self.maxDist = 100
        self.int = 1
        self.inc = (self.maxDist - self.minDist) / self.int

        plt.style.use('default')
        plt.rcParams['font.family'] = 'Arial'
        self.x = np.arange(self.minDist, self.maxDist, self.int, dtype='float')
        self.y = np.histogram(self.NeNADist, bins=int(self.inc), range=(self.minDist, self.maxDist), density=True)[0]
        plt.figure()
        plt.bar(self.x, self.y, color='gray', edgecolor='black')
        plt.xlabel("Distance (nm)")
        plt.ylabel("Probability")
        plt.show(block=False)