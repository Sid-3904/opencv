import cv2 as cv
import numpy as np

img = cv.imread('taj.jpg')
cv.imshow('Taj', img)
 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('blurred', blur)

edges = cv.Canny(blur, 125 ,175)
cv.imshow('cascade', edges)

dilated = cv.dilate(edges, (3 ,3), iterations = 3)
cv.imshow('dilated', dilated)

eroded = cv.erode(dilated, (3, 3), iterations = 3)
cv.imshow('eroded', eroded)

resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

cropped = img[:img.shape[1]//2, :img.shape[0]//2]
cv.imshow('cropped', cropped)

cv.waitKey(0)