#import numpy as np
import cv2
from PIL import Image

img = Image.open("15.jpg")
#cv2.imshow('image',img)

#Obtiene el tamaño total de una image
print(img.size)
#el resultado muestra que el tamaño de esta imagen-captura2.png es de 921600

#ahora escogere otra imagen la 15.jpg el tamaño de esta es de 38340864


#Obtener una imagen de tamaño indicado

reducida = img.resize((400, 900))
reducida.show()

reducida.save("reducida.jpg")

#cv2.imwrite(reducida, "reducida.jpg")
#cv2.imshow('image',reducida)
