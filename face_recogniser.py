import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

DIR = r'C:/Users/Siddharth/Desktop/sid/ml models/opencv/faces/train'
haar_cascade = cv.CascadeClassifier('haarcascade.xml')

features, labels = [], []

def face_train() :
    for person in people :
        path = os.path.join(DIR, person)
        label = people.index(person)
        for img in os.listdir(path) :
            img_path = os.path.join(path ,img)
            img_array = cv.imread(img_pathpath)
            if img_array is None :
                continue
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)
            for (x, y, w, h) in face_rect :
                img_roi = img[y:y+h, x:x+w]
                features.append(img_roi)
                labels.append(label)

face_train()
features = np.array(features, 'object')
labels = np.array(labels)

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.train(features, labels)
face_recogniser.save('face_trained.yml')
np.save('featues.npy', features)
np.save('labels.npy', labels)