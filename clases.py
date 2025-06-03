import datetime;
import time
import sqlite3 
import pathlib

class carga():
    
    LimVMax = None #Limite de tension
    LimIMax = None #Limite de corriente
    LimIMin = None #para al llegar
    ct = None #factor de compesación termica
    LimTMax = None #temperatura maxima
    
    #valores limites de las medidas
    MeasVMax = None 
    MeasVMin = None 
    MeasIMax = None
    MeasIMin = None
    MeasTMax = None
    MeasTMin = None
    
    isActive = False
    batName = "Carga"
    StartTime = None
    StopTime = None
    ts = None
    dev = "DEV0"
    tableName = ""
    
    hilo = None
    
    V = []
    I = []
    T = []
    D = []
    
        
    def add(self,v,i,t):
        self.V.append(v)
        self.I.append(i)
        self.T.append(t)
        self.D.append(datetime.datetime.now().replace(microsecond=0).isoformat())
        
    def Start(self):
        
        self.V = []
        self.I = []
        self.T = []
        self.D = []
        self.ts = int(time.time())
        self.StartTime = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.isActive = True
        
    def Stop(self):
        self.isActive = True
        self.StopTime = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.MeasVMax = max(self.V)
        self.MeasVMin = min(self.V)
        self.MeasIMax = max(self.I)
        self.MeasIMin = min(self.I)
        self.MeasTMax = max(self.T)
        self.MeasTMin = min(self.T)
        self.updateLocal()
        
    
    def setConf(self,vM,iM,im,ct,tM):
        self.LimIMax= iM
        self.LimVMax = vM
        self.LimIMin = im
        self.ct=ct
        self.LimTMax = tM
        
    def setName(self,bname):
        self.batName = str(bname)
        
    def updateLocal(self):
        
        sqlpath = str(pathlib.Path(__file__).parent.resolve() / "Resources" / "measures.db")
        con = sqlite3.connect(sqlpath)
        cur = con.cursor()
        
        self.tableName = self.batName + "_" + self.dev + "_" + str(self.StartTime)
        
        cre = 'CREATE TABLE "'+self.tableName+'" ("time" TEXT,"V" NUMERIC,"I" NUMERIC,"T" NUMERIC);'
        cur.execute(cre)
        con.commit()
        
        for i in range(len(self.D)):
            ins = ("INSERT INTO '"+self.tableName+"' ('time','V','I','T') VALUES (")
            ins = ins + "'"+str(self.D[i])+"',"
            ins = ins + "'"+str(self.V[i])+"',"
            ins = ins + "'"+str(self.I[i])+"',"
            ins = ins + "'"+str(self.T[i])+"');"
            print(ins)
            cur.execute(ins)
        con.commit()
        
        
        
        
        req = ("INSERT INTO summary ('Name','Start','Stop','Tabla','LimVMax','LimIMax','LimIMin','ct','LimTMax','MeasVMax','MeasVMin','MeasIMax','MeasIMin','MeasTMax','MeasTMin','DeviceName') VALUES (")
        req= req + "'" + self.batName + "',"
        req= req + "'" + str(self.StartTime) + "',"
        req= req + "'" + str(self.StopTime) + "',"
        req= req + "'" + self.tableName + "',"
        req= req + "'" + str(self.LimVMax) + "',"
        req= req + "'" + str(self.LimIMax) + "',"
        req= req + "'" + str(self.LimIMin) + "',"
        req= req + "'" + str(self.ct) + "',"
        req= req + "'" + str(self.LimTMax) + "',"
        req= req + "'" + str(self.MeasVMax) + "',"
        req= req + "'" + str(self.MeasVMin) + "',"
        req= req + "'" + str(self.MeasIMax) + "',"
        req= req + "'" + str(self.MeasIMin) + "',"
        req= req + "'" + str(self.MeasTMax) + "',"
        req= req + "'" + str(self.MeasTMin) + "',"
        req = req + "'" + self.dev+"');"
        cur.execute(req)
        con.commit()
        con.close()
            
class ConfigDB():
    path = None
    cur = None
    con = None
    
    def  __init__(self,db):
        self.path = db
        print(db)
        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()
        
    def getServer(self):
        res = self.cur.execute("SELECT * FROM SRVR_IP")
        cosa = res.fetchone()
        ip = cosa[0].strip()
        name = cosa[1].strip()
        return ip, name
    
    def getServerList(self):
        res = self.cur.execute("SELECT * FROM SRVR_IP")
        return res.fetchall()
    
    def close(self):
        self.con.close()
        
class cloudComm():
    isActtive = False
    ip = None

        
        
        
    
        
        
        
        


        