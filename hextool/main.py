
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui.hextool_ui import Ui_MainWindow

from intelhex import IntelHex

from qtmodern.styles import dark
from qtmodern.windows import ModernWindow

class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        self.btnChooseHex.clicked.connect(self.choose_hexfile)
        self.btnChooseBin.clicked.connect(self.choose_binfile)
        self.btnConvert.clicked.connect(self.convert_hex2bin)

        self.hexfile = ""
        self.binfile = ""
        self.ih = None

    def choose_hexfile(self):
        self.hexfile = QFileDialog.getOpenFileName(None,"choose hex file",".","*.hex")[0]
        self.editHexFile.setText(self.hexfile)
        self.ih = IntelHex(self.hexfile)

    def choose_binfile(self):
        self.binfile = QFileDialog.getSaveFileName(None,"save bin file",".","*.bin")[0]
        self.editBinFile.setText(self.binfile)

    def convert_hex2bin(self):
        with open('dump.txt','w') as dump:
            self.ih.dump(dump)

        with open('dump.txt','r') as dump:
            self.editDump.appendPlainText(dump.read())

        #write to bin file
        self.ih.tobinfile(self.binfile)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("../monkey.ico"))

    dark(app)

    mwin = MainWindow()

    mwin.setWindowTitle("Hex2Bin file tool")

    win = ModernWindow(mwin)

    win.show()

    sys.exit(app.exec_())