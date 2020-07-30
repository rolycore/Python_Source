# import the necessary packages
from imutils import face_utils
#from dlib1 import *
#import dlib1
#from dlib1 import tools
#from dlib1 import src
import cv2

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
#detector = dlib.get_frontal_face_detector()
predictor = src.shape_predictor(p)

# load the input image and convert it to grayscale
imagent = cv2.imread("example.jpg")
gray = cv2.cvtColor(imagent, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale image
rects = detector(gray, 0)

# loop over the face detections
for (i, rect) in enumerate(rects):
	# determine the facial landmarks for the face region, then
	# convert the facial landmark (x, y)-coordinates to a NumPy
	# array
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
	for (x, y) in shape:
		cv2.circle(imagent, (x, y), 2, (0, 255, 0), -1)

# show the output image with the face detections + facial landmarks
cv2.imshow("Outputexamp", imagent)
cv2.waitKey(0)
