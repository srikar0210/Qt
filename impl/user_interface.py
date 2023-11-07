import sys

from PySide6 import QtCore, QtWidgets
from ui_main_form import Ui_mainwindow
from util import *

class MainPage(QtWidgets.QWidget, Ui_mainwindow):
    switch_window = QtCore.Signal()
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        
        self.ping_button.clicked.connect(self.ping_button_handler)
        self.submit_button.clicked.connect(self.submit_button_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec()    

    def bool_check_credentials(self):
        if len(self.password_line_edit.text()) <= 1:
            self.pop_message(text='Enter valid username and password!!')
            return False
        return True

    def submit_button_handler(self):
        val = self.bool_check_credentials()

        if (val):
            self.switch_window.emit()
        else:
            pass

    def ping_button_handler(self):
        chk = self.bool_check_credentials()
        if (chk):
            val = ping(self.username_line_edit.text())

            if (val):
                self.pop_message(text='Ping success !')
            else:
                self.pop_message(text='Ping Failed !')
        else:
            pass
            
