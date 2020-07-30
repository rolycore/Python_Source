import cv2
import sys
from resizeimage import resizeimage
from matplotlib import pyplot as plt
from cv2 import resize
from imutils import contours
import numpy as np
import imutils



def _abrir_archivo(dir):
    imagen = cv2.imread(dir)
    if imagen.any() == None:
        print('No se puede abrir imagen')
        sys.exit(1)
    return imagen

def order_points(pts):
    #Inicializar una lista de coordenadas que pueden ser ordenadas
    #como la primera entrada en la lista al lado izquierdo,
    #la segunda entrada está al lado derecho, la tercera es el
    #botón derecho y la cuarta es el botón izquierdo
    rect = np.zeros((4, 2), dtype = 'float32')

    #El punto del top-izquierdo puede tener una pequeña suma, mientras
    #que el punto del botón derecho puede tener una suma muy larga
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    #ahora, estimar la diferencia entre los puntos, el,
    #punto del top-derecho puede tener la diferencia más pequeña,
    #mientras que el botón izquierdo puede tener la diferencia más larga
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[2] = pts[np.argmax(diff)]

    #Retorna la coordenadas ordenadas
    return rect

def four_point_transform(image, pts):
    #Obtener un orden consistente de los puntos y desempacarlos individualmente
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    #Calcule la amplitud de la nueva imagen, cual es la máxima
    #distancia entre el top-derecho y el botón derecho
    # coordenadas-y- o el top-derecho y el top-izquierdo coordenadas-x-
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    #Calcular la altura de la nueva imagen, la cual será la distancia máxima entre
    #el top-derecho y botón-izquierdo coordinadas-y-
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    #Ahora que tenemos las dimenciones de la nueva imagen, construir el conjunto
    #de puntos de destino para obtener una "vista panóramica", (i.e. top-down view)
    #de la imagen, nuevamente especificando los puntos en el top-izquierdo, top-derecho,
    #botón-derecho y botón izquierdo en orden
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    #Calcule la perspectiva de la matrix transformada y apliquela
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))


    #Retorna la imagen girada
    return warped

def prueba():

    DIGITS_LOOKUP = {
        (1, 1, 1, 0, 1, 1, 1): 0,
        (0, 0, 1, 0, 0, 1, 0): 1,
        (1, 0, 1, 1, 1, 1, 0): 2,
        (1, 0, 1, 1, 0, 1, 1): 3,
        (0, 1, 1, 1, 0, 1, 0): 4,
        (1, 1, 0, 1, 0, 1, 1): 5,
        (1, 1, 0, 1, 1, 1, 1): 6,
        (1, 0, 1, 0, 0, 1, 0): 7,
        (1, 1, 1, 1, 1, 1, 1): 8,
        (1, 1, 1, 1, 0, 1, 1): 9}

    imagen = _abrir_archivo('images/2.jpg')
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen2 = cv2.resize(gray, None, fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)


    blurred = cv2.GaussianBlur(gray,(5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200, 255)

    #encontrar contornos en el mapa edge, luego ordenarlos por su tamaño
    #en orden descendente
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = sorted(cnts, key = cv2.contourArea, reverse=True)
    displayCnt = None

    #Loop fuera de contorno
    for c in cnts:
        #aproximando el contorno
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        print(approx)
        #Si el contorno tiene cuatro vértices, entonces
        #hemos encontrado la pantalla del display
        if len(approx) == 4:
            displayCnt = approx
            break

    warped = four_point_transform(imagen2, displayCnt.reshape(4, 2))
    output = four_point_transform(imagen2, displayCnt.reshape(4, 2))

    thresh = cv2.threshold(warped, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
    #thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    digitCnts = []

    #Loop por encima del área elegible
    for c in cnts:
        #Calcular el contorno del borde de la caja
        (x, y, w, h) = cv2.boundingRect(c)
        #Si el contorno es suficientemente largo, debe ser un digito
        #Imprime "x={}  y={}  w={}   h={}".format(x,y,w,h)
        if w >= 10 and (h >= 30 and h <= 90):
            print("x={}     y={}    w={}    h={}".format(x,y,w,h))
            digitCnts.append(c)



        cv2.imshow("Original", imagen2)
        cv2.imshow("Recortado", output)
        cv2.imshow("Ventana2", thresh)

        cv2.waitKey(0)
