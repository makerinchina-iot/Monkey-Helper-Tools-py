
import csv
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

        self.timer_read = QTimer(self)
        self.timer_read.setInterval(100)
        self.timer_read.timeout.connect(self.read_device)

        self.btnSend.clicked.connect(self.write_device)

        self.btnSendMultiple.setCheckable(True)
        self.btnSendMultiple.toggled.connect(self.toggle_send_multiple)
        self.groupBoxSendMultiple.setVisible(False)
        self.btnSendMultiple.setChecked(False)

        self.btnSendAll.clicked.connect(self.send_all_cmd)

        self.btnSend1.clicked.connect(self.send_cmd1)
        self.btnSend2.clicked.connect(self.send_cmd2)
        self.btnSend3.clicked.connect(self.send_cmd3)
        self.btnSend4.clicked.connect(self.send_cmd4)
        self.btnSend5.clicked.connect(self.send_cmd5)
        self.btnSend6.clicked.connect(self.send_cmd6)
        self.btnSend7.clicked.connect(self.send_cmd7)
        self.btnSend8.clicked.connect(self.send_cmd8)
        self.btnSend9.clicked.connect(self.send_cmd9)
        self.btnSend10.clicked.connect(self.send_cmd10)

        self.btnSaveCmd.clicked.connect(self.save_cmd)
        self.btnLoadCmd.clicked.connect(self.load_cmd)

    def toggle_send_multiple(self):
        print("Toggling send multiple")
        if self.btnSendMultiple.isChecked():
            self.groupBoxSendMultiple.setVisible(True)
        else:
            self.groupBoxSendMultiple.setVisible(False)

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

    def send_cmd(self,x):
        sendx = bytes.fromhex(x)
        if len(sendx) != 0:
            if self.dev != None:
                self.dev.write(sendx)

    def send_all_cmd(self):
        if self.checkSend1.isChecked():
            self.send_cmd1()
        if self.checkSend2.isChecked():
            self.send_cmd2()
        if self.checkSend3.isChecked():
            self.send_cmd3()
        if self.checkSend4.isChecked():
            self.send_cmd4()
        if self.checkSend5.isChecked():
            self.send_cmd5()
        if self.checkSend6.isChecked():
            self.send_cmd6()
        if self.checkSend7.isChecked():
            self.send_cmd7()
        if self.checkSend8.isChecked():
            self.send_cmd8()
        if self.checkSend9.isChecked():
            self.send_cmd9()
        if self.checkSend10.isChecked():
            self.send_cmd10()

    def send_cmd1(self):
        self.send_cmd(self.editSend1.text())

    def send_cmd2(self):
        self.send_cmd(self.editSend2.text())

    def send_cmd3(self):
        self.send_cmd(self.editSend3.text())

    def send_cmd4(self):
        self.send_cmd(self.editSend4.text())

    def send_cmd5(self):
        self.send_cmd(self.editSend5.text())

    def send_cmd6(self):
        self.send_cmd(self.editSend6.text())

    def send_cmd7(self):
        self.send_cmd(self.editSend7.text())

    def send_cmd8(self):
        self.send_cmd(self.editSend8.text())
    
    def send_cmd9(self):
        self.send_cmd(self.editSend9.text())

    def send_cmd10(self):
        self.send_cmd(self.editSend10.text())

    def save_cmd(self):
        with open("cmd.csv",'w',newline='') as csv_file:
            wr = csv.writer(csv_file,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
            wr.writerow([f'{self.editSend1.text()}'])
            wr.writerow([f'{self.editSend2.text()}'])
            wr.writerow([f'{self.editSend3.text()}'])
            wr.writerow([f'{self.editSend4.text()}'])
            wr.writerow([f'{self.editSend5.text()}'])
            wr.writerow([f'{self.editSend6.text()}'])
            wr.writerow([f'{self.editSend7.text()}'])
            wr.writerow([f'{self.editSend8.text()}'])
            wr.writerow([f'{self.editSend9.text()}'])
            wr.writerow([f'{self.editSend10.text()}'])

    def load_cmd(self):
        with open("cmd.csv",newline='') as csv_file:
            rd = csv.reader(csv_file,delimiter=' ',quotechar='|',quoting=csv.QUOTE_MINIMAL)
            s = []
            for l in rd:
                s.append(l[0])

            print(s)
            self.editSend1.setText(s[0])
            self.editSend2.setText(s[1])
            self.editSend3.setText(s[2])
            self.editSend4.setText(s[3])
            self.editSend5.setText(s[4])
            self.editSend6.setText(s[5])
            self.editSend7.setText(s[6])
            self.editSend8.setText(s[7])
            self.editSend9.setText(s[8])
            self.editSend10.setText(s[9])
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mwin = MainWindow()
    mwin.setWindowTitle('USBHID Test tool @MakerInChina')

    app.setWindowIcon(QIcon("../monkey.ico"))

    qtmodern.styles.dark(app)
    win = qtmodern.windows.ModernWindow(mwin)

    win.show()

    sys.exit(app.exec_())