from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent
from sys import platform
from time import sleep
from datetime import datetime

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import MaxNLocator
import subprocess

class DualAxisChart(QWidget):
    def __init__(self,wd,lo):
        super().__init__()

        layout = wd.findChild(QHBoxLayout,lo)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        x = [0, 1, "patata", 3, 4, 5]
        tension = [0, 1, 2, 3, 4, 5]   # Voltaje
        corriente = [0, 10, 20, 30, 20, 10]  # Corriente
        #self.plot(tension,corriente,x)



    def plot(self,tension,corriente,tiempo):
        self.figure.clear()
        ax1 = self.figure.add_subplot(111)
        ax2 = ax1.twinx()  # Segundo eje Y
        ax1.grid(True)
        ax1.set_ylim(0,16)
        ax2.set_ylim(0,3.5)
        
        mins =[]
        for t in tiempo:
            objeto_datetime = datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")
            mins.append(objeto_datetime.strftime("%H:%M:%S"))

        
        # Primer eje (Tensión)
        ax1.plot(mins, tension, 'b-', label="Voltage (V)")
        ax1.set_ylabel("Voltage (V)", color='b')
        ax1.tick_params(axis='y', labelcolor='b')

        # Segundo eje (Corriente)
        ax2.plot(mins, corriente, 'r--', label="Current (A)")
        ax2.set_ylabel("Current (A)", color='r')
        ax2.tick_params(axis='y', labelcolor='r')

        # Eje X
        ax1.set_xlabel("")
        ax1.xaxis.set_major_locator(MaxNLocator(nbins=6))
        
        # Leyenda combinada (opcional)
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

        self.canvas.draw()

class LineEdit(QLineEdit):
    
    plat = platform
    #plat = "linux"
    ventana = None
    
    def setWD(self, wd):
        self.ventana = wd
        
    def OnKB(self):
        if self.plat == "linux":
            sleep(0.1)
            subprocess.Popen(["wvkbd-mobintl"])
            #self.ventana.showNormal()
            
    def OffKB(self):
        if self.plat == "linux":
            sleep(0.1)
            subprocess.Popen(["killall","wvkbd-mobintl"])
            #self.ventana.showFullScreen()
            
        
    def setOutFocusAct(self, funcion ):
        self.OutFocusAct = funcion
    
    def setInFocusAct(self, funcion ):
        self.InFocusAct = funcion
        
    def focusInEvent(self, event: QFocusEvent) -> None:
        print(self.objectName()+" ha ganado el foco.")
        self.OnKB()
        super().focusInEvent(event)
        
    def focusOutEvent(self, event: QFocusEvent) -> None:
        print(self.objectName()+" ha perdido el foco.")
        self.OffKB()
        super().focusOutEvent(event)
        
