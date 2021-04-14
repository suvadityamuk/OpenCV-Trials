import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    lap = cv2.Laplacian(frame, cv2.CV_64F)  #for laplacian image filtering
    sobx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)  #for sobel-x direction image filtering  
    soby = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)  #for sobel-y direction image filtering
    edge = cv2.Canny(frame, 100, 200) #applies canny algorithm to achieve edge direction

    cv2.imshow('Default', frame)
    cv2.imshow('Laplacian', lap)
    # cv2.imshow('Sobel X', sobx)
    # cv2.imshow('Sobel Y', soby)
    cv2.imshow('Edge', edge)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
