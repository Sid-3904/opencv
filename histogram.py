import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('taj.jpg')
cv.imshow('taj', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (400, 700), img.shape[0]//4, (255, 255, 255), -1)
masked_image = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('masked', masked_image)

gray_hist = cv.calcHist([gray], [0], masked_image, [256], [0, 256])
plt.figure()
plt.title('grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0, 256])
plt.plot(gray_hist)
plt.show()

plt.figure()
plt.title('color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)

colors = ('b', 'g', 'r')
for i, col in enumerate(colors) :
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)