
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import sys,os

import psutil
import win32gui
import win32con
import win32process
from win32ctypes import *
from system_hotkey import SystemHotkey

import qtmodern.styles
import qtmodern.windows

global hide_key
hide_key = ('control','shift','h')

class PreferenceWin(QDialog):
    def __init__(self):
        super(PreferenceWin, self).__init__()

        self.setWindowFlags(Qt.FramelessWindowHint )

        self.mainLayout = QVBoxLayout(self)

        self.keysquenceedit = QKeySequenceEdit(self)
        self.mainLayout.addWidget(self.keysquenceedit)

        self.btnlayout = QHBoxLayout(self)
        self.btnOk = QPushButton(f'OK',self,clicked=self.setKeyOk)
        self.btnCancel= QPushButton(f'Cancel', self,clicked=lambda:self.reject())
        self.btnlayout.addWidget(self.btnOk)
        self.btnlayout.addWidget(self.btnCancel)
        self.mainLayout.addLayout(self.btnlayout)

    def setKeyOk(self):
        global hide_key
        keystr = self.keysquenceedit.keySequence().toString().lower()
        keystr_l = keystr.split('+')
        for i in range(0,len(keystr_l)):
            if keystr_l[i] == 'ctrl':
                keystr = keystr_l[i] = 'control'
        hide_key = tuple(keystr_l)
        print(f'setKeyOk {hide_key}')
        self.accept()

    def setKeyCancel(self):
        print('setKeyCancel')

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setStatusBar(QStatusBar(self))

        self.me_hwnd = 0
        self.me_hide = False

        self.hidekey = SystemHotkey()

        print(f'register key {hide_key}')
        self.hidekey.register(hide_key,callback=lambda x:self.hideme())

        self.menubar = QMenuBar(self)
        self.menuFile = QMenu(f'File', self)
        self.actRefresh = self.menuFile.addAction(QAction(f'Refresh',self,triggered=self.refreshProcess))
        self.actPreference = self.menuFile.addAction(QAction(f'Preference',self,triggered=self.setPreference))
        self.actExit = self.menuFile.addAction(QAction(f'Exit',self,triggered=self.exitApp))
        self.menubar.addMenu(self.menuFile)
        self.setMenuBar(self.menubar)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.header = QHeaderView(Qt.Vertical)
        self.header.setVisible(False)
        self.table.setVerticalHeader(self.header)

        self.addProgressToTable()

        # contex menu
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.contextMenuSlot)

        self.setCentralWidget(self.table)

        self.resize(1000,600)
        self.show()

    def addProgressToTable(self):
        self.table.clear()
        self.table.setRowCount(0)
        for handle,title in self.getAllWindows().items():
            if title != '':
                print(f"window title:{title}")

                rowcnt = self.table.rowCount()
                self.table.insertRow(rowcnt)

                tid, pid = win32process.GetWindowThreadProcessId(handle)
                
                pname = psutil.Process(pid).name()
                cwd = psutil.Process(pid).cwd()

                pid_me = os.getpid()
                print(f"pid me:{pid_me} , {pid}")

                if int(pid_me) == int(pid):
                    self.me_hwnd = handle
                    print(f"get me handle:{self.me_hwnd}")

                self.table.setItem(rowcnt, 0, QTableWidgetItem(f'{handle}'))
                self.table.setItem(rowcnt,1,QTableWidgetItem(title))
                self.table.setItem(rowcnt,2,QTableWidgetItem(f'{pid}'))
                self.table.setItem(rowcnt,3,QTableWidgetItem(cwd))

        self.table.setHorizontalHeaderLabels(['Handle','Title','pid','cwd'])
        self.table.resizeColumnsToContents()

    def contextMenuSlot(self,pos):
        menu = QMenu()
        
        hideact = menu.addAction(f'Hide Me')
        showact = menu.addAction(f'Show Me')
        action = menu.exec_(self.table.mapToGlobal(pos))

        rownum = self.table.itemAt(pos).row()
        handle = self.table.item(rownum,0).text()
        handle = int(handle)

        print(f'get hwnd {handle}')

        if action == hideact:
            win32gui.ShowWindow(handle, win32con.SW_HIDE)
        elif action == showact:
            win32gui.ShowWindow(handle, win32con.SW_SHOW)
            
    def getAllWindows(self):
        hwnd_title = {}

        def get_all_hwnd(hwnd,_):
            if (win32gui.IsWindow(hwnd) and
                win32gui.IsWindowEnabled(hwnd) and
                win32gui.IsWindowVisible(hwnd)):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

        win32gui.EnumWindows(get_all_hwnd, 0)

        return hwnd_title

    def refreshProcess(self):
        print('refreshProcess')

        self.addProgressToTable()


    def setPreference(self):
        print('setPreference')

        self.winset = PreferenceWin()
        self.winset.exec_()

        global hide_key
        if len(hide_key) < 2:
            hide_key = ('control','shift','h')
            print(f'set key to default{hide_key}')

        self.hidekey.register(hide_key,callback=lambda x:self.hideme())

    def hideme(self):
        print('hideme')

        print(f'me hwnd={self.me_hwnd}')
        # fixme: should refresh before hide me
        if self.me_hwnd == 0:
            print('no hwnd of me')
            return
        if self.me_hide == False:
            
            win32gui.ShowWindow(self.me_hwnd, win32con.SW_HIDE)
            self.me_hide = True
        else :
            # fixme: lost focus if only set SW_SHOW
            win32gui.ShowWindow(self.me_hwnd, win32con.SW_SHOW|win32con.SW_MINIMIZE)
            self.me_hide = False

    def exitApp(self):
        print('exitApp')

        sys.exit(0)

if __name__=='__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("../monkey.ico"))

    win = MainWindow()

    win.setWindowTitle(f'HideMe @MakerInChina.cn')

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(win)
    mw.show()

    sys.exit(app.exec_())