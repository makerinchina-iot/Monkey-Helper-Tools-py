
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtSerialPort import *

from ui.serial_ui import Ui_MainWindow

import qtmodern.styles
import qtmodern.windows

class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        serial_list = QSerialPortInfo.availablePorts()
        for port in serial_list:
            self.comboPort.addItem(port.portName())

        self.comboBaudrate.addItems(['9600','115200'])

        self.serial = QSerialPort()
        self.btnOpen.setText('打开')
        self.btnOpen.clicked.connect(self.open_serial)

        self.btnSend.clicked.connect(self.send_data)
        self.serial.readyRead.connect(self.read_data)

        self.btnClear.clicked.connect(self.editRecv.clear)

    def open_serial(self):
        self.serial.setPortName(self.comboPort.currentText())

        if self.btnOpen.text() == '打开':
            self.serial.open(QIODevice.ReadWrite)

            self.serial.setBaudRate(int(self.comboBaudrate.currentText()))
            self.btnOpen.setText('关闭')
        else:
            self.serial.close()
            self.btnOpen.setText('打开')

    def send_data(self):
        if self.serial.isOpen():
            str = self.editSend.text()+"\r\n"
            ba = QTextCodec.codecForLocale().fromUnicode(str)
            self.serial.write(ba)

    def read_data(self):
        ba = self.serial.readAll()
        str = QTextCodec.codecForLocale().toUnicode(ba.data())
        self.editRecv.appendPlainText(str)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    qtmodern.styles.dark(app)

    app.setWindowIcon(QIcon("../monkey.ico"))


    mwin = MainWindow()
    
    win = qtmodern.windows.ModernWindow(mwin)

    win.show()

    sys.exit(app.exec_())