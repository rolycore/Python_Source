#import numpy as np
import cv2
from PIL import Image

img = Image.open("15.jpg")


# Define tupla con región
caja = (200, 1900, 3300, 3100)

# Obtener de la imagen original la región de la caja
region = img.crop(caja)  

region.show()  # Mostrar imagen de la region

region.size   # Mostrar tamaño de imagen final 600x400

# Guarda la imagen obtenida con el formato JPEG.
region.save("region13.jpg")

# Guarda la imagen obtenida con el formato PNG.
region.save("region13.png")
