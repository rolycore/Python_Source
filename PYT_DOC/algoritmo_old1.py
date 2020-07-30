import cv2
import sys
import time
from os import walk

def _abrir_archivo(dir):
    imagen = cv2.imread(dir)
    if imagen == None:
        print "No se puede abrir imagen"
        sys.exit(1)
    return imagen

def prueba():

    imagen = _abrir_archivo("images/1.jpg")
    cv2.imshow("ventana", imagen)
    cv2.waitKey(0)
