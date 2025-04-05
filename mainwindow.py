# This Python file uses the following encoding: utf-8
import sys
import time
import sqlite3 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent
import urllib.request
import LocalDB as LDB
from sys import platform
import CustomWidgets

ip = None
srvrName = None
confPath= "./Resources/conf.db"

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if platform == "linux":
            self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        
        print("INICIANDO")
        db = LDB.ConfigDB(confPath)
        tmp = db.getServer()
        ip = tmp[0]
        srvrName = tmp[1]
    
        IPTAG = self.findChild(QLabel,"lbIP")
        IPTAG.setText(ip)
        print(ip)
        
        GET = urllib.request.urlopen("http://"+ip+"/accesoDB.php?t=u&m=t&c=10").read().decode().strip()
        TESTTAG = self.findChild(QLabel,"lbHTTP")
        print(GET)
        TESTTAG.setText(GET)
        
        
        closeBTN = self.findChild(QPushButton,"btClose")
        closeBTN.clicked.connect(lambda: btClose(closeBTN,self))
        
        lista = db.getServerList()
        tabla = self.findChild(QTableWidget,"tabla")
        tabla.setRowCount(len(lista))
        for i in range(len(lista)):
            cIP = QTableWidgetItem(lista[i][0])
            cNam = QTableWidgetItem(lista[i][1])
            tabla.setItem(i,0,cIP)
            tabla.setItem(i,1,cNam)
        tabla.show()
        
        toggleSCR = self.findChild(QPushButton,"testMaxi")
        toggleSCR.clicked.connect(lambda: toggleFullScreen(self))
        
        self.show()
        
        
        
      
        
        
            #self.showFullScreen()
            

        

def btClose(bt,wndw):
    print("Close")
    bt.setText("CLICK")
    wndw.close()
 
def test():
    print("test")
    
def toggleFullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
