import threading

class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def modificar(self):
        self.valor += 1

def funcion_hilo(obj):
    obj.modificar()

# Crear una instancia de la clase
mi_objeto = MiClase(5)

# Crear y lanzar un hilo
hilo = threading.Thread(target=funcion_hilo, args=(mi_objeto,))
hilo.start()
hilo.join()

print(mi_objeto.valor)  # Debería imprimir 6
