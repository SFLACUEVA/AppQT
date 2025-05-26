import sys
import time
import sqlite3 
from PySide6.QtWidgets import QPlainTextEdit, QLabel
import urllib.request
from sys import platform
from setup import StartServerIn
from PySide6 import QtCore
from ui_form import Ui_MainWindow
from clases import *
from CustomWidgets import *
from functions import *

def btCharge(bt: QPushButton,wd,carga: carga,graf: DualAxisChart):
    print("btCharge")
    
    stLb = wd.findChild(QPlainTextEdit,"statusText") 

    if(not carga.isActive):
        
        vM = wd.findChild(LineEdit,"vMaxIN").text()
        iM = wd.findChild(LineEdit,"iMaxIN").text()
        im = wd.findChild(LineEdit,"iMinIN").text()
        tM = wd.findChild(LineEdit,"tMaxIN").text()
        ct = wd.findChild(LineEdit,"ctIN").text()
        
        if(are_float([vM,iM,im,tM,ct])):
            print("Son numeros")
            vM = float(vM)
            iM = float(iM)
            im = float(im)
            tM = float(tM)
            ct = float(ct)
            
            if(are_ok(vM,iM,im,tM,ct)):
                wd.findChild(LineEdit,"vMaxIN").setEnabled(False)
                wd.findChild(LineEdit,"iMaxIN").setEnabled(False)
                wd.findChild(LineEdit,"iMinIN").setEnabled(False)
                wd.findChild(LineEdit,"tMaxIN").setEnabled(False)
                wd.findChild(LineEdit,"ctIN").setEnabled(False)
                wd.findChild(LineEdit,"batNameIN").setEnabled(False) 
                
                carga.setConf(vM,iM,im,ct,tM)
                carga.setName(wd.findChild(LineEdit,"batNameIN").text())
                
                carga.hilo = Thread(target=threadCargar,args=(carga,graf))
                carga.hilo.setDaemon(True)
                
                stLb.setPlainText("Cargando")
                bt.setText("Stop")
                
                carga.Start()
                carga.hilo.start()
                
        
        else:
            stLb.setPlainText("Caracteres en la configuracion no validos")
            
        
    else:
        
        
        wd.findChild(LineEdit,"vMaxIN").setEnabled(True)
        wd.findChild(LineEdit,"iMaxIN").setEnabled(True)
        wd.findChild(LineEdit,"iMinIN").setEnabled(True)
        wd.findChild(LineEdit,"tMaxIN").setEnabled(True)
        wd.findChild(LineEdit,"ctIN").setEnabled(True)
        wd.findChild(LineEdit,"batNameIN").setEnabled(True) 
        bt.setText("Cargar")
        carga.Stop()
        stLb.setPlainText("Esperando")
        carga.isActive= not carga.isActive
        carga.hilo.join()
        pass
    
     

def btClose(bt,wd,carga: clases.carga):
    if carga.hilo:
        carga.isActive= False
        carga.hilo.join()
    print("Close")
    bt.setText("CLICK")
    wd.close()


