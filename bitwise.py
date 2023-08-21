import cv2 as cv
import numpy as np

blank = np.zeros(img.shape, dtype = 'uint8')
rectangle = cv.rectangle(blank.copy(), (img.shape[1]//5, img.shape[0]//5), (img.shape[1]-img.shape[1]//5, img.shape[1]-img.shape[0]//5), (255, 255, 255), -1)
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 300, (0, 255, 0), -1)

b_and = cv.bitwise_and(rectangle, circle)
cv.imshow('and', b_and)
b_or = cv.bitwise_or(rectangle, circle)
cv.imshow('or', b_or)
b_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', b_xor)
b_not = cv.bitwise_not(circle)
cv.imshow('not', b_not)

cv.waitKey(0)