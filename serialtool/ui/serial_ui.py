# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYRIXvo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.comboPort = QComboBox(self.centralwidget)
        self.comboPort.setObjectName(u"comboPort")

        self.horizontalLayout_3.addWidget(self.comboPort)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBaudrate = QComboBox(self.centralwidget)
        self.comboBaudrate.setObjectName(u"comboBaudrate")

        self.horizontalLayout_3.addWidget(self.comboBaudrate)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")

        self.horizontalLayout_3.addWidget(self.btnClear)

        self.btnOpen = QPushButton(self.centralwidget)
        self.btnOpen.setObjectName(u"btnOpen")

        self.horizontalLayout_3.addWidget(self.btnOpen)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.editRecv = QPlainTextEdit(self.groupBox)
        self.editRecv.setObjectName(u"editRecv")
        self.editRecv.setReadOnly(True)

        self.verticalLayout.addWidget(self.editRecv)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editSend = QLineEdit(self.groupBox_2)
        self.editSend.setObjectName(u"editSend")

        self.horizontalLayout.addWidget(self.editSend)

        self.btnSend = QPushButton(self.groupBox_2)
        self.btnSend.setObjectName(u"btnSend")

        self.horizontalLayout.addWidget(self.btnSend)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\uff1a", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.btnOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\uff1a", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
    # retranslateUi

