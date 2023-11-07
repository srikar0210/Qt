# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        if not mainwindow.objectName():
            mainwindow.setObjectName(u"mainwindow")
        mainwindow.resize(517, 506)
        self.centralwidget = QWidget(mainwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.username_frame = QFrame(self.centralwidget)
        self.username_frame.setObjectName(u"username_frame")
        self.username_frame.setMinimumSize(QSize(300, 0))
        self.username_frame.setMaximumSize(QSize(300, 100))
        self.username_frame.setFrameShape(QFrame.StyledPanel)
        self.username_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.username_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.username_label = QLabel(self.username_frame)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setMaximumSize(QSize(200, 200))
        self.username_label.setTextFormat(Qt.AutoText)

        self.verticalLayout_2.addWidget(self.username_label)

        self.username_line_edit = QLineEdit(self.username_frame)
        self.username_line_edit.setObjectName(u"username_line_edit")

        self.verticalLayout_2.addWidget(self.username_line_edit)


        self.verticalLayout.addWidget(self.username_frame)

        self.password_frame = QFrame(self.centralwidget)
        self.password_frame.setObjectName(u"password_frame")
        self.password_frame.setMinimumSize(QSize(300, 0))
        self.password_frame.setMaximumSize(QSize(300, 100))
        self.password_frame.setFrameShape(QFrame.StyledPanel)
        self.password_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.password_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.password_label = QLabel(self.password_frame)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMaximumSize(QSize(100, 50))

        self.verticalLayout_4.addWidget(self.password_label)

        self.password_line_edit = QLineEdit(self.password_frame)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setAutoFillBackground(False)
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.password_line_edit)


        self.verticalLayout.addWidget(self.password_frame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 50))
        self.frame.setMaximumSize(QSize(100, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ping_button = QPushButton(self.frame)
        self.ping_button.setObjectName(u"ping_button")

        self.verticalLayout_5.addWidget(self.ping_button)


        self.verticalLayout.addWidget(self.frame)

        self.submit_button_frame = QFrame(self.centralwidget)
        self.submit_button_frame.setObjectName(u"submit_button_frame")
        self.submit_button_frame.setMinimumSize(QSize(100, 50))
        self.submit_button_frame.setMaximumSize(QSize(100, 50))
        self.submit_button_frame.setFrameShape(QFrame.StyledPanel)
        self.submit_button_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.submit_button_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.submit_button = QPushButton(self.submit_button_frame)
        self.submit_button.setObjectName(u"submit_button")

        self.verticalLayout_3.addWidget(self.submit_button)


        self.verticalLayout.addWidget(self.submit_button_frame)

        self.retranslateUi(mainwindow)

        QMetaObject.connectSlotsByName(mainwindow)
    # setupUi

    def retranslateUi(self, mainwindow):
        mainwindow.setWindowTitle(QCoreApplication.translate("mainwindow", u"MainWindow", None))
        self.username_label.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Username</span></p></body></html>", None))
        self.password_label.setText(QCoreApplication.translate("mainwindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Password</span></p></body></html>", None))
        self.ping_button.setText(QCoreApplication.translate("mainwindow", u"Ping me first!", None))
        self.submit_button.setText(QCoreApplication.translate("mainwindow", u"Submit", None))
    # retranslateUi

