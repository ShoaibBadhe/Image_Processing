import cv2 as cv
import numpy as np

image1 = cv.imread('new.jpg')
image2 = cv.imread('new2.jpg')

diff = cv.subtract(image1,image2)

result = not np.any(diff)

if result is True:
    print('theimages_are_the_same')
else:
    print('the images are diff')
