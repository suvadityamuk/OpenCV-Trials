import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('breitling.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (300,300), (255,255,255), 5)
cv2.rectangle(img, (14,154), (460,587), (255,0,0), 5)
cv2.circle(img, (255,255), 80, (255,255,0), 5)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,0,0))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV Trial", (75,300), font, 1, (255,0,0), 2, cv2.LINE_AA)

# plt.imshow(img, cmap="gray")
# plt.show()
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
