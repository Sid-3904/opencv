import cv2 as cv
import numpy as np

img = cv.imread('taj.jpg')
cv.imshow('taj', img)

blank = np.zeros(img.shape, dtype = 'uint8')
circle = cv.circle(blank, (0, 0), 500, (0, 255, 0), -1)

mask1 = cv.bitwise_and(circle, img)
cv.imshow('and', mask1)
mask2 = cv.bitwise_or(circle, img)
cv.imshow('or', mask2)
mask3 = cv.bitwise_xor(circle, img)
cv.imshow('xor', mask3)
mask4 = cv.bitwise_not(img)
cv.imshow('not', mask4)

cv.waitKey(0)