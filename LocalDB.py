import sqlite3 

class ConfigDB():
    path = None
    cur = None
    con = None
    
    def  __init__(self,db):
        self.path = db
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