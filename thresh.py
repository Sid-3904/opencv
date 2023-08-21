import cv2 as cv

img = cv.imread('taj.jpg')
cv.imshow('taj', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded', thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 15, 5)
cv.imshow('adaptive threshold', adaptive_thresh)

cv.waitKey(0)