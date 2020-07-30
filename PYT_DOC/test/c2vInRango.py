import numpy as np
import cv2
from PIL import Image

img = Image.open("15.jpg")


# Define tupla con región
r,h,c,w = 250, 90, 400, 125
track_window = (c,r,w,h)

#
roi = img[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.

