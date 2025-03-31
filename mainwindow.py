# This Python file uses the following encoding: utf-8
import sys
import time
import sqlite3 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel 
import urllib.request

ip = None

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
        print("INICIANDO")
        baseCon = sqlite3.connect("./Resources/AppDB.db")
        cur = baseCon.cursor()
        res = cur.execute("SELECT * FROM SRVR_IP")
        cosa = res.fetchone()
        ip = cosa[0].strip()
        
        IPTAG = self.findChild(QLabel,"lbIP")
        IPTAG.setText(ip)
        print(ip)
        
        GET = urllib.request.urlopen("http://"+ip+"/accesoDB.php?t=u&m=t&c=10").read().decode().strip()
        TESTTAG = self.findChild(QLabel,"lbHTTP")
        print(GET)
        print(type(GET))
        TESTTAG.setText(GET)
        
        
        closeBTN = self.findChild(QPushButton,"btClose")
        closeBTN.clicked.connect(lambda: btClose(closeBTN,self))
        self.show()
        #self.showFullScreen()


def btClose(bt,wndw):
    print("Close")
    bt.setText("CLICK")
    wndw.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
