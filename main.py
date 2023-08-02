from interface import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
import sys
from ctypes import *
from ctypes.wintypes import *
import time
import pyautogui
import keyboard
from tkinter import *



class Clicker(QtWidgets.QMainWindow):
    def __init__(self):
        super(Clicker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.pushButton.clicked.connect(self.left)#
        self.ui.radioButton.clicked.connect(self.left)
        self.ui.radioButton_2.clicked.connect(self.right)

    def left_right_button(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.radioButton.toggled.connect(self.left)
 
        self.radioButton_2.toggled.connect(self.right)
     
    def left(self, selected):
        text_bind = self.ui.lineEdit.text()
        while True:
            if not keyboard.is_pressed(text_bind):
                pyautogui.click()
                time.sleep(0.1)
            else:
                break
             
    def right(self, selected):
        text_bind = self.ui.lineEdit.text()
        while True:
            if not keyboard.is_pressed(text_bind):
                pyautogui.click(button="right")
                time.sleep(0.1)
            else:
                break
                   
             

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Clicker()
    ui.show()
    app.exec_()
