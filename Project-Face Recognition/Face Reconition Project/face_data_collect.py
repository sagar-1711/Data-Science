# Write a Python Script that captures images from your webcam video stream
# Extracts all Faces from the image frame (using haarcascades)
# Stores the Face information into numpy arrays

# 1. Read and show video stream, capture images
# 2. Detect Faces and show bounding box (haarcascade)
# 3. Flatten the largest face image(gray scale) and save in a numpy array
# 4. Repeat the above for multiple people to generate training data


import cv2
import numpy as np


#initialize camera
cap=cv2.VideoCapture(0)
skip=0
face_data=[]
dataset_path='./data/'
file_name=input("Enter the name of the person = ")
#Face Detection
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

while True:
    ret,frame=cap.read()
    if ret==False:
        continue
    #we will store gray image to reduce space
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #we will sort thr face values based on area of face(area=w*h)
    
    faces=face_cascade.detectMultiScale(frame,1.3,5)
    faces=sorted(faces,key=lambda f:f[2]*f[3])
    #pick the last face because it is the largest face according to area
    for face in faces[-1:]:
        
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        #crop out the required face(bigger face) : Region of Iterest
        offset=10 #to add padding of 10 in all directions #frame is of the form(y,x)
        face_section=frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section=cv2.resize(face_section,(100,100))
        #Store every 10th face
        skip+=1
        if skip%10==0:
            #Store the 10th face
            face_data.append(face_section)
            print(len(face_data))
       
    cv2.imshow("Frame",frame)
    cv2.imshow("Face Section",face_section)
   
    
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed==ord('q'):
        break
#convert face_data array into numpy array
face_data=np.asarray(face_data)
face_data=face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

#save this data into file system
np.save(dataset_path+file_name+'.npy',face_data)
print("Data Successfully save at "+dataset_path+file_name+'.npy')
cap.release()
cv2.destroyAllWindows()
