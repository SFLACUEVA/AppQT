# This Python file uses the following encoding: utf-8
import sys
import time
import sqlite3 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout
import urllib.request

from sys import platform
from setup import StartServerIn
from PySide6 import QtCore
from ui_form import Ui_MainWindow
from buttons import *
from clases import *

ip = None
srvrName = None
confPath= ".\\Resources\\conf.db"
charge = carga()
cloud = cloudComm() 



# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("INICIANDO")
        
        db = ConfigDB(confPath)
        tmp = db.getServer()
        ip = tmp[0]
        srvrName = tmp[1]

        IPTAG = self.findChild(QLabel,"lbIP")
        IPTAG.setText(ip)
        print(ip)

        #GET = urllib.request.urlopen("http://"+ip+"/accesoDB.php?t=u&m=t&c=10").read().decode().strip()
        TESTTAG = self.findChild(QLabel,"lbHTTP")
        GET = "OFFLINE"
        print(GET)
        TESTTAG.setText(GET)
        
        grafico = StartServerIn(self)
        x = [0,1,2,3,4,5]
        tension = [9,11,13,14,15,15 ]   # Voltaje
        corriente = [3,3,3,3,2,1]  # Corriente
        grafico.plot(tension,corriente,x)
        
        
        closeBTN = self.findChild(QPushButton,"btClose")
        closeBTN.clicked.connect(lambda: btClose(closeBTN,self,charge))
        
        chargeBTN = self.findChild(QPushButton,"btCharge")
        chargeBTN.clicked.connect(lambda: btCharge(chargeBTN,self,charge,grafico))
        
        lista = db.getServerList()
        tabla = self.findChild(QTableWidget,"tabla")
        
        tabla.setRowCount(len(lista))
        for i in range(len(lista)):
            cIP = QTableWidgetItem(lista[i][0])
            cNam = QTableWidgetItem(lista[i][1])
            #fila.setText("1")
            tabla.setItem(i,0,cIP)
            tabla.setItem(i,1,cNam)
            
        
        
       
        
        self.show()
        if platform == "linux":
            self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
            self.showFullScreen()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    
    sys.exit(app.exec())
