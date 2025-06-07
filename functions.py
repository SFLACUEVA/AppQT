from threading import Thread,Timer
from CustomWidgets import *
import time
import clases
import random  
import multitimer
import sqlite3
from PERIF import io

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

    if not (1<=iM<=3):
        return False
    
    if not (0.5<=im<=3 and im<iM):
        return False
    
    if not (25<=tM):
        return False
    
    if not (0<=im<=100):
        return False
    
    return True
    
def threadCargar(carga: clases.carga,graf: DualAxisChart):
    
    IO=io()
    IO.pot.write(1023)
    IO.iLim(45)
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
    print("acabado")
    IO.buckEn.off() 
    sleep(0.2)   
    IO.RELAY2.off()
    sleep(0.5)
    IO.RELAY0.off()
    sleep(0.5)
    mTimer.stop()

def cargar(carga: clases.carga,graf: DualAxisChart,IO:io):
    print("CARGA")
    v,i=IO.getVI()
    carga.add(v,i/1000,random.randrange(25,55))
    graf.plot(carga.V,carga.I,carga.D)
    

    
  
    
       


