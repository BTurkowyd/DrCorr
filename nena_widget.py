
from PyQt5 import QtCore, QtWidgets
import numpy as np
from scipy import spatial
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class Ui_NeNA(QtWidgets.QMainWindow):
    def setupUi(self, selection, NeNAanalysis, count):
        NeNAanalysis.setObjectName("NeNAanalysis")
        self.selections = selection
        self.number_of_selections = len(self.selections)
        NeNAanalysis.resize(500, 90 + 50*self.number_of_selections)
        self.centralwidget = QtWidgets.QWidget(NeNAanalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.minDist = 0
        self.maxDist = 100
        self.int = 1
        self.inc= (self.maxDist - self.minDist) / self.int

        self.runNeNA = [None] * self.number_of_selections
        self.setDefaults = [None] * self.number_of_selections
        self.lowerBoundValue = [None] * self.number_of_selections
        self.initialValue = [None] * self.number_of_selections
        self.upperBoundValue = [None] * self.number_of_selections

        self.selectionArray = [None] * self.number_of_selections
        self.maxFrame = [None] * self.number_of_selections
        self.length = [None] * self.number_of_selections
        self.frames = [None] * self.number_of_selections
        self.tree = [None] * self.number_of_selections
        self.idx = [None] * self.number_of_selections
        self.NeNADist = [None] * self.number_of_selections
        self.x = [None] * self.number_of_selections
        self.y = [None] * self.number_of_selections
        self.acc = [None] * self.number_of_selections
        self.acc_err = [None] * self.number_of_selections
        self.nenaFit = [None] * self.number_of_selections

        self.prepare_NNs()

        for i in range(self.number_of_selections):
            self.lowerBoundValue[i] =QtWidgets.QTextEdit(self.centralwidget)
            self.lowerBoundValue[i].setGeometry(QtCore.QRect(10, i*50 + 40, 60, 30))
            self.lowerBoundValue[i].setObjectName("lowerBoundValue {}".format(i))

            self.initialValue[i] =QtWidgets.QTextEdit(self.centralwidget)
            self.initialValue[i].setGeometry(QtCore.QRect(110, i*50 + 40, 60, 30))
            self.initialValue[i].setObjectName("initialValue {}".format(i))

            self.upperBoundValue[i] =QtWidgets.QTextEdit(self.centralwidget)
            self.upperBoundValue[i].setGeometry(QtCore.QRect(210, i*50 + 40, 60, 30))
            self.upperBoundValue[i].setObjectName("upperBoundValue {}".format(i))

            self.runNeNA[i] =QtWidgets.QPushButton(self.centralwidget)
            self.runNeNA[i].setGeometry(QtCore.QRect(390, i*50 + 40, 90, 30))
            self.runNeNA[i].setObjectName("runNeNA {}".format(i))
            self.runNeNA[i].clicked.connect(lambda state, i=i: self.compute_nena(i))

            self.setDefaults[i] =QtWidgets.QPushButton(self.centralwidget)
            self.setDefaults[i].setGeometry(QtCore.QRect(290, i*50 + 40, 90, 30))
            self.setDefaults[i].setObjectName("setDefaults {}".format(i))
            self.setDefaults[i].clicked.connect(lambda state, i=i: self.set_defaults(i))

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
            self.setDefaults[i].setText(_translate("NeNAanalysis", "Set Defaults {}".format(i+1)))
            self.lowerBoundValue[i].setHtml(_translate("NeNAanalysis", "3"))
            self.initialValue[i].setHtml(_translate("NeNAanalysis", "{}".format(int(self.x[i][np.argmax(self.y[i])]))))
            self.upperBoundValue[i].setHtml(_translate("NeNAanalysis", "100"))

    def compute_nena(self, index):
        # plt.close()
        # self.x[index] = np.arange(self.minDist, self.maxDist, self.int, dtype='float')
        # self.y[index] = np.histogram(self.NeNADist[index], bins=int(self.inc), range=(self.minDist, self.maxDist), density=True)[0]
        self.accuracy, self.accuracy_err = self.CFit_resultsCorr(self.x[index], self.y[index], self.initialValue[index].toPlainText(), self.lowerBoundValue[index].toPlainText(), self.upperBoundValue[index].toPlainText())
        self.acc[index] = self.accuracy
        self.acc_err[index] = self.accuracy_err
        print(np.round(self.acc[index][0],2))
        self.nenaFit[index] = self.cFunc_2dCorr(self.x[index], *self.acc[index])
        plt.style.use('default')
        plt.rcParams['font.family'] = 'Arial'
        plt.figure()
        plt.bar(self.x[index], self.y[index], color='gray', edgecolor='black')
        plt.plot(self.x[index], self.nenaFit[index], color='red')
        plt.xlabel("Distance (nm)")
        plt.ylabel("Probability")
        plt.title('Selection #{}: NeNA {} nm'.format(index+1, np.round(self.acc[index][0],2)))
        plt.show(block=False)
    
    def set_defaults(self, index):
        self.lowerBoundValue[index].setPlainText("3")
        self.initialValue[index].setPlainText("{}".format(int(self.x[index][np.argmax(self.y[index])])))
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
        p0 = np.array([initialValue, 15, 100, (A / 2), (A / 2), ((y[98] / 200))])
        bounds = ([lowerBound,0,0,0,0,0],[upperBound,1000,1000,1,1,1])
        popt, pcov = curve_fit(self.cFunc_2dCorr, x, y, p0=p0, bounds=bounds)
        return popt, pcov
    
    def prepare_NNs(self):
        for k in range(self.number_of_selections):
            self.selectionArray[k] = np.asarray(self.selections[k].fiducial)
            self.maxFrame[k] = np.max(self.selectionArray[k][:,2])
            self.length[k] = np.shape(self.selectionArray[k])[0]
            self.frames[k] = np.zeros([self.length[k], 2])
            self.frames[k][:, 1] = self.selectionArray[k][:, 2]
            self.tree[k] = spatial.KDTree(self.frames[k][:, 0:2])
            self.d = np.zeros([self.length[k], 1])
            self.p = -1
            for i in range(self.length[k] - 1):
                self.o = self.selectionArray[k][i, 2]
                # j muss angeben,ob nächster Frame existent ist
                self.j = self.selectionArray[k][i + 1, 2] - self.selectionArray[k][i, 2]
                if self.selectionArray[k][i, 2] < self.maxFrame[k] and self.o == self.p:
                    self.d[i] = self.min_dist(self.selectionArray[k][i, 0:3], self.tempLocs)
                    self.p = self.o
                elif self.selectionArray[k][i, 2] < self.maxFrame[k] and self.o > self.p:
                    self.tempLocs = self.selectionArray[k][self.tree[k].query_ball_point([0, self.o + 1], 0.1), 0:2]
                    if np.shape(self.tempLocs)[0] > 0:
                        self.d[i] = self.min_dist(self.selectionArray[k][i, 0:3], self.tempLocs)
                        self.p = self.o
                elif self.selectionArray[k][i, 2] == self.maxFrame[k]:
                    break
            self.idx[k] = self.d > 0
            self.NeNADist[k] = self.d[self.idx[k]]

            # plt.style.use('default')
            # plt.rcParams['font.family'] = 'Arial'
            self.x[k] = np.arange(self.minDist, self.maxDist, self.int, dtype='float')
            self.y[k] = np.histogram(self.NeNADist[k], bins=int(self.inc), range=(self.minDist, self.maxDist), density=True)[0]
            # plt.figure()
            # plt.bar(self.x[k], self.y[k], color='gray', edgecolor='black')
            # plt.xlabel("Distance (nm)")
            # plt.ylabel("Probability")
            # plt.title("Fiducial #{}".format(k+1))
            # plt.show(block=False)