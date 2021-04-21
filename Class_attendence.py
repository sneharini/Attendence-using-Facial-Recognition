import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'Image_attendence'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markAttendence(name):
    with open('Attendence.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')






encodelistKnown = findEncodings(images)
print("Encoding completed")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceloc in zip(encodeCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodelistKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodelistKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:

            name = classNames[matchIndex].capitalize()
            #print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2+6),cv2.FONT_ITALIC,1,(255,255,255),2)
            markAttendence(name)


            
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)



#faceloc = face_recognition.face_locations(kamal_images)[0]
#encodekamal = face_recognition.face_encodings(kamal_images)[0]
#cv2.rectangle(kamal_images,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

#faceloctest = face_recognition.face_locations(imgtest)[0]
#encodetest = face_recognition.face_encodings(imgtest)[0]
#cv2.rectangle(imgtest,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),2)

#results = face_recognition.compare_faces([encodekamal],encodetest)
#faceDis = face_recognition.face_distance([encodekamal],encodetest)
#print(results,faceDis)

#cv2.putText(imgtest,f'{results} {round(faceDis[0])}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


