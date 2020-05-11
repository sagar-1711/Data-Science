#looks for features on the face using classifier model (pretrained model)
#code for reading a video stream from Camera(frame by frame)
import cv2
cap=cv2.VideoCapture(0)
#creating classifier
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
while True:
    ret,frame=cap.read()
    if ret==False:
        continue
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray_frame,1.3,5) #(,scaling factor,number of neighbours) image gets shrinked by scaling factor . 1.3 means at each pass image will shrink by 30% 
    #no of neighbours specifies how many neighbours each rectangle should have ,higher values results in less detection but with higher quality 3-6 is a good value
    #in faces we will get coordinates(x,y1,width,height) of face, if multiple faces are present it would return list of tuples so we will iterate throuh tuple and create boundary wall around each face

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
    cv2.imshow("Video Frame",frame)
    #wait for user input -q, then you will stop the loop
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    