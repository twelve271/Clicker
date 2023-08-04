from interface import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QValidator
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
import pyautogui
import keyboard

class Clicker(QtWidgets.QMainWindow):
    def __init__(self):
        super(Clicker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.start)
        self.initUI()
        self.ui.lineEdit.setMaxLength(1)
        self.ui.interval_text.setMaxLength(4)
        validator = QDoubleValidator(0.0, 5.0, 2)
        self.ui.interval_text.setValidator(validator)


    def initUI(self):
        self.setWindowTitle('AutoClicker')
        self.setWindowIcon(QIcon('iconnn.png'))

    def start(self):
        text_bind = self.ui.lineEdit.text()
        inter_text = self.ui.interval_text.text()
        inter_text = inter_text.replace(",", ".")
        inter_text2 = float(inter_text)
        if not text_bind:
            self.ui.warning_key.setText("PROVIDE A KEY IN KEY FIELD!")
            self.ui.warning_key.setStyleSheet("color: red")
        elif not self.ui.left_click.isChecked() and not self.ui.right_click.isChecked():
            self.ui.warning_key.setText("CHOOSE LMB OR RMB!")
            self.ui.warning_key.setStyleSheet("color: red")
        elif inter_text2 == 0.00 or 0:
            self.ui.warning_key.setText("SPECIFY THE CLICK SPEED")
            self.ui.warning_key.setStyleSheet("color: red")
        elif self.ui.left_click.isChecked():
            self.ui.warning_key.clear()
            self.left(text_bind,inter_text2)
        elif self.ui.right_click.isChecked():
            self.ui.warning_key.clear()
            self.right(text_bind,inter_text2)

    def left(self,text_bind,inter_text2):
        while True:
            if not keyboard.is_pressed(text_bind):
                pyautogui.click()
                time.sleep(inter_text2)
            else:
                break
             
    def right(self,text_bind,inter_text2):
        while True:
            if not keyboard.is_pressed(text_bind):
                pyautogui.click(button="right")
                time.sleep(inter_text2)
            else:
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Clicker()
    ui.show()
    app.exec_()
