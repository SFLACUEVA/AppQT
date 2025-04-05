from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent
from sys import platform


class LineEdit(QLineEdit):
    
    ventana = None
    
    def setWD(self, wd):
        self.ventana = wd
        
    def OnKB(self):
        if platform == "linux":
            self.ventana.showNormal()
            
    def OffKB(self):
        if platform == "linux":
            self.ventana.showFullScreen()
        
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
        
    
