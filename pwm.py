import pigpio
from time import sleep

class PWMPin():
    """Handles the PWM signal"""
    
    def __init__(self,f,duty,pin):
        """Starts the PWM"""
        
        self.pi = pigpio.pi()
        self.range = range
        self.duty = duty
        self.pin = pin
        self.f = f
        
        # 1. Establecer el rango del ciclo de trabajo para el GPIO.
        self.pi.set_PWM_range(pin, 100)
        print(f"Rango de PWM establecido en GPIO{pin} a { self.pi.get_PWM_range(pin)}.")

        # 2. Establecer la frecuencia del PWM para el GPIO.
        self.pi.set_PWM_frequency(pin, f)
        print(f"Frecuencia de PWM establecida en GPIO{pin} a { self.pi.get_PWM_frequency(pin)} Hz.")

        # 3. Establecer el ciclo de trabajo (duty cycle) para el GPIO.
        self.pi.set_PWM_dutycycle(pin, duty)
        print(f"Ciclo de trabajo establecido en GPIO{pin} a {self.pi.get_PWM_dutycycle(pin)} ({duty}%).")
    
      
    def setDuty(self,duty):
        """Sets the duty cycle"""
        
        self.pi.set_PWM_dutycycle(self.pin,duty)
        self.duty=duty
        
       
