from PySide6.QtWidgets import QApplication,QVBoxLayout , QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent
from CustomWidgets import LineEdit, DualAxisChart 

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

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
    
    grafico = DualAxisChart(wd)
    gridLim = ventana.findChild(QVBoxLayout,"limLayout")
    
    nameIN = LineEdit("")
    nameIN.setText("MVH1290")
    nameIN.setObjectName("batNameIN")
    nameIN.setWD(wd)
    
    vMaxIN = LineEdit("")
    vMaxIN.setObjectName("vMaxIN")
    vMaxIN.setText("14.9")
    vMaxIN.setWD(wd)
    
    iMinIN = LineEdit("")
    iMinIN.setText("0.5")
    iMinIN.setObjectName("iMinIN")
    iMinIN.setWD(wd)
    
    iMaxIN = LineEdit("")
    iMaxIN.setText("2.25")
    iMaxIN.setObjectName("iMaxIN")
    iMaxIN.setWD(wd)
    
    tMaxIN = LineEdit("")
    tMaxIN.setText("60")
    tMaxIN.setObjectName("tMaxIN")
    tMaxIN.setWD(wd)
    
    ctIN = LineEdit("")
    ctIN.setText("30")
    ctIN.setObjectName("ctIN")
    ctIN.setWD(wd)
    
    gridLim.addWidget(nameIN)
    gridLim.addWidget(vMaxIN)
    gridLim.addWidget(iMaxIN)
    gridLim.addWidget(iMinIN)
    gridLim.addWidget(tMaxIN)
    gridLim.addWidget(ctIN)
    
   
    
    
    
    
    return grafico
    
    
    
    
    
   
   
    
    
            
