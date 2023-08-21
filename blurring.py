import cv2 as cv
import numpy as np

img = cv.imread('taj.jpg')
cv.imshow('taj', img)

blur1 = cv.blur(img, (5, 5))
cv.imshow('Average blur', blur1)

blur2 = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('gaussian blur', blur2)

blur3 = cv.medianBlur(img, 5)
cv.imshow('median', blur3)

blur4 = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', blur4)

canny1 = cv.Canny(blur2, 125, 175)
cv.imshow('gauss', canny1)

canny2 = cv.Canny(blur4, 125, 175)
cv.imshow('bilat', canny2)

cv.waitKey(0)