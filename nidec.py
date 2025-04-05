from PySide6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PySide6.QtGui import QFocusEvent
import sys

class MiLineEdit(QLineEdit):
    def focusInEvent(self, event: QFocusEvent) -> None:
        # Comportamiento personalizado: por ejemplo, imprimir en consola
        print("El QLineEdit ha ganado el foco.")
        
        # Llamar al método original de la clase base
        super().focusInEvent(event)




class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de focusInEvent")
        layout = QVBoxLayout(self)
        
        self.line_edit = MiLineEdit()
        layout.addWidget(self.line_edit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())