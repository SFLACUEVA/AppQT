#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout
import urllib.request
from sys import platform
from setup import StartServerIn
from PySide6 import QtCore
from ui_form import Ui_MainWindow
from buttons import *
from clases import *
import pathlib
from PySide6.QtCore import Slot




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
        
        confPath= str(pathlib.Path(__file__).parent.resolve() / "Resources" / "conf.db")
        measPath = str(pathlib.Path(__file__).parent.resolve() / "Resources" / "measures.db")
        
        self.charge = clases.carga()
        self.charge.cloud = cloudComm()
        discharge = clases.descarga()
        self.charge.señal.finished.connect(self.on_charge_finished)
        self.charge.cloud.señal.offline.connect(self.uncheck)
        
        graficoS,graficoC,graficoD = StartServerIn(self)
        
        closeBTN = self.findChild(QPushButton,"btClose")
        closeBTN.clicked.connect(lambda: btClose(closeBTN,self,self.charge,discharge))
        
        chargeBTN = self.findChild(QPushButton,"btCharge")
        chargeBTN.clicked.connect(lambda: btCharge(chargeBTN,self,self.charge,graficoC,self.charge.cloud))
        
        saveBTN = self.findChild(QPushButton,"batSave")
        saveBTN.clicked.connect(lambda: batSave(self,confPath))
        
        batRefreshBTN = self.findChild(QPushButton,"batRefresh")
        batRefreshBTN.clicked.connect(lambda: batRefresh(self,confPath))
        
        batLoadBTN = self.findChild(QPushButton,"batLoad")
        batLoadBTN.clicked.connect(lambda: batLoad(self,confPath))

        btRefreshBTN = self.findChild(QPushButton,"btRefresh")
        btRefreshBTN.clicked.connect(lambda: btRefresh(self,measPath))
        
        btLoadBTN = self.findChild(QPushButton,"btLoad")
        btLoadBTN.clicked.connect(lambda: btLoad(self,measPath,graficoS))       
              
        testBTN = self.findChild(QPushButton,"testBtn")
        testBTN.clicked.connect(lambda: testBtn(self))  
        
        discBTN = self.findChild(QPushButton,"discBtn")
        discBTN.clicked.connect(lambda: discBtn(discBTN,self,discharge,graficoD))  
        
        
        wifiBTN = self.findChild(QPushButton,"btWifi")
        wifiBTN.clicked.connect(lambda: btWifi(self))  
        
        serverBTN = self.findChild(QPushButton,"btServer")
        serverBTN.clicked.connect(lambda: btServer(self,self.charge.cloud))        
        
        self.show()
        if platform == "linux":
            self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
            self.showMaximized()



    @Slot()
    def on_charge_finished(self):
        self.findChild(QLineEdit, "vMaxIN").setEnabled(True)
        self.findChild(QLineEdit, "iMaxIN").setEnabled(True)
        self.findChild(QLineEdit, "iMinIN").setEnabled(True)
        self.findChild(QLineEdit, "tMaxIN").setEnabled(True)
        self.findChild(QLineEdit, "ctIN").setEnabled(True)
        self.findChild(QLineEdit, "batNameIN").setEnabled(True)
        self.findChild(QPushButton, "btCharge").setText("Cargar")
        self.findChild(QPlainTextEdit, "statusText").setPlainText("Waiting")

    def uncheck(self):
        self.findChild(QCheckBox,"chkWifi").setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    
    sys.exit(app.exec())



