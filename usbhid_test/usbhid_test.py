
import sys
import hid

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui.ui_test import Ui_MainWindow

import qtmodern.styles
import qtmodern.windows

hid_packet_size = 64

class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        #scan usbhid device
        devices = hid.enumerate()

        self.dev = hid.device()

        index = 0
        for devinfo in devices:
            product_str = devinfo['product_string']
            manu_str = devinfo['manufacturer_string']
            vid = devinfo['vendor_id']
            pid = devinfo['product_id']

            name_str = product_str + f' by {manu_str}'
            print(name_str)
            if product_str != '':
                self.comboPort.addItem(name_str)    
                self.comboPort.setItemData(index,pid,Qt.UserRole+1)
                self.comboPort.setItemData(index,vid,Qt.UserRole+2)    
                index += 1

        self.editSend.setPlaceholderText('send hex str')
        self.btnConnect.setText('connect')
        self.btnConnect.clicked.connect(self.connect_device)

        self.timer_read = QTimer()
        self.timer_read.setInterval(100)
        self.timer_read.timeout.connect(self.read_device)

        self.btnSend.clicked.connect(self.write_device)

    def connect_device(self):
        pid = self.comboPort.itemData(self.comboPort.currentIndex(),Qt.UserRole+1)
        vid = self.comboPort.itemData(self.comboPort.currentIndex(),Qt.UserRole+2)
        product_str = self.comboPort.currentText()

        print(f'current device:{product_str},pid={pid:#0x}, vid={vid:#0x}')

        if self.btnConnect.text() == 'connect':
            self.btnConnect.setText('disconnect')

            try:
                print('open the device')
                self.dev.open(vid,pid)
            except IOError as exc:
                print((f'open usb device failed:{exc}'))
                self.editRecv.appendPlainText(f'open usb device failed:{exc}')

            self.editRecv.clear()
            self.editRecv.appendPlainText(f'open device: {product_str}')

            self.dev.set_nonblocking(True)
            print('now read the process.')
            self.timer_read.start()
        else:
            self.timer_read.stop()
            self.dev.close()
            self.btnConnect.setText('connect')
        
    def read_device(self):
        # print('read device')

        if self.dev != None:
            recv_buff = self.dev.read(hid_packet_size)

        if len(recv_buff) != 0:
            recv_str = ' '.join([f'{i:#02x}' for i in bytes(recv_buff).rstrip(b'\x00')])
            print(recv_str)
            self.editRecv.appendPlainText(recv_str)

    def write_device(self):
        send_buff = self.editSend.text()

        hex_str = bytes.fromhex(send_buff)

        if len(hex_str) != 0:
            if self.dev != None:
                print(f'send data to device:{hex_str}')
                self.dev.write(hex_str)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mwin = MainWindow()

    qtmodern.styles.dark(app)
    qtmodern.windows.ModernWindow(mwin).show()

    sys.exit(app.exec_())