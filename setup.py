from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent
from CustomWidgets import LineEdit 




def StartServerIn(wd):
    ventana = wd
    grid = ventana.findChild(QHBoxLayout,"svrIN")
    
    ipIN = LineEdit("")
    ipIN.setObjectName("ipIN")
    ipIN.setWD(wd)
    
    nameIN = LineEdit("")
    nameIN.setObjectName("nameIN")
    nameIN.setWD(wd)
    
    grid.addWidget(nameIN)
    grid.addWidget(ipIN)
            
