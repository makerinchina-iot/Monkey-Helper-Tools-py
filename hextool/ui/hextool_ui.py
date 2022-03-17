# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerXgIxMf.ui'
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.editHexFile = QLineEdit(self.centralwidget)
        self.editHexFile.setObjectName(u"editHexFile")

        self.horizontalLayout.addWidget(self.editHexFile)

        self.btnChooseHex = QToolButton(self.centralwidget)
        self.btnChooseHex.setObjectName(u"btnChooseHex")

        self.horizontalLayout.addWidget(self.btnChooseHex)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.editBinFile = QLineEdit(self.centralwidget)
        self.editBinFile.setObjectName(u"editBinFile")

        self.horizontalLayout_2.addWidget(self.editBinFile)

        self.btnChooseBin = QToolButton(self.centralwidget)
        self.btnChooseBin.setObjectName(u"btnChooseBin")

        self.horizontalLayout_2.addWidget(self.btnChooseBin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnConvert = QPushButton(self.centralwidget)
        self.btnConvert.setObjectName(u"btnConvert")

        self.horizontalLayout_3.addWidget(self.btnConvert)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.editDump = QPlainTextEdit(self.groupBox)
        self.editDump.setObjectName(u"editDump")
        self.editDump.setReadOnly(True)

        self.verticalLayout.addWidget(self.editDump)


        self.verticalLayout_2.addWidget(self.groupBox)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hex:", None))
        self.btnChooseHex.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bin:", None))
        self.btnChooseBin.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btnConvert.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"dump", None))
    # retranslateUi

