from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
from MainWindow import Ui_MainWindow
from ISIMM import Institut
class MainWindow:
    def __init__(self):
        self.ISIMM=Institut()
        self.window=QMainWindow()
        self.ui=Ui_MainWindow(self.ISIMM)
        self.ui.setupUi(self.window)
        self.window.show()



app=QtWidgets.QApplication(sys.argv)
window=MainWindow()

app.exec_()