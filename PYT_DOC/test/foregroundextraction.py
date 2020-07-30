import numpy as np
import cv2
from matplotlib import pyplot as plt



imag = cv2.imread('images/33.jpg')
gray = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#bgdModel = np.zeros((1,65),np.float64)
#fgdModel = np.zeros((1,65),np.float64)

#rect = (161,79,150,150)
#cv2.grabCut(imag,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

#mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#imag = imag*mask2[:,:,np.newaxis]

#plt.imshow(imag)
#plt.colorbar()
#plt.show()
