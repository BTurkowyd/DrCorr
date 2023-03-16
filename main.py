import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from gui import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
app.setStyle('Fusion')
app.setFont(QFont('Arial', 10))
w = AppWindow()
w.show()
sys.exit(app.exec_())