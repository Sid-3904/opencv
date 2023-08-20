import cv2 as cv
import numpy as np

draw = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('blank', draw)

cv.rectangle(draw, (0, 0), (draw.shape[1]//2, draw.shape[0]//2), (0, 255, 0), -1)
cv.imshow('rectangle', draw)

cv.circle(draw, (250, 250), 50, (255, 0, 0), 2)
cv.imshow('circle', draw)

cv.line(draw, (0, 0), (250, 100), (0, 255, 255), 2)
cv.imshow('line', draw)

cv.putText(draw, 'hello world', (100, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow('text', draw)

cv.waitKey(0)
