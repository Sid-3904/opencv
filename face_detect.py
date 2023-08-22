import cv2 as cv
import numpy as np

img = cv.imread('photos\group 1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haarcascade.xml')

face_recogniser = haar_cascade.detectMultiScale(gray, 1.1, 1)
print(f'{len(face_recogniser)} faces found')

for (x, y, w, h) in face_recogniser:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('person', img)
cv.waitKey(0)