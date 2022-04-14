import cv2
cap=cv2.VideoCapture(0);
print(cap.isOpened())# return the boolean value when video is on or not

fourcc=cv2.VideoWriter_fourcc('X','V','I','D') # or *'XVID'
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #second argument is the FourCC code //fourcc.org/codecs.php
# while(True):
while (cap.isOpened()):
    ret,frame = cap.read() # return true will frame available
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # print the width of the frame
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # print the height of the frame
        out.write(frame) # video will save without gray color
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # gives the gray scale image
        #out.write(frame)  # video will save with gray color
        cv2.imshow('frame', gray)
        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
