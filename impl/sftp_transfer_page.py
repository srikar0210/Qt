import sys
import time

from PySide6 import QtCore, QtWidgets
from ui_sftp_transfer_page import Ui_sftp_form
from  util import *
from ssh_client import *

class SftpPage(QtWidgets.QWidget, Ui_sftp_form, SSHClient):
    switch_window = QtCore.Signal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        SSHClient.__init__(self)
        self.setupUi(self)

        self.browse_button.clicked.connect(self.browse_button_handler)
        self.connect_button.clicked.connect(self.connect_button_handler)
        self.transfer_button.clicked.connect(self.transfer_button_handler)
        self.install_button.clicked.connect(self.install_button_handler)
        self.logout_button.clicked.connect(self.logout_button_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec()
    
    def browse_button_handler(self):
        self.open_dialog_box()

    def connect_button_handler(self):
        if (len(self.hostname_line_edit.text()) < 0) or (len(self.username_line_edit.text()) < 0) or (len(self.port_line_edit.text()) < 0) or (len(self.password_line_edit.text()) < 0):
            self.pop_message(text="Enter appropriate credentials!!")
        else:
            val = ping(self.hostname_line_edit.text())
            if (val):
                self.pop_message(text="Ping Success!!")
            else:
                self.pop_message(text="Ping Failed!")         
        self.ssh_connect(host=self.hostname_line_edit.text(), user=self.username_line_edit.text(), password=self.password_line_edit.text())
        cmd = "sudo pip install pymodbus future"
        self.ssh_execute(cmd)
                 
    def transfer_button_handler(self):
        self.sftp_client = self.client.open_sftp()
        dir_list = self.sftp_client.listdir('/home/pi')
        if 'download' in dir_list:
            self.sftp_client.chdir('/home/pi/download')
        else:
            self.sftp_client.chdir('/home/pi')
            self.sftp_client.mkdir('download')
            self.sftp_client.chdir('/home/pi/download')
        self.sftp_client.put(self.path, '/home/pi/download/N470_pi_script.zip')
        dir_list = self.sftp_client.listdir('/home/pi/download')
        if 'N470_pi_script.zip' in dir_list:
            self.pop_message("Zip File Transferred!")
        else:
            self.pop_message("Unsuccessfull transfer!")
        self.sftp_client.close()

    def install_button_handler(self):
        self.client.exec_command("cd /home/pi/download ; unzip N470_pi_script.zip")
        time.sleep(1)
        self.client.exec_command("chmod 777 -R /home/pi/download/N470_pi_script/")
        time.sleep(1)
        stdin, stdout, stderr = self.client.exec_command("cd /home/pi/download/N470_pi_script/; ./install")
        print(stderr.read().decode())
        time.sleep(10)
        stdin, stdout, stderr = self.ssh_execute("sudo systemctl status N470_pi_script.service")
        print(stdout.channel.recv_exit_status())
        if (stdout.channel.recv_exit_status() == 0):
            self.pop_message("Service ACTIVE!! \n Logout and close the window")
        elif (stdout.channel.recv_exit_status() != 0):
            self.pop_message("Service is NOT ACTIVE!! \n Ask for help")
        else:
            self.pop_message("Service Status is UNKNOWN!\n Ask for help")

    def logout_button_handler(self):
        self.ssh_disconnect()
        self.pop_message("Logged Out!\n Window can be closed")
    
    def open_dialog_box(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.browse_label.setText(self.path)

