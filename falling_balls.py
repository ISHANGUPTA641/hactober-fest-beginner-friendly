import time
import numpy as np
import cv2
import time
import mediapipe as mp
import random

col = []
no_of_balls = 13
multiplication_factor = 1.65
start_horizontal = [0]*no_of_balls
start_vertical = [0]*no_of_balls
go_sideways = 0
distance_horizontal = [0]*no_of_balls
distance_vertical = [0]*no_of_balls

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (125, 255, 125), (35, 28, 187), (86, 247, 168)]
no_of_colors = len(colors)
color_no = [0]*no_of_balls

g = int(10*multiplication_factor)
ball_in_frame = [False]*no_of_balls
start_after = [0]*no_of_balls

for _4 in range(no_of_balls):
    start_after[_4] = random.randint(0, 10000)

current_time = 0
previous_time = 0
radius = 40

feed = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.6, min_tracking_confidence=0.6)
Draw = mp.solutions.drawing_utils

while 1:
    is_true, frame = feed.read()
    height, width, channels = frame.shape
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    current_time = time.time()
    fps = 1/(current_time-previous_time)
    previous_time = current_time

    for _1 in range(no_of_balls):
        if ball_in_frame[_1]:
            if start_after[_1]>0:
                start_after[_1]-=fps
            else:
                start_after[_1] = 0
                if start_vertical[_1]<=height:
                    start_vertical[_1]+=g
                    start_horizontal[_1] += distance_horizontal[_1]
                else:
                    ball_in_frame[_1] = False
        else:
            start_vertical[_1] = 0
            distance_horizontal[_1] = 0
            start_horizontal[_1] = random.randint(240, 320)
            ball_in_frame[_1] = True
            color_no[_1] = random.randint(0, no_of_colors-1)
            start_after[_1] = random.randint(0, 1000)

    frameBlur = cv2.GaussianBlur(frameRGB, (3, 3), 7)

    result = hands.process(frameBlur)
    if result.multi_hand_landmarks:
        for land_mark in result.multi_hand_landmarks:
            for no, i in enumerate(land_mark.landmark):
                if no==8:
                    col = [int(i.x*width), int(i.y*height)]
            Draw.draw_landmarks(frame, land_mark, mpHands.HAND_CONNECTIONS)
        
        for _3 in range(no_of_balls):
            if np.linalg.norm(np.array(col)-np.array([start_horizontal[_3], start_vertical[_3]]))<=radius:
                distance_horizontal[_3] = start_horizontal[_3] - col[0]

    for _2 in range(no_of_balls):
        if start_after[_2]==0:
            frame = cv2.circle(frame, (start_horizontal[_2], start_vertical[_2]),radius, colors[color_no[_2]], -1)
        if distance_horizontal[_2]!=0:
            distance_horizontal[_2] = distance_horizontal[_2] - distance_horizontal[_2]//5
    
    cv2.imshow('falling balls', frame)
    if cv2.waitKey(20)==27:
        break

feed.release()
cv2.destroyAllWindows()