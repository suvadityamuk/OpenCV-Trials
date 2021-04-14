import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_clr = np.array([0,0,0])
    upper_clr = np.array([180,255,150])

    mask = cv2.inRange(hsv, lower_clr, upper_clr)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15,15), np.float32)/225
    smooth = cv2.filter2D(res, -1, kernel)

    gaus = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)
    bil = cv2.bilateralFilter(res, 15, 75, 75)


    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', smooth)
    cv2.imshow('gaus', gaus)
    cv2.imshow('median', median)
    cv2.imshow('bil', bil)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()