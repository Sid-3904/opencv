import cv2 as cv
import numpy as np

img = cv.imread('taj.jpg')
cv.imshow('taj', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

canny = cv.Canny(gray, 125, 175)
cv.imshow('canny', canny)

laplacian = cv.Laplacian(gray, cv.CV_64F)
cv.imshow('laplacian', laplacian)

sobel_X = cv.Sobel(gray, cv.CV_64F, 1, 0)
cv.imshow('sobel x', sobel_X)

sobel_Y = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('sobel y', sobel_Y)

combined_sobel = cv.bitwise_or(sobel_X, sobel_Y)
cv.imshow('sobel full', combined_sobel)

cv.waitKey(0)