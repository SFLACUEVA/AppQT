from gpiozero import DigitalOutputDevice, PWMLED
from time import sleep
from ina219 import INA219
from ina219 import DeviceRangeError
from LM75 import LM75
import smbus2
from pwm import PWMPin
from pot import AD5272

class io():
    """Handles all the IO"""
    bus = 10
    
    def __init__(self):
        try:
            self.LED0 = DigitalOutputDevice(7,active_high=False)
            self.LED1 = DigitalOutputDevice(8,active_high=False)
            self.RELAY0 = DigitalOutputDevice(24,active_high=True)
            self.RELAY1 = DigitalOutputDevice(23,active_high=True)
            self.RELAY2 = DigitalOutputDevice(18,active_high=True)
            self.buckEn = DigitalOutputDevice(6,active_high=False)
            self.iLim = PWMPin(20000,0,12)
            self.sTemp = LM75(busnum=self.bus)
            self.sTemp.i2c_address = 0x4F
            self.ina = INA219(0.013,busnum=self.bus,address=0x40)
            self.ina.configure()
            self.pot = AD5272()
        except Exception as e:
            print(e)
            print("Error iniciando los pines")
      
    def getVI(self):
        """Read INA219"""
        
        try:
            v = self.ina.voltage()
            i = self.ina.current()
            print("Bus Voltage: %.3f V" % v)
            print("Bus Current: %.3f mA" % i)
            return v,i
        except DeviceRangeError as e:
            print(e)
            print("Error leyendo V/I")
            return 0,0
                  
    def getTemp(self):
        """Read NCT75"""
        
        try:
            C = self.sTemp.getCelsius()
            print("temp_c:", C)
            return C
        except Exception as e:
            print(e)
            print("Error leyendo la temperatura")
            return 25
    
    def SetPot(self, value):
        """Set the AD5272 to the desired value"""
        self.pot.write(int(value))
        pass
