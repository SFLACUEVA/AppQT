import smbus2
import time


I2C_BUS_NUM = 10
AD5272_I2C_ADDRESS = 0x2F # 
AD5272_RDAC_WRITE = 0x01  


class AD5272:
    def __init__(self, addr: int = AD5272_I2C_ADDRESS, bus_num: int = I2C_BUS_NUM):
        self._addr = addr
        self._bus_num = bus_num
        self.bus = None # 

    def _open_bus(self):
        return smbus2.SMBus(self._bus_num)

    def _write_data_internal(self, cmd: int, data: int):

        first_byte_to_send = (cmd << 2) | ((data >> 8) & 0x03)
        second_byte_to_send = data & 0xFF
        message_bytes = [first_byte_to_send, second_byte_to_send]

        try:
            with smbus2.SMBus(self._bus_num) as bus:
                msg = smbus2.i2c_msg.write(self._addr, message_bytes)
                bus.i2c_rdwr(msg)
            return 0
        except FileNotFoundError:
            raise IOError(f"El bus I2C {self._bus_num} no se encontró. ¿Está I2C habilitado?")
        except Exception as e:
            raise IOError(f"Error I2C en _write_data_internal (cmd={cmd}, data={data}): {e}")

    def write(self, value: int):
        if not (0 <= value <= 1023):
            raise ValueError("El valor para el AD5272 debe estar entre 0 y 1023.")
        
        print(f"AD5272: Escribiendo RDAC con valor {value}...")
        return self._write_data_internal(AD5272_RDAC_WRITE, value)



if __name__ == '__main__':

    try:
        pot = AD5272(addr=AD5272_I2C_ADDRESS, bus_num=I2C_BUS_NUM)
        print("AD5272_Python objeto creado e inicializado.")
        time.sleep(1)


        print("\nEstableciendo resistencia valor 0")
        pot.write(0)
        time.sleep(2)

        print("\nEstableciendo resistencia valor 511")
        pot.write(511)
        time.sleep(2)

        print("\nEstableciendo resistencia valor 1023.")
        pot.write(1023)
        time.sleep(2)

        
    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except IOError as ioe:
        print(f"Error de E/S (I2C): {ioe}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    print("\nPrograma finalizado.")