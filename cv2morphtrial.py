import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_clr = np.array([150,150,50])
    upper_clr = np.array([180,255,150])

    mask = cv2.inRange(hsv, lower_clr, upper_clr)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5,5), np.uint8)

    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

    tophat = cv2.morphologyEx(res, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(res, cv2.MORPH_BLACKHAT, kernel)


    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
