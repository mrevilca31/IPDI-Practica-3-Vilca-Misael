import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import numpy as np
import imageio

class pantalla(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)

        # Cargar imagen
        self.cargarImagen.clicked.connect(self.cargarImg)

    
    def cargarImg(self):
        ruta = QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','',"Images (*.png *.bmp)")
        img = imageio.imread(ruta[0])
        mostrarImagen(self,img)


def mostrarImagen(self, rgb):
    rgb = np.clip(rgb, 0, 255)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.imgOriginal.setPixmap(pix)        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pantalla()
    GUI.show()
    sys.exit(app.exec_())