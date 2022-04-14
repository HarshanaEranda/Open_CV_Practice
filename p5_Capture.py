import cv2
cap=cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # print the width of the frame
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # print the height of the frame
cap.set(3,10000) #change the width of the video
cap.set(4,700) #change the height of the video
print(cap.get(3))
print(cap.get(4))
while (cap.isOpened()):
    ret,frame = cap.read() # return true will frame available
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # gives the gray scale image
        #out.write(frame)  # video will save with gray color
        cv2.imshow('frame', gray)
        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
