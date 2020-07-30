import numpy as np
import cv2

origm = cv2.imread('images/tac_3.jpg')
cv2.imshow('origm14', origm)

#Colocar en Gris
gris = cv2.cvtColor(origm, cv2.COLOR_BGR2GRAY)
cv2.imshow('origm15', gris)

#uso de Gaussiano
gauss = cv2.GaussianBlur(gris, (3,3), 0)
cv2.imshow('origm16', gauss)


#Uso de Canny para calcular el detector de bordes

canny = cv2.Canny(gauss, 50, 150)
cv2.imshow('origm17', canny)
#hasta este punto se ejecuta correctamente

