# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Slot
from PySide6.QtCore import QObject as obj



# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print("INICIANDO")
        closeBTN = self.findChild(QPushButton,"btClose")
        closeBTN.clicked.connect(lambda: btClose(closeBTN,self))



def btClose(bt,wndw):
    print("Close")
    bt.setText("CLICK")
    wndw.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
