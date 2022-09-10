import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class pantalla(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pantalla()
    GUI.show()
    sys.exit(app.exec_())