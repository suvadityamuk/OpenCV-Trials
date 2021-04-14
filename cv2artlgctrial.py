import numpy as np
import cv2

img1 = cv2.imread('plt1.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('plt2.png', cv2.IMREAD_COLOR)

add1 = img1+img2 #adding both images together like this maintains opaqueness of both, leading to possible problems
add2 = cv2.add(img1, img2) # similar to if the color value of a pixel in img1 was (a,b,c) and img2 was (d,e,f), 
#it would give (a+d, b+e, c+f)


weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)



cv2.imshow('Addition', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()