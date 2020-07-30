import cv2
import numpy as np

image = cv2.imread('15.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(0)
 
#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('second', thresh)
cv2.waitKey(0)
 
#dilation
kernel = np.ones((1,1), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated', img_dilation)
cv2.waitKey(0)


#showCrosshair = False
#fromCenter = False
r = cv2.selectROI(image)

imCrop = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

showCrosshair = False
fromCenter = True
r = cv2.selectROI(gray, fromCenter, showCrosshair)


# Specify a vector of rectangles (ROI) 
rects = []
fromCenter = false
# Select multiple rectangles
selectROI("Image", r, rects, fromCenter)




#im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#x,y,w,h = cv2.boundingRect(ctrs)

#roi = image[y:y+h, x:x+w]

#cv2.rectangle(image,(x,y),(c + w, y + h),(0,255,0),2)
    

#roi = image[300:700, 310:520]

cv2.imshow('roi', imCrop)
cv2.imshow('original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
