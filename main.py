from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ctypes import *
from ctypes.wintypes import *
import time
import pyautogui
import keyboard


class Clicker(QtWidgets.QMainWindow):
    def __init__(self):
        super(Clicker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
    
    def start(self):
        self.ui.pushButton.setEnabled(False)
        while True:
            try:
                pyautogui.click()
                print(3)
                time.sleep(3)
            except KeyboardInterrupt:
                break
            


        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Clicker()
    ui.show()
    app.exec_()
