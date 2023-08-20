import cv2 as cv
import numpy as np

img = cv.imread('taj.jpg')
cv.imshow('taj', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blurred = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blurred', blurred)

canny = cv.Canny(blurred, 125, 175)
cv.imshow('edges', canny)

contours, heirachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

blank = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('contours', blank)

ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

cv.waitKey(0)