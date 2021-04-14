import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('breitling2.jpg', cv2.IMREAD_COLOR)
img[55,55] = [255,255,255] #img pixel color can be changed using this
px = img[55,55] #color of the pixel
#379,145
#616,449

img[100:150, 100:150] = [255,255,255]#changes color of the pixels in lhs regions to rhs color value(bgr)

roi = img[100:150, 100:150] #to define the 'region of image'
print(roi) #returns the colour values of the pixels in the roi in bgr value format

watch_face = img[379:616, 145:449]  #selects roi 
img[0:183, 0:304] = watch_face #imposes roi watch_face on pixels selected 

# plt.imshow(img, cmap='rainbow_r')
# plt.show()
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()