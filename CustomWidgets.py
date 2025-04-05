from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent



class CustomLE(QLineEdit):
    InFocusAct = print("hola")
    
    def setInFocusAct(self, funcion ):
        self.InFocusAct = funcion
        
    def focusInEvent(self, event: QFocusEvent) -> None:
        # Comportamiento personalizado: por ejemplo, imprimir en consola
        print(self.objectName()+" ha ganado el foco.")
        self.InFocusAct()
        # Llamar al método original de la clase base
        super().focusInEvent(event)
        
    def focusOutEvent(self, event: QFocusEvent) -> None:
        # Comportamiento personalizado: por ejemplo, imprimir en consola
        print(self.objectName()+" ha perdido el foco.")
        
        # Llamar al método original de la clase base
        super().focusOutEvent(event)