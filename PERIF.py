from gpiozero import DigitalOutputDevice, PWMLED
from time import sleep
from ina219 import INA219
from ina219 import DeviceRangeError
from LM75 import LM75
import smbus2
from pwm import PWMPin
from pot import AD5272

class io():
    bus = 10
    
    def __init__(self):
        try:
            self.LED0 = DigitalOutputDevice(7,active_high=False)
            self.LED1 = DigitalOutputDevice(8,active_high=False)
            self.RELAY0 = DigitalOutputDevice(24,active_high=True)
            self.RELAY1 = DigitalOutputDevice(23,active_high=True)
            self.RELAY2 = DigitalOutputDevice(18,active_high=True)
            self.buckEn = DigitalOutputDevice(6,active_high=False)
            self.iLim = PWMPin(20000,50,12)
            self.pot = AD5272(0x2F,self.bus)
        except Exception as e:
            print(e)
            print("Error iniciando los pines")
      
    def getVI(self):
        
        ina = INA219(0.013,busnum=self.bus,address=0x40)
        ina.configure()
        
        try:
            v = ina.voltage()
            i =ina.current()
            print("Bus Voltage: %.3f V" % v)
            print("Bus Current: %.3f mA" % i)
            return v,i
        except DeviceRangeError as e:
            print(e)
            print("Error leyendo V/I")
            return 0,0
                  
    def getTemp(self):
        try:
            sens = LM75(busnum=self.bus)
            sens.i2c_address = 0x4F
            C = sens.getCelsius()
            print("temp_c:", C)
            return C
        except Exception as e:
            print(e)
            print("Error leyendo la temperatura")
    
    def SetPot(self, value):
        
        pass
              
if __name__=='__main__':       
    IO = io()

    IO.pot.write(1023)
    IO.buckEn.off()
    IO.RELAY0.on()
    sleep(0.5)
    IO.RELAY2.on()
    IO.buckEn.on()
    sleep(0.5)
    

    for i in range(10):

        IO.iLim.setDuty(100)
        print("")
        print(i)
        #IO.buckEn.on()
        print(IO.getVI())
        sleep(0.5)



    IO.buckEn.off() 
    sleep(0.2)   
    IO.RELAY2.off()
    sleep(0.5)
    IO.RELAY0.off()
    sleep(0.5)