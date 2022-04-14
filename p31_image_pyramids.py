import cv2
import numpy as np
img=cv2.imread('lena.jpg')
lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)
hr1=cv2.pyrUp(lr2)
hr2=cv2.pyrUp(hr1)
cv2.imshow('Original Image',img)
cv2.imshow('pyr_dn Image1',lr1)
cv2.imshow('pyr_dn Image2',lr2)
cv2.imshow('pyr_up Image3',hr1)
cv2.imshow('pyr_up Image4',hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()
