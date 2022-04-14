import numpy as np
import cv2

img=cv2.imread('opencv-logo.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Image',img)
cv2.imshow('Image_gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()