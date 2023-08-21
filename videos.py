import cv2 as cv

video = cv.VideoCapture('dog.mp4')

def rescaleFrame(frame, scale = 1.0) :
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height) :
    video.set(3, width)
    video.set(4, height)

def play(video, scale) :
    while True:
        isTrue, frame = video.read()
        frame_resized = rescaleFrame(frame, scale)
        if isTrue :
            cv.imshow('video', frame)
            cv.imshow('video resized', frame_resized)
            if cv.waitKey(20) & 0xFF == ord('d') :
                break
        else :
            break

play(video, 0.5)

video.release()
cv.destroyAllWindows()