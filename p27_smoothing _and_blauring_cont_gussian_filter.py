
import cv2
import  numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Noise_salt_and_pepper.png')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.float32)/ 25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gussian_blur=cv2.GaussianBlur(img,(5,5),0) # remove the high frequency noise from the image
median=cv2.medianBlur(img,5)#kernal size(ksize) must be odd value

titles=['image', '2D_convolution', 'Blur','gussian_blur','median']
images=[img, dst, blur, gussian_blur,median]


for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()