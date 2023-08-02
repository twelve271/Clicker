from interface import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
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

    def initUI(self):
        self.setWindowTitle('AutoClicker')
        self.setWindowIcon(QIcon('iconnn.png'))
        
    def start(self):
        text_bind = self.ui.lineEdit.text()
        if not text_bind:
            self.ui.warning_key.setText("PROVIDE A KEY IN KEY FIELD!")
            self.ui.warning_key.setStyleSheet("color: red")
        elif not self.ui.left_click.isChecked() and not self.ui.right_click.isChecked():
            self.ui.warning_key.setText("CHOOSE LMB OR RMB!")
            self.ui.warning_key.setStyleSheet("color: red")
        elif self.ui.left_click.isChecked():
            self.ui.warning_key.clear()
            self.left(text_bind)
            print(3)
        elif self.ui.right_click.isChecked():
            self.ui.warning_key.clear()
            self.right(text_bind)

    def left(self,text_bind):
        while True:
            if not keyboard.is_pressed(text_bind):
                pyautogui.click()
                time.sleep(0.1)
            else:
                break
             
    def right(self,text_bind):
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
