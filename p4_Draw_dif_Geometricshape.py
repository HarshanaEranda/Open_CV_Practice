import numpy as np
import cv2
# Read the given location image
# img = cv2.imread('lena.jpg',-1) #(-1,0,1)
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,255),(255,255),(0,0,255),5)#draw a line ,3rd argument is color ,That shoud be BGR format
img=cv2.arrowedLine(img,(0,0),(255,255),(0,0,255),5) # Draw a arrow line
img=cv2.rectangle(img,(0,0),(255,255),(0,0,255),5) # draw a rectrangle ,1st coodinate is the top let and second coodinate is lower right coodinate
#-1 of the thickness is fill the rectrangle
img=cv2.circle(img,(255,255),100,(0,255,0),5) # draw a circle
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
img=cv2.putText(img,"OPENCV",(10,500),font,4,(255,5,0),3,cv2.LINE_AA)
# show the image
cv2.imshow('image',img)
# waiting time of the image
cv2.waitKey(0)
cv2.destroyAllWindows()
