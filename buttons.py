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
from PERIF import io
from functions import *

def btCharge(bt: QPushButton,wd,carga: clases.carga,graf: DualAxisChart):
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
                
                carga.hilo = Thread(target=threadCargar,args=(carga,graf,wd))
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
        stLb.setPlainText("Esperando")
        carga.isActive = False
        carga.hilo.join()
           
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

def btRefresh(wd, db):
    combo = wd.findChild(QComboBox,"sumCombo")
    con = sqlite3.connect(db)
    cur = con.cursor()
    sel = "SELECT Tabla FROM summary;"
    res = cur.execute(sel).fetchall()
    nombres = []
    
    for fila in res:
        nombres.append(fila[0])
    
    combo.clear()
    combo.addItems(nombres)

def btLoad(wd,db,graf: DualAxisChart):

    tabName = wd.findChild(QComboBox,"sumCombo").currentText()
    con = sqlite3.connect(db)
    cur = con.cursor()
    sel = "SELECT * FROM '"+tabName+"' ;"
    medidas = cur.execute(sel).fetchall()
    
    sel = "SELECT * FROM summary WHERE Tabla =  '"+tabName+"' ;"
    resumen = cur.execute(sel).fetchall()
    
    wd.findChild(QLabel,"batNameLab").setText(str(resumen[0][0]))
    wd.findChild(QLabel,"ctLab").setText(str(resumen[0][7]))
    wd.findChild(QLabel,"iMLab").setText(str(resumen[0][5]))
    wd.findChild(QLabel,"imLab").setText(str(resumen[0][6]))
    wd.findChild(QLabel,"tMLab").setText(str(resumen[0][8]))
    wd.findChild(QLabel,"vMLab").setText(str(resumen[0][4]))
    
    wd.findChild(QLabel,"StartLb").setText(str(resumen[0][1]))
    wd.findChild(QLabel,"StopLb").setText(str(resumen[0][2]))
    wd.findChild(QLabel,"tLb").setText(str(round(resumen[0][14],3))+"ºC-"+str(round(resumen[0][13],3))+"ºC")
    wd.findChild(QLabel,"iLb").setText(str(round(resumen[0][12],3))+"A-"+str(round(resumen[0][11],3))+"A")
    wd.findChild(QLabel,"vLb").setText(str(round(resumen[0][10],3))+"V-"+str(round(resumen[0][9],3))+"V")
    
    v = []
    i = [] 
    t = []
    
    for fila in medidas:
        v.append(fila[1])
        i.append(fila[2])
        t.append(fila[0])
    
    graf.plot(v,i,t)
    
def testBtn(wd):

    IO = io()
    IO.RELAY0.off()
    IO.RELAY1.off()
    IO.RELAY2.off()
    
    IO.LED0.off()
    IO.LED1.on()
    vFloat,i = IO.getVI()
    sleep(0.2)
    
    IO.RELAY1.on()
    sleep(0.2)
    vLoad,iLoad = IO.getVI()
    IO.RELAY1.off()
    IO.LED1.off()
    iLoad= abs(iLoad)
    R = (vFloat-vLoad)/iLoad
    
    wd.findChild(QLabel,"testFloat").setText(str(round(vFloat,3))+"V")
    wd.findChild(QLabel,"testLoad").setText(str(round(vLoad,3))+"V")
    wd.findChild(QLabel,"testR").setText(str(round(R,3))+"Ω")
    wd.findChild(QLabel,"testCurrent").setText(str(round(iLoad,3))+"mA")
    
def discBtn(bt: QPushButton,wd,descarga: clases.descarga,graf: DualAxisChart):
    if descarga.isActive == False:
                descarga.hilo = Thread(target=threadDescargar,args=(descarga,graf,wd))
                descarga.hilo.setDaemon(True)
                bt.setText("Stop")
                
                descarga.Start()
                descarga.hilo.start()
    
    else:
        
        bt.setText("Start test")
        carga.Stop()
        carga.hilo.join()