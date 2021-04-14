import cv2
import numpy as np

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID')
saver = cv2.VideoWriter('Output.avi', codec, 20.0, (640,480))
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    saver.write(frame)
    cv2.imshow('Video', frame)
    cv2.imshow('VideoGray', gray)
    

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
saver.release()
cv2.destroyAllWindows()