import cv2 as cv

img = cv.imread('taj.jpg')
cv.imshow('Taj', img)

cv.waitKey(0)

video = cv.VideoCapture('dog.mp4')

while True :
    isTrue, frame = video.read()
    if isTrue :
        cv.imshow('video', frame)
        if cv.waitKey(20) & 0xFF == ord('d') :
            break
    else :
        break
video.release()
cv.destroyAllWindows()