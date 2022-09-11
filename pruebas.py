#%%
import numpy as np
import imageio
import matplotlib.pyplot as plt
from funciones import *
#%%
#img = imageio.imread("astronaut.png")
img = imageio.imread('D:/CURSADA FACULTAD 2022/PROCESAMIENTO DE IMAGENES/Tema 4/Practica 3/coffee.png')
Y,I,Q = RGBtoYIQ(img)
img2 = YIQtoRGB(Y,I,Q)
plt.imshow(img)
plt.show()
Y_mod = filtroRaiz(Y)

img3 = YIQtoRGB(Y_mod,I,Q)
plt.imshow(img3)
plt.show()

Y_mod = filtroCuadrado(Y)
img4 = YIQtoRGB(Y_mod,I,Q)
plt.imshow(img3)
plt.show()

#%%
a = np.array([1,2,3,4,5,6,7,8])
minimo = 3
maximo = 6
b[Y<minimo] = 0
b[Y>maximo] = 1
b = np.where((a>=minimo)&(a<=maximo), 1/(maximo-minimo)*(a-minimo),a)

print(b)

#%%
c = np.zeros(a.shape)
print(c)