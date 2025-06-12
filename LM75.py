import time
import smbus2


I2C_BUS_NUMBER			= 1
LM75_ADDRESS		 	= 0x48  #Default address if not supplied. Valid range 0x48 - 0x4F

LM75_TEMP_REGISTER 	 	= 0
LM75_CONF_REGISTER 	 	= 1
LM75_THYST_REGISTER  	= 2
LM75_TOS_REGISTER 	 	= 3

LM75_CONF_SHUTDOWN  	= 0
LM75_CONF_OS_COMP_INT 	= 1
LM75_CONF_OS_POL 	 	= 2
LM75_CONF_OS_F_QUE 	 	= 3


class LM75(object):
	"""Handles the NCT75 communication"""
 
	def __init__(self, mode=LM75_CONF_OS_COMP_INT, i2c_address=LM75_ADDRESS,
							 busnum=I2C_BUS_NUMBER):
		self._mode = mode
		self.i2c_address = i2c_address
		self._bus = smbus2.SMBus(busnum)

	def getRegisterVal(self):
		try:
			raw = self._bus.read_word_data(self.i2c_address, LM75_TEMP_REGISTER) & 0xFFFF
			reordered_raw = ((raw << 8) & 0xFF00) + (raw >> 8)
			temperature_is_negative = (reordered_raw >> 15)
			if temperature_is_negative:
				register_value = (((reordered_raw >> 5) & 0xFFFF) - 1) - 0b0000011111111111
			else:
				register_value = reordered_raw >> 5
		except:
			print("Error while trying to read i2c bus at chip address", hex(self.i2c_address), "\n")
			raise
		return register_value

	def getCelsius(self):
		"""Return celsius temperature"""
     
		c_val = self.getRegisterVal() * 0.125
		return round(c_val, 3)

	def getFahrenheit(self):
		"""Returns farenheit temperature"""

		f_val = (self.getCelsius() * (9.0/5.0)) + 32.0
		return round(f_val, 3)
