import numpy as np
import cv2

origm = cv2.imread('images/tac_3.jpg')
cv2.imshow('origm30', origm)

#Colocar en Gris
gris = cv2.cvtColor(origm, cv2.COLOR_BGR2GRAY)
cv2.imshow('origm31', gris)

#uso de Gaussiano
gauss = cv2.GaussianBlur(gris, (1,1), 0)
cv2.imshow('origm32', gauss)


#Uso de Canny para calcular el detector de bordes

canny = cv2.Canny(gauss, 50, 150)
cv2.imshow('origm33', canny)
#hasta este punto se ejecuta correctamente


#decidir cuales son los contornos que deseamos

(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#mostrar
print('Lo encontrado es {} object'.format(len(contornos)))

cv2.drawContours(origm,contornos,-1,(0,255,0), 3)
cv2.imshow('contornos4', origm)
#hasta este punto se ejecuta correctamente

cv2.waitKey(0)

