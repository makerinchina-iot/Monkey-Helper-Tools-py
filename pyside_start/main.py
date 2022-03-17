
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui.main_ui import Ui_MainWindow

import qtmodern.styles
import qtmodern.windows

class MainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_pushbutton)

    def on_pushbutton(self):
        msgbox = QMessageBox.information(self,"msg","you login succeed!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("../monkey.ico"))

    qtmodern.styles.dark(app)

    mwin = MainWindow()

    mwin.setWindowTitle("pyside start example")
    
    win = qtmodern.windows.ModernWindow(mwin)

    win.show()

    sys.exit(app.exec_())
