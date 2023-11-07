# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sftp_transfer_page.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_sftp_form(object):
    def setupUi(self, sftp_form):
        if not sftp_form.objectName():
            sftp_form.setObjectName(u"sftp_form")
        sftp_form.resize(400, 300)
        self.gridLayout = QGridLayout(sftp_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hostname_label = QLabel(sftp_form)
        self.hostname_label.setObjectName(u"hostname_label")

        self.gridLayout.addWidget(self.hostname_label, 0, 0, 1, 1)

        self.hostname_line_edit = QLineEdit(sftp_form)
        self.hostname_line_edit.setObjectName(u"hostname_line_edit")

        self.gridLayout.addWidget(self.hostname_line_edit, 0, 1, 1, 2)

        self.username_label = QLabel(sftp_form)
        self.username_label.setObjectName(u"username_label")

        self.gridLayout.addWidget(self.username_label, 1, 0, 1, 1)

        self.username_line_edit = QLineEdit(sftp_form)
        self.username_line_edit.setObjectName(u"username_line_edit")

        self.gridLayout.addWidget(self.username_line_edit, 1, 1, 1, 2)

        self.port_label = QLabel(sftp_form)
        self.port_label.setObjectName(u"port_label")

        self.gridLayout.addWidget(self.port_label, 2, 0, 1, 1)

        self.port_line_edit = QLineEdit(sftp_form)
        self.port_line_edit.setObjectName(u"port_line_edit")

        self.gridLayout.addWidget(self.port_line_edit, 2, 1, 1, 2)

        self.password_label = QLabel(sftp_form)
        self.password_label.setObjectName(u"password_label")

        self.gridLayout.addWidget(self.password_label, 3, 0, 1, 1)

        self.password_line_edit = QLineEdit(sftp_form)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_line_edit, 3, 1, 1, 2)

        self.browse_label = QLabel(sftp_form)
        self.browse_label.setObjectName(u"browse_label")
        self.browse_label.setText(u"")
        self.browse_label.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.browse_label, 4, 0, 1, 4)

        self.browse_button = QPushButton(sftp_form)
        self.browse_button.setObjectName(u"browse_button")

        self.gridLayout.addWidget(self.browse_button, 4, 4, 1, 1)

        self.connect_button = QPushButton(sftp_form)
        self.connect_button.setObjectName(u"connect_button")

        self.gridLayout.addWidget(self.connect_button, 5, 0, 1, 2)

        self.transfer_button = QPushButton(sftp_form)
        self.transfer_button.setObjectName(u"transfer_button")

        self.gridLayout.addWidget(self.transfer_button, 5, 2, 1, 1)

        self.install_button = QPushButton(sftp_form)
        self.install_button.setObjectName(u"install_button")

        self.gridLayout.addWidget(self.install_button, 5, 3, 1, 2)

        self.logout_button = QPushButton(sftp_form)
        self.logout_button.setObjectName(u"logout_button")

        self.gridLayout.addWidget(self.logout_button, 6, 2, 1, 1)


        self.retranslateUi(sftp_form)

        QMetaObject.connectSlotsByName(sftp_form)
    # setupUi

    def retranslateUi(self, sftp_form):
        sftp_form.setWindowTitle(QCoreApplication.translate("sftp_form", u"DCBAT-BMS-IF", None))
        self.hostname_label.setText(QCoreApplication.translate("sftp_form", u"Hostname", None))
        self.username_label.setText(QCoreApplication.translate("sftp_form", u"Username", None))
        self.port_label.setText(QCoreApplication.translate("sftp_form", u"Port", None))
        self.password_label.setText(QCoreApplication.translate("sftp_form", u"Password", None))
        self.browse_button.setText(QCoreApplication.translate("sftp_form", u"...", None))
        self.connect_button.setText(QCoreApplication.translate("sftp_form", u"Connect", None))
        self.transfer_button.setText(QCoreApplication.translate("sftp_form", u"SFTP Transfer", None))
        self.install_button.setText(QCoreApplication.translate("sftp_form", u"Install", None))
        self.logout_button.setText(QCoreApplication.translate("sftp_form", u"Logout", None))
    # retranslateUi

