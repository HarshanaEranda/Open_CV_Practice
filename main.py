import cv2
# Read the given location image
img = cv2.imread('lena.jpg',-1) #(-1,0,1)
print(img)
# show the image
cv2.imshow('image',img)
# waiting time of the image
cv2.waitKey(5000)
cv2.destroyAllWindows()
# Write the image in the file
cv2.imwrite('lena_copy.png',img)