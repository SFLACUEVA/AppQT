from PySide6.QtWidgets import QApplication,QVBoxLayout , QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent
from CustomWidgets import LineEdit, DualAxisChart 
from PySide6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

def StartServerIn(wd):
    ventana = wd
    confGrid = ventana.findChild(QVBoxLayout,"settingsLayout")
    
    ipIN = LineEdit("")
    ipIN.setObjectName("ipIN")
    ipIN.setWD(wd)
    
    devIN = LineEdit("")
    devIN.setObjectName("devIN")
    devIN.setText("DEV0")
    devIN.setWD(wd)
    
    rIN = LineEdit("")
    rIN.setObjectName("rIN")
    rIN.setText("30")
    rIN.setWD(wd)    
    
    ssidIN = LineEdit("")
    ssidIN.setObjectName("ssidIN")
    ssidIN.setWD(wd)
    
    pwdIN = LineEdit("")
    pwdIN.setObjectName("pwdIN")
    pwdIN.setWD(wd)      
    

    
    confGrid.addWidget(ipIN)
    confGrid.addWidget(devIN)
    confGrid.addWidget(rIN)
    confGrid.addWidget(ssidIN)
    confGrid.addWidget(pwdIN)    
    
    graficoC = DualAxisChart(wd,"chaLayout")
    graficoS = DualAxisChart(wd,"consLayout")
    graficoD = DualAxisChart(wd,"loadLayout")
    
    gridLim = ventana.findChild(QVBoxLayout,"limLayout")
    
    nameIN = LineEdit("")
    nameIN.setText("MVH1290")
    nameIN.setObjectName("batNameIN")
    nameIN.setWD(wd)
    
    vMaxIN = LineEdit("")
    vMaxIN.setObjectName("vMaxIN")
    vMaxIN.setText("14")
    vMaxIN.setWD(wd)
    
    iMinIN = LineEdit("")
    iMinIN.setText("0.25")
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
    
   
    
    
    
    
    return graficoS,graficoC,graficoD
    
    
    
    
    
   
   
    
    
            
