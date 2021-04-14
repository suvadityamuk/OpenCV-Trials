import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('breitling.jpg', cv2.IMREAD_GRAYSCALE)

#With CV2
# cv2.imshow('Breitling', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#OR 

#With Matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()