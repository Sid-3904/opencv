import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('taj.jpg')
cv.imshow('taj', img)

# mpltimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', mpltimg)

# plt.imshow(mpltimg)
# plt.show()

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

img2 = cv.merge([b, g, r])
cv.imshow('img merge', img2)

cv.waitKey(0)