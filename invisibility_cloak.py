import time
import cv2 
import numpy as np

feed = cv2.VideoCapture(0)
time.sleep(3)
ret_true, background = feed.read()
background = cv2.flip(background, 1)
while(1):
    ret_true, frame = feed.read()
    frame = cv2.flip(frame, 1)
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([109, 55, 69])
    upper = np.array([137, 255, 205])
    mask = cv2.inRange(frame_hsv, lower,upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2)
    res1 = cv2.bitwise_and(background,background,mask=mask)
    res2 = cv2.bitwise_and(frame,frame,mask=cv2.bitwise_not(mask))
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow('Invisible Cloak',final_output)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
feed.release()
cv2.destroyAllWindows()