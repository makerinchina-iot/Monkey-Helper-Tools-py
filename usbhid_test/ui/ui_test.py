# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testakpTgj.ui'
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
        MainWindow.resize(1098, 606)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboPort = QComboBox(self.centralwidget)
        self.comboPort.setObjectName(u"comboPort")

        self.horizontalLayout.addWidget(self.comboPort)

        self.btnConnect = QPushButton(self.centralwidget)
        self.btnConnect.setObjectName(u"btnConnect")

        self.horizontalLayout.addWidget(self.btnConnect)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.editRecv = QPlainTextEdit(self.groupBox)
        self.editRecv.setObjectName(u"editRecv")

        self.verticalLayout.addWidget(self.editRecv)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBoxSendMultiple = QGroupBox(self.centralwidget)
        self.groupBoxSendMultiple.setObjectName(u"groupBoxSendMultiple")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxSendMultiple)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkSend1 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend1.setObjectName(u"checkSend1")

        self.horizontalLayout_4.addWidget(self.checkSend1)

        self.editSend1 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend1.setObjectName(u"editSend1")

        self.horizontalLayout_4.addWidget(self.editSend1)

        self.btnSend1 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend1.setObjectName(u"btnSend1")

        self.horizontalLayout_4.addWidget(self.btnSend1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkSend2 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend2.setObjectName(u"checkSend2")

        self.horizontalLayout_13.addWidget(self.checkSend2)

        self.editSend2 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend2.setObjectName(u"editSend2")

        self.horizontalLayout_13.addWidget(self.editSend2)

        self.btnSend2 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend2.setObjectName(u"btnSend2")

        self.horizontalLayout_13.addWidget(self.btnSend2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkSend3 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend3.setObjectName(u"checkSend3")

        self.horizontalLayout_12.addWidget(self.checkSend3)

        self.editSend3 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend3.setObjectName(u"editSend3")

        self.horizontalLayout_12.addWidget(self.editSend3)

        self.btnSend3 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend3.setObjectName(u"btnSend3")

        self.horizontalLayout_12.addWidget(self.btnSend3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkSend4 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend4.setObjectName(u"checkSend4")

        self.horizontalLayout_11.addWidget(self.checkSend4)

        self.editSend4 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend4.setObjectName(u"editSend4")

        self.horizontalLayout_11.addWidget(self.editSend4)

        self.btnSend4 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend4.setObjectName(u"btnSend4")

        self.horizontalLayout_11.addWidget(self.btnSend4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkSend5 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend5.setObjectName(u"checkSend5")

        self.horizontalLayout_10.addWidget(self.checkSend5)

        self.editSend5 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend5.setObjectName(u"editSend5")

        self.horizontalLayout_10.addWidget(self.editSend5)

        self.btnSend5 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend5.setObjectName(u"btnSend5")

        self.horizontalLayout_10.addWidget(self.btnSend5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkSend6 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend6.setObjectName(u"checkSend6")

        self.horizontalLayout_9.addWidget(self.checkSend6)

        self.editSend6 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend6.setObjectName(u"editSend6")

        self.horizontalLayout_9.addWidget(self.editSend6)

        self.btnSend6 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend6.setObjectName(u"btnSend6")

        self.horizontalLayout_9.addWidget(self.btnSend6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkSend7 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend7.setObjectName(u"checkSend7")

        self.horizontalLayout_8.addWidget(self.checkSend7)

        self.editSend7 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend7.setObjectName(u"editSend7")

        self.horizontalLayout_8.addWidget(self.editSend7)

        self.btnSend7 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend7.setObjectName(u"btnSend7")

        self.horizontalLayout_8.addWidget(self.btnSend7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkSend8 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend8.setObjectName(u"checkSend8")

        self.horizontalLayout_7.addWidget(self.checkSend8)

        self.editSend8 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend8.setObjectName(u"editSend8")

        self.horizontalLayout_7.addWidget(self.editSend8)

        self.btnSend8 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend8.setObjectName(u"btnSend8")

        self.horizontalLayout_7.addWidget(self.btnSend8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkSend9 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend9.setObjectName(u"checkSend9")

        self.horizontalLayout_6.addWidget(self.checkSend9)

        self.editSend9 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend9.setObjectName(u"editSend9")

        self.horizontalLayout_6.addWidget(self.editSend9)

        self.btnSend9 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend9.setObjectName(u"btnSend9")

        self.horizontalLayout_6.addWidget(self.btnSend9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkSend10 = QCheckBox(self.groupBoxSendMultiple)
        self.checkSend10.setObjectName(u"checkSend10")

        self.horizontalLayout_5.addWidget(self.checkSend10)

        self.editSend10 = QLineEdit(self.groupBoxSendMultiple)
        self.editSend10.setObjectName(u"editSend10")

        self.horizontalLayout_5.addWidget(self.editSend10)

        self.btnSend10 = QPushButton(self.groupBoxSendMultiple)
        self.btnSend10.setObjectName(u"btnSend10")

        self.horizontalLayout_5.addWidget(self.btnSend10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btnSaveCmd = QPushButton(self.groupBoxSendMultiple)
        self.btnSaveCmd.setObjectName(u"btnSaveCmd")

        self.horizontalLayout_14.addWidget(self.btnSaveCmd)

        self.btnLoadCmd = QPushButton(self.groupBoxSendMultiple)
        self.btnLoadCmd.setObjectName(u"btnLoadCmd")

        self.horizontalLayout_14.addWidget(self.btnLoadCmd)

        self.btnSendAll = QPushButton(self.groupBoxSendMultiple)
        self.btnSendAll.setObjectName(u"btnSendAll")

        self.horizontalLayout_14.addWidget(self.btnSendAll)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_3.addWidget(self.groupBoxSendMultiple)

        self.horizontalLayout_3.setStretch(0, 7)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.editSend = QLineEdit(self.groupBox_2)
        self.editSend.setObjectName(u"editSend")

        self.horizontalLayout_2.addWidget(self.editSend)

        self.btnSend = QPushButton(self.groupBox_2)
        self.btnSend.setObjectName(u"btnSend")

        self.horizontalLayout_2.addWidget(self.btnSend)

        self.btnSendMultiple = QToolButton(self.groupBox_2)
        self.btnSendMultiple.setObjectName(u"btnSendMultiple")

        self.horizontalLayout_2.addWidget(self.btnSendMultiple)

        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"usbhid port:", None))
        self.btnConnect.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"recv:", None))
        self.groupBoxSendMultiple.setTitle(QCoreApplication.translate("MainWindow", u"send multiple", None))
        self.checkSend1.setText("")
        self.btnSend1.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend2.setText("")
        self.btnSend2.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend3.setText("")
        self.btnSend3.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend4.setText("")
        self.btnSend4.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend5.setText("")
        self.btnSend5.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend6.setText("")
        self.btnSend6.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend7.setText("")
        self.btnSend7.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend8.setText("")
        self.btnSend8.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend9.setText("")
        self.btnSend9.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.checkSend10.setText("")
        self.btnSend10.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.btnSaveCmd.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btnLoadCmd.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.btnSendAll.setText(QCoreApplication.translate("MainWindow", u"Send All Once", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"send:", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.btnSendMultiple.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

