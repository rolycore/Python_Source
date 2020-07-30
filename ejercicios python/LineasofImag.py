import numpy as np
import cv2

origm = cv2.imread('images/tacomp14.png')
cv2.imshow('origm9', origm)

#Colocar en Gris
gris = cv2.cvtColor(origm, cv2.COLOR_BGR2GRAY)
cv2.imshow('origm6', gris)

#uso de Gaussiano
gauss = cv2.GaussianBlur(gris, (5,5), 0)
cv2.imshow('origm7', gauss)



#Uso de Canny para calcular el detector de bordes

canny = cv2.Canny(gauss, 50, 150)
cv2.imshow('origm8', canny)
#hasta este punto se ejecuta correctamente

