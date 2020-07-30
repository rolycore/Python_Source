import cv2
import numpy as np

img1 = cv2.imread('image/tac_3.jpg',0)
img2 = cv2.imread('image/1.jpg',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,4,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,4,1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print('ret', ret)
