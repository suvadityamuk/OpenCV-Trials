import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('bookpage.jpg', cv2.IMREAD_COLOR)
retval, thr = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, thr2 = cv2.threshold(greyscaled, 10, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3, otsu = cv2.threshold(greyscaled, 125, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY)

#otsu = cv2.threshold(greyscaled, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('Original', img)
cv2.imshow('Threshold', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()