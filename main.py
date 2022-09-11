import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import numpy as np
import imageio
from funciones import *

class pantalla(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaz.ui", self)

        # Cargar imagen
        self.btn_cargarImagen.clicked.connect(self.cargarImg)

        # Aplicar filtro
        self.btn_aplicarFiltro.clicked.connect(self.aplicarFiltro)

    def cargarImg(self):
        global img
        ruta = QtWidgets.QFileDialog.getOpenFileName(self,'Abrir una imagen','',"Images (*.png *.bmp)")
        img = imageio.imread(ruta[0])[:,:,0:3] #Para tomar cualquier imagen
        mostrarImagen(self,img)

    def aplicarFiltro(self):
        opc = self.combo_filtros.currentText()
        if opc == "Filtro Raíz":
            imgRaiz = filtroRaiz(img)
            mostrarResultado(self,imgRaiz)
        elif opc == "Filtro Cuadrado":
            imgCuad = filtroCuadrado(img)
            mostrarResultado(self,imgCuad)
        elif opc == "Filtro Lineal a Trozos":
            imgLineal = filtroLinealATrozos(img)
            mostrarResultado(self,imgLineal)
    

def mostrarImagen(self, rgb):
    rgb = np.clip(rgb, 0, 255)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.imgOriginal.setPixmap(pix) 

def mostrarResultado(self, rgb):
    rgb = np.clip(rgb, 0, 255)
    h, w, _ = rgb.shape
    im = QtGui.QImage(rgb.astype(np.uint8), w, h, 3 *
                      w, QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(im)
    self.imgConFiltro.setPixmap(pix)        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pantalla()
    GUI.show()
    sys.exit(app.exec_())