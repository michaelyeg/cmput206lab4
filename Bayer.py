import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


# part I

img = cv2.imread('PeppersBayerGray.bmp', 0)

h,w = img.shape

# our final image will be a 3 dimentional image with 3 channels
rgb = np.zeros((h,w,3),np.uint8);


# reconstruction of the green channel IG

IG = np.copy(img) # copy the image into each channel

for row in range(0,h,4): # loop step is 4 since our mask size is 4.
    for col in range(0,w,4): # loop step is 4 since our mask size is 4.
        
        IG[row,col+1]=(int(img[row,col])+int(img[row,col+2]))/2
        ...
        IG[row+3,col]= (int(img[row+2,col])+int(img[row+3,col+1]))/2
        ...

# reconstruction of the red channel IR


# reconstruction of the blue channel IB



# merge the channels
rgb[:,:,0]=IR
...


cv2.imwrite('rgb.jpg',rgb);

plt.imshow(rgb),plt.title('rgb')
plt.show()


# part II should be written here:
