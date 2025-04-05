import sys
import time
import sqlite3 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QTableWidget, QTabWidget, QTableWidgetItem,QLineEdit, QWidget, QGridLayout
from PySide6.QtCore import QEvent
from PySide6 import QtCore
from PySide6.QtGui import QFocusEvent
import urllib.request
import LocalDB as LDB
from sys import platform
import CustomWidgets


def srvrIn(self):
    pantalla = self.findChild(QHBoxLayout,"horizontalLayout")     
    pepe = CustomWidgets.CustomLE("PEPE")
    pepe.setObjectName("PEPE")
    pantalla.addWidget(pepe)
    
    juan = CustomWidgets.CustomLE("JUAN")
    juan.setObjectName("JUAN")
    juan.setInFocusAct(test)
    pantalla.addWidget(juan)