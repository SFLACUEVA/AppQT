import sys
import time
import sqlite3 
from PySide6.QtWidgets import QPlainTextEdit, QLabel, QComboBox
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
                
                stLb.setPlainText("Charging battery")
                bt.setText("Stop")
                
                carga.Start()
                carga.hilo.start()
            else:
                stLb.setPlainText("Parameters in configuration out of range")

        else:
           stLb.setPlainText("Invalid charaters in configuration")
            
        
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
    
def batSave(wd,db):
    
    stLb = wd.findChild(QPlainTextEdit,"statusText")  
    vM = wd.findChild(LineEdit,"vMaxIN").text()
    iM = wd.findChild(LineEdit,"iMaxIN").text()
    im = wd.findChild(LineEdit,"iMinIN").text()
    tM = wd.findChild(LineEdit,"tMaxIN").text()
    ct = wd.findChild(LineEdit,"ctIN").text()
    
    if(are_float([vM,iM,im,tM,ct])):
        vM = float(vM)
        iM = float(iM)
        im = float(im)
        tM = float(tM)
        ct = float(ct)
        
        if(are_ok(vM,iM,im,tM,ct)):
            nm = wd.findChild(LineEdit,"batNameIN").text()
            con = sqlite3.connect(db)
            cur = con.cursor()
            dele = "DELETE FROM battery WHERE Name = '"+nm+"';"
            print(dele)
            res = cur.execute(dele)
            
            ins = "INSERT INTO battery ('Name','vMax','iMax','iMin','tMax','tCom') VALUES ("
            ins += "'" + str(nm) + "',"
            ins += "'" + str(vM) + "',"
            ins += "'" + str(iM) + "',"
            ins += "'" + str(im) + "',"
            ins += "'" + str(tM) + "',"
            ins += "'" + str(ct) + "');"
            
            res = cur.execute(ins)
            con.commit()
            con.close()
            
            stLb.setPlainText("Battery configuration saved successfully!")
            
        else:
            stLb.setPlainText("Parameters in configuration out of range")
            
    else:
       stLb.setPlainText("Invalid charaters in configuration")

def batRefresh(wd,db):
    combo = wd.findChild(QComboBox,"batCombo")
    
    con = sqlite3.connect(db)
    cur = con.cursor()
    sel = "SELECT Name FROM battery;"
    res = cur.execute(sel).fetchall()
    nombres = []
    for fila in res:
        nombres.append(fila[0])
    
    combo.clear()
    combo.addItems(nombres)
    print(combo.currentText())

def batLoad(wd,db):
    stLb = wd.findChild(QPlainTextEdit,"statusText")  
    batName = wd.findChild(QComboBox,"batCombo").currentText()
    con = sqlite3.connect(db)
    cur = con.cursor()
    sel = "SELECT * FROM battery WHERE Name ='"+batName+"' ;"
    res = cur.execute(sel).fetchone()
    print(res)
    
    
    nm = str(res[0])
    vM = str(res[1])
    iM = str(res[2])
    im = str(res[3])
    tM = str(res[4])
    ct = str(res[5])

    wd.findChild(LineEdit,"batNameIN").setText(nm)
    wd.findChild(LineEdit,"vMaxIN").setText(vM)
    wd.findChild(LineEdit,"iMaxIN").setText(iM)
    wd.findChild(LineEdit,"iMinIN").setText(im)
    wd.findChild(LineEdit,"tMaxIN").setText(tM)
    wd.findChild(LineEdit,"ctIN").setText(ct)
    stLb.setPlainText('Battery "'+nm+'" loaded succesfully!' )

def btClose(bt,wd,carga: clases.carga):
    if carga.hilo:
        carga.isActive= False
        carga.hilo.join()
    print("Close")
    bt.setText("CLICK")
    wd.close()


