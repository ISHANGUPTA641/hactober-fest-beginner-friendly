import cv2
import time
feed = cv2.VideoCapture(0)
tracker = cv2.legacy.TrackerCSRT_create()
success, frame = feed.read()
frame = cv2.bilateralFilter(frame, 5,15, 15)
boundingBox = cv2.selectROI('Tracking', frame, False)
tracker.init(frame, boundingBox)
previousTime = 0
while True:
    success, frame = feed.read()
    frame = cv2.flip(frame, 1)
    success, boundingBox = tracker.update(cv2.bilateralFilter(frame, 5, 15, 15))
    if success:
        frame = cv2.rectangle(frame, (int(boundingBox[0]), int(boundingBox[1])), (int(boundingBox[0]+boundingBox[2]), int(boundingBox[1]+boundingBox[3])), (255, 0, 0), )
    else:
        frame = cv2.putText(frame, f'LOST!', (200, 300), cv2.FONT_ITALIC, 3, (0, 255, 255), 2)
    currentTime = time.time()
    fps = int(1/(currentTime-previousTime))
    previousTime = currentTime
    frame = cv2.putText(frame, f'FPS:{str(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 255), 2)
    cv2.imshow('Raw Image', frame)
    if cv2.waitKey(1)==27:
        break
feed.release()
cv2.destroyAllWindows()