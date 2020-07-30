#import numpy as np
import cv2
from PIL import Image

img = Image.open("15.jpg")


# Define tupla con región
caja = (100, 1800, 3500, 3100)

# Obtener de la imagen original la región de la caja
region = img.crop(caja)  

region.show()  # Mostrar imagen de la region

region.size   # Mostrar tamaño de imagen final 600x400

# Guarda la imagen obtenida con el formato JPEG.
region.save("region12.jpg")

# Guarda la imagen obtenida con el formato PNG.
region.save("region12.png")
