#%%
import numpy as np
import imageio
import matplotlib.pyplot as plt
from funciones import *
#%%
img = imageio.imread("astronaut.png")
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

