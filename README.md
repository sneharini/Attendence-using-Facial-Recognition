# Attendence-using-Facial-Recognition using opencv library in python
IDE USED = Pycharm + Visual studio for c++ desktop development
DEPENDENCIES = cmake, dilib, face_recognition,Numpy,Opencv
                   ############## WORKING STEPS #################
STEP 1:  A set of data needed to be inputted into system which consists of individual’s name and their photos
STEP 2:  Portrait acquisition can be done by using the camera to capture the faces of the individual
STEP 3:  The system will first detect the presence of a face in the captured image in the webcam
STEP 4:  Then image will undergo several pre-processing procedures to obtain a grayscale image cropped faces of equal sized image
STEP 5:  The processed image will compare with the set of images which is already collected from the students
STEP 6:  With the help of the neural network, it will check for the maximum matched facial features
STEP 7:  If a face is matched, the responding name with PRESENT status is marked in aEXCEL file with the current date and time. 
STEP 8: You can also send the EXCEL sheet to your mail.


