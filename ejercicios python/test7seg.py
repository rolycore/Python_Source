# -*- coding: utf-8 -*-
import cv2
from PIL import Image
import numpy as np
import tkinter

"""
 7 segments indexes are:
 0: top,
 1: top left,
 2: top right,
 3: middle,
 4: bottom left
 5: bottom right
 6: bottom
"""
segments = {
    (1, 1, 1, 0, 1, 1, 1): 0,
    (0, 0, 1, 0, 0, 1, 0): 1,
    (1, 0, 1, 1, 1, 1, 0): 2,
    (1, 0, 1, 1, 0, 1, 1): 3,
    (0, 1, 1, 1, 0, 1, 0): 4,
    (1, 1, 0, 1, 0, 1, 1): 5,
    (1, 1, 0, 1, 1, 1, 1): 6,
    (1, 0, 1, 0, 0, 1, 0): 7,
    (1, 1, 1, 1, 1, 1, 1): 8,
    (1, 1, 1, 1, 0, 1, 1): 9
}


def cv2_2_pil(cv2img, transform=cv2.COLOR_BGR2RGB):
    return Image.fromarray(cv2.cvtColor(cv2img, transform))


def get_digit(img):
    segment_pos = [(12, 3), (3, 14), (26, 14), (11, 26), (2, 38), (24, 39), (8, 50)]
    active = map(lambda x: int(np.count_nonzero(get_dig_sub(img, x[0], x[1], 4, 4)) > 8), segment_pos)

    return segments.get(tuple(active), 'x')


def get_dig_sub(img, x, y, width=36, height=60):
    return img[y:y + height, x:x + width]


def min_image_to_temp(img):

    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, imthresh = cv2.threshold(imgray, 50, 255, cv2.THRESH_BINARY_INV)
    imthresh = cv2.dilate(imthresh, np.ones((2, 2), np.uint8), iterations=1)
    #cv2_2_pil(imthresh, cv2.COLOR_GRAY2RGB).show()
    dig1 = get_dig_sub(imthresh, 290, 264)
    dig2 = get_dig_sub(imthresh, 329, 264)
    dig3 = get_dig_sub(imthresh, 367, 264)
    return "{}{}.{}°C".format(*map(get_digit, [dig1, dig2, dig3]))


if __name__ == "__main__":
    image = cv2.imread('15.jpg')
    print(min_image_to_temp(image))
