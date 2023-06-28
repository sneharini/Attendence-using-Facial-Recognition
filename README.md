# Attendence-using-Facial-Recognition using opencv library in python
IDE USED = Pycharm + Visual studio for c++ desktop development
DEPENDENCIES = cmake, dilib, face_recognition,Numpy,Opencv
The proposed system will reduce the paperwork where attendance will no longer involve any manual recording. The new system will also reduce the total time needed to do attendance recording. 

The new system will acquire individual attendance by means of facial recognition to secure data accuracy of the attendance 

An attendance system using facial recognition and sending messages through WhatsApp can be implemented using a combination of hardware and software components. Here's a high-level overview of how you can build such a system:

Hardware Components:

Camera: A camera capable of capturing facial images.
Computer or Raspberry Pi: A computer or Raspberry Pi board to process the facial images and run the software.
Software Components:

Facial Recognition Algorithm: Use a facial recognition algorithm or library (such as OpenCV or DLib) to detect and recognize faces from the captured images.
Face Database: Maintain a database of registered faces for comparison during recognition.
Attendance Tracking System: Develop an attendance tracking system to keep a record of attendance data.
WhatsApp API: Utilize the WhatsApp Business API to send messages to registered users.
System Workflow:

Enrollment:

Capture facial images of individuals to be enrolled in the system.
Store the facial features or representations of these individuals in the face database.
Attendance Marking:

Continuously capture images using the camera.
Apply the facial recognition algorithm to detect and recognize faces in real-time.
Compare the recognized faces with the face database to identify registered individuals.
If a match is found, mark the attendance for that individual in the attendance tracking system.
Sending Messages via WhatsApp:

Integrate the WhatsApp API with your system.
When attendance is marked, trigger a message sending mechanism.
Use the WhatsApp API to send customized messages to registered individuals, informing them about their attendance status.
It's important to note that building such a system involves detailed implementation and integration steps, and it may require expertise in computer vision, software development, and system integration. Additionally, ensure that you comply with legal and privacy regulations related to facial recognition and data handling in your jurisdiction.




                   ############## WORKING STEPS #################
STEP 1:  A set of data needed to be inputted into system which consists of individual’s name and their photos
STEP 2:  Portrait acquisition can be done by using the camera to capture the faces of the individual
STEP 3:  The system will first detect the presence of a face in the captured image in the webcam
STEP 4:  Then image will undergo several pre-processing procedures to obtain a grayscale image cropped faces of equal sized image
STEP 5:  The processed image will compare with the set of images which is already collected from the students
STEP 6:  With the help of the neural network, it will check for the maximum matched facial features
STEP 7:  If a face is matched, the responding name with PRESENT status is marked in aEXCEL file with the current date and time. 
STEP 8: You can also send the EXCEL sheet to your mail.


