import datetime;
import time
import sqlite3 
import pathlib
from urllib import request

class carga():
    
    cloud = None
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
    dev = ""
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
        now = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.D.append(now)
        self.cloud.sendVal(v,i,t,t,self)
        
    def Start(self):
        
        self.V = []
        self.I = []
        self.T = []
        self.D = []
        self.ts = int(time.time())
        self.StartTime = datetime.datetime.now().replace(microsecond=0).isoformat()
        self.tableName = self.batName + "_" + self.dev + "_" + str(self.StartTime)
        self.cloud.createTable(self)
        self.isActive = True
        
    def Stop(self):
        self.isActive = False
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
    
    isActive = False
    ip=None
    
    def createTable(self,cargaAct:carga):
        if self.isActive:
            try:        
                req = "http://"+self.ip+"/measures.php?f=c&name="+cargaAct.batName
                req = req +"&start=" + str(cargaAct.StartTime)
                req = req +"&tabla=" + str(cargaAct.tableName)
                req = req +"&LimVMax=" + str(cargaAct.LimVMax)
                req = req +"&LimIMax=" + str(cargaAct.LimIMax)
                req = req +"&LimIMin=" + str(cargaAct.LimIMin)
                req = req +"&ct=" + str(cargaAct.ct)
                req = req +"&LimTMax=" + str(cargaAct.LimIMax)
                req = req +"&DeviceName=" + str(cargaAct.dev)
                res = request.urlopen(req).read().decode().strip()
                print(res)
            except Exception as e:
                print(e)
                self.isActive=False
    
    def sendVal(self,v,i,t,h,cargaAct:carga):
                if self.isActive:
                    try:        
                        req = "http://"+self.ip+"/measures.php?f=i&tabla="+cargaAct.tableName
                        req = req +"&v=" + str(v)
                        req = req +"&i=" + str(i)
                        req = req +"&t=" + str(t)
                        req = req +"&h=" + str(h)
                        print(req)
                        print(request.urlopen(req).read().decode().strip())
                    except Exception as e:
                        print(e)
                        self.isActive=False
    
    def ping(self):
        try:
            req="http://"+self.ip+"/measures.php?f=p"
            res = request.urlopen(req).read().decode().strip()
            if res =="ping":
                self.isActive=True
                print("Connected to :"+self.ip)
                return True
            else:
                self.isActive=False
                return False
        except Exception as e:
                print(e)
                self.isActive=False
                return False

    def conect(self,ip):
        self.ip = ip
        return self.ping()
        
        
class descarga():
    V = []
    I = []
    D = []
    isActive = False
    hilo = None
    
    def add(self,v,i):
        self.V.append(v)
        self.I.append(i)
        self.D.append(datetime.datetime.now().replace(microsecond=0).isoformat())
    
    def Start(self):
        self.V = []
        self.I = []
        self.D = []
        self.isActive = True
        
    def Stop(self):
        self.isActive = False

if __name__=='__main__':  
    
    cloud = cloudComm()
    print(cloud.conect("SFLTFG"))
    
