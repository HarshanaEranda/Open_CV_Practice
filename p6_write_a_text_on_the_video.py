import cv2
import datetime
cap=cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # print the width of the frame
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # print the height of the frame
# cap.set(3,10000) #change the width of the video
# cap.set(4,700) #change the height of the video
# print(cap.get(3))
# print(cap.get(4))
while (cap.isOpened()):
    ret,frame = cap.read() # return true will frame available
    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='width: '+str(cap.get(3)) + ' Height: '+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame= cv2.putText(frame,text,(10,50),font,1,
                           (0,255,255),2,cv2.LINE_AA) #show the width and height of the video
        frame = cv2.putText(frame, datet, (40, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA) # show the current date and time one the video
        cv2.imshow('frame', frame)
        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
