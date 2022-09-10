import numpy as np

# Restringe RGB a [0,1]
def normalizarRGB(img):
    return np.clip(img/255,0,1)

# Convierte RGB a YIQ
def RGBtoYIQ(img):
    img = normalizarRGB(img)
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
    I = (0.59590059 * R) + (-0.27455667 * G) + (-0.32134392 * B)
    Q = (0.21153661 * R) + (-0.52273617 * G) + (0.31119955 * B)
    return (Y, I, Q)

# Convierte YIQ a RGB
def YIQtoRGB(Y,I,Q):
    r = (Y+0.9563*I+0.621*Q)
    g = (Y-0.2721*I-0.6474*Q)
    b = (Y-1.1070*I+1.7046*Q)

    img = np.zeros((np.shape(Y)[0], np.shape(Y)[1], 3))
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return np.clip(img,0,1)

# Devuelve la luminancia Y de una imagen en YIQ
def obtenerLuminancia(img):
    img = normalizarRGB(img)
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]
    return (0.299 * R) + (0.587 * G) + (0.114 * B)

def filtroRaiz(Y):
    return np.clip(np.sqrt(Y),0,1)

def filtroCuadrado(Y):
    return np.clip(np.square(Y),0,1)

