#read a video stream from camera(frame by frame)
import cv2
#capture the device from which you want to capture video . 0 for our device webcam
cap = cv2.VideoCapture(0)

while True:

    success,frame = cap.read() 
    #success is boolean value if false then it means the frame is not captured properly due to mumtiple reasons
    
    if not success:
        continue
    #to have gray video as well
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video Frame",frame)
    cv2.imshow("GRAY Frame",gray_frame)
    #wait for user input-q,then you will stop
    key_pressed=cv2.waitKey(1) & 0xFF #program will wait for 1ms before next iteration
    #cv2.waitKey() gives 32 bit integer so we convert it int 8 bit numberby doing and with 0xFF
    if key_pressed==ord('q'): # ord gives ASCII value between 0-255 which is a 8 bit integer
        break
#release the device
cap.release()
cv2.destroyAllWindows()