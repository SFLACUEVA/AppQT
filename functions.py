from threading import Thread,Timer
from CustomWidgets import *
import time
import clases
import random  
import multitimer
import sqlite3

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
    
    mTimer = multitimer.MultiTimer(interval=1,function=cargar,args=(carga,graf,"I2C")) 
    mTimer.start()
    while carga.isActive:
        #print("Check")
        time.sleep(0.01)
    print("acabado")
    mTimer.stop()

def cargar(carga: clases.carga,graf: DualAxisChart,txt):
    print("CARGA")
    carga.add(random.randrange(13,15),random.randrange(0,3),random.randrange(25,55))
    graf.plot(carga.V,carga.I,carga.D)
    

    
  
    
       


