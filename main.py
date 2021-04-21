import cv2
import numpy as np
import face_recognition

kamal_images = face_recognition.load_image_file('kamal_images/images1.jpg')
kamal_images = cv2.cvtColor(kamal_images,cv2.COLOR_BGR2RGB)

imgtest = face_recognition.load_image_file('kamal_images/images3.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(kamal_images)[0]
encodekamal = face_recognition.face_encodings(kamal_images)[0]
cv2.rectangle(kamal_images,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

faceloctest = face_recognition.face_locations(imgtest)[0]
encodetest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodekamal],encodetest)
faceDis = face_recognition.face_distance([encodekamal],encodetest)
print(results,faceDis)

cv2.putText(imgtest,f'{results} {round(faceDis[0])}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)





cv2.imshow('Kamal',kamal_images)
cv2.imshow('Kamaltest',imgtest)
cv2.waitKey(0)
