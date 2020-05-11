import cv2
img=cv2.imread('dog.jpg')
gray=cv2.imread('dog.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Mountain Image',img)
cv2.imshow('Gray Mountain Image',gray)
cv2.waitKey(0) #0 means wait for infinite time if cv2.waitkey(25) means close after 25ms will exit if any key is pressed
cv2.destroyAllWindows()



