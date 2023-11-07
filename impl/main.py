import sys

from PySide6 import QtWidgets
from sftp_transfer_page import SftpPage

class Controller:

    def __init__(self):
        pass

    def show_sftp_transfer_page(self):
        self.sftp_transfer_page = SftpPage()
        self.sftp_transfer_page.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show_sftp_transfer_page()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
