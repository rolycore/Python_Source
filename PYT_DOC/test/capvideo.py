import cv2
#from os import walk
#import sys
#import time
import numpy as np


# Camara 1 es la camara web integrada en mi caso
camara = 1
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 1
#iniciar camara
camera = cv2.VideoCapture(0)

# Captura imagen  camara
def get_image():
 # leer la captura
 retval, im = camera.read()
 return im
for i in range (fotogramas):
 temp = get_image()
print("Foto tomada")

# entregar imagen leida anteriormente
camera_capture = get_image()
file = "img1.jpg"

# Guardar la imagen con opencv que fue leida por PIL
cv2.imwrite(file, camera_capture)

# muestra la imagen con opencv que fue leida por PIL
cv2.imshow(file, camera_capture)

# finalizar camara
del(camera)
