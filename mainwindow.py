# This Python file uses the following encoding: utf-8
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
        charge = carga()
        cloud = cloudComm() 
        
        graficoS,graficoC,graficoD = StartServerIn(self)
        
        closeBTN = self.findChild(QPushButton,"btClose")
        closeBTN.clicked.connect(lambda: btClose(closeBTN,self,charge))
        
        chargeBTN = self.findChild(QPushButton,"btCharge")
        chargeBTN.clicked.connect(lambda: btCharge(chargeBTN,self,charge,graficoC))
        
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
              
        
        self.show()
        if platform == "linux":
            self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
            self.showMaximized()







if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    
    sys.exit(app.exec())
