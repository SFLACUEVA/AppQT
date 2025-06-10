from threading import Thread,Timer
from CustomWidgets import *
import time
import clases
import random  
import multitimer
import sqlite3
from PERIF import io
from PySide6.QtWidgets import QPlainTextEdit, QLabel, QComboBox
import numpy as np

def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False
    
def are_float(string):
    for txt in string:
        if not txt.replace(".", "").isnumeric():
            return False
    
    return True
         
def are_ok(vM,iM,im,tM,ct):
    if not (13<=vM<=15):
        return False

    if not (1.23<=iM<=3):
        return False
    
    if not (im<=3 and im<iM):
        return False
    
    if not (25<=tM):
        return False
    
    if not (0<=im<=100):
        return False
    
    return True
    
def i_to_dt(x):

    x1, y1 = 1.23, 7
    x2, y2 = 3, 77

    m = (y2 - y1) / (x2 - x1)

    b = y1 - m * x1

    return m * x + b    

 
def threadCargar(carga: clases.carga,graf: DualAxisChart,wd):
    
    IO=io()
    tmp = (1-(15-carga.LimVMax)/2)*1023
    IO.SetPot(tmp)
    tmp = i_to_dt(carga.LimIMax)
    IO.iLim.setDuty(tmp)
    IO.buckEn.off()
    IO.RELAY0.on()
    sleep(0.5)
    IO.RELAY2.on()
    IO.buckEn.on()
    sleep(0.5)
    
    mTimer = multitimer.MultiTimer(interval=1,function=cargar,args=(carga,graf,IO)) 
    mTimer.start()
    
    while carga.isActive:
        #print("Check")
        time.sleep(0.01)
        
    carga.Stop()
    print("acabado")
    IO.buckEn.off() 
    sleep(0.2)   
    IO.RELAY2.off()
    sleep(0.5)
    IO.RELAY0.off()
    sleep(0.5)
    mTimer.stop()
    
    stLb = wd.findChild(QPlainTextEdit,"statusText") 
    bt= wd.findChild(QPushButton,"btCharge")
    wd.findChild(LineEdit,"vMaxIN").setEnabled(True)
    wd.findChild(LineEdit,"iMaxIN").setEnabled(True)
    wd.findChild(LineEdit,"iMinIN").setEnabled(True)
    wd.findChild(LineEdit,"tMaxIN").setEnabled(True)
    wd.findChild(LineEdit,"ctIN").setEnabled(True)
    wd.findChild(LineEdit,"batNameIN").setEnabled(True)
    stLb.setPlainText("Esperando")
    bt.setText("Cargar")
    stLb = wd.findChild(QPlainTextEdit,"statusText") 
    

def cargar(carga: clases.carga,graf: DualAxisChart,IO:io):
    if carga.isActive:
        print("CARGA")
        v,i=IO.getVI()
        t = IO.getTemp()
        carga.add(v,i/1000,t)
        
        tmp = np.clip((1-(15-(carga.LimVMax-carga.ct*t)/2)*1023),0,1023)
        IO.SetPot(tmp)
        
        graf.plot(carga.V,carga.I,carga.D)
        if i/1000 < carga.LimIMin or t > carga.LimTMax:
            carga.isActive=False
    