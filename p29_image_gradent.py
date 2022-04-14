import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
laplacian=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
laplacian=np.uint8(np.absolute(laplacian))

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))
sobel_Combine=cv2.bitwise_or(sobelx,sobely)


title=['image','laplacian','SobelX','SobelY','Sobel_Com']
images=[img,laplacian,sobelx,sobely,sobel_Combine]
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()