import cv2
import mediapipe as mp
import time
import numpy as np
feed = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.6, min_tracking_confidence=0.6)
Draw = mp.solutions.drawing_utils
current_time = 0
previous_time = 0
Points = []
Drawing_pts = []
previous_draw=True
current_draw=True
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color_no = 0
shape = 0
current_shape = False
previous_shape = False
eraser = False
start_corner = []
end_corner = []
start_line = []
end_line = []
radius = 0
centre = []

def getLine(x1,y1,x2,y2):
    if x1==x2:
        if y1!=y2:
            return [(x1,i) for i in range(y1,y2,int(abs(y2-y1)/(y2-y1)))]
    else:
        if x1>x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        slope=(y2-y1)/(x2-x1)
        line=[]
        i=0
        while x1+i < x2:
            i+=1
            line.append((int(x1+i),int(y1+slope*i)))
        return line

def assign0(a, b, shape0):
    if not b:
        if a!=shape0:
            return shape0
        else:
            return 0
    else:
        return a

def Draw_boxes_2(frame):
    frame = cv2.rectangle(frame, (550, 25), (630, 75), (122, 122, 122), -1)
    frame = cv2.putText(frame, 'CLEAR', (555, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    frame = cv2.rectangle(frame, (550, 75), (630, 125), colors[0], -1)
    frame = cv2.putText(frame, 'BLUE', (555, 105), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    frame = cv2.rectangle(frame, (550, 125), (630, 175), colors[1], -1)
    frame = cv2.putText(frame, 'GREEN', (555, 155), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    frame = cv2.rectangle(frame, (550, 175), (630, 225), colors[2], -1)
    frame = cv2.putText(frame, 'RED', (555, 205), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    frame = cv2.rectangle(frame, (550, 225), (630, 275), colors[3], -1)
    frame = cv2.putText(frame, 'YELLOW', (555, 255), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 275), (630, 325), (255, 255, 255), -1)
    frame = cv2.rectangle(frame, (570, 285), (610, 315), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 325), (630, 375), (255, 255, 255), -1)
    frame = cv2.circle(frame, (590, 350), 20, (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 375), (630, 425), (255, 255, 255), -1)
    frame = cv2.line(frame, (560, 395), (620, 410), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 425), (630, 475), (255, 255, 255), -1)
    frame = cv2.putText(frame, 'ERASER', (555, 455), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 25), (630, 75), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 75), (630, 125), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 125), (630, 175), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 175), (630, 225), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 225), (630, 275), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 275), (630, 325), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 325), (630, 375), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 375), (630, 425), (0, 0, 0), 2)
    frame = cv2.rectangle(frame, (550, 425), (630, 475), (0, 0 ,0), 2)

while True:
    is_true, frame = feed.read()
    height, width, channels = frame.shape
    canvas = np.zeros((height, width, channels), dtype='uint8') + 255
    frame = cv2.flip(frame, 1)
    frame_orignal = frame
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frameBlur = cv2.GaussianBlur(frameRGB, (3, 3), 3)
    col = []
    result = hands.process(frameBlur)
    if result.multi_hand_landmarks:
        for land_mark in result.multi_hand_landmarks:
            for i in land_mark.landmark:
                col.append((int(i.x*width), int(i.y*height)))
            Draw.draw_landmarks(frame, land_mark, mpHands.HAND_CONNECTIONS)
        distance = (np.linalg.norm(np.array(col[8])-np.array(col[12])))/(np.linalg.norm(np.array(col[0])-np.array(col[5])))    
        if 550<=col[8][0]<=630:
            if 25<=col[8][1]<=75:
                Drawing_pts = []
                Points = []
                rect_command = []
                circle_command = []
                line_command = []
                erase_list = []
            if 75<=col[8][1]<=125:
                Drawing_pts.append([Points, color_no])
                Points = []
                color_no = 0
            if 125<=col[8][1]<=175:
                Drawing_pts.append([Points, color_no])
                Points = []
                color_no = 1
            if 175<=col[8][1]<=225:
                Drawing_pts.append([Points, color_no])
                Points = []
                color_no = 2
            if 225<=col[8][1]<=275:
                Drawing_pts.append([Points, color_no])
                Points = []
                color_no = 3
            if 275<=col[8][1]<=325:
                current_shape = True
                shape = assign0(shape, previous_shape, 1)
            elif 325<=col[8][1]<=375:
                current_shape = True
                shape = assign0(shape, previous_shape, 2)
            elif 375<=col[8][1]<=425:
                current_shape = True
                shape = assign0(shape, previous_shape, 3)
            elif 425<=col[8][1]<=475:
                current_shape = True
                if not previous_shape:    
                    if eraser:
                        eraser = False
                    else:
                        eraser = True
        else:
            current_shape = False
        if distance>=0.7:
            current_draw = True
            if shape==0 and (not eraser):
                Points.append(list(col[8]))
            frame = cv2.circle(frame, col[8], 20, colors[color_no], -1)
        else:
            current_draw = False
            Drawing_pts.append([Points, color_no])
            Points = []
            frame = cv2.circle(frame, col[8], 10, colors[color_no], -1)
        if (not previous_draw) and current_draw:
            if shape!=0:
                if shape==1:
                    start_corner = list(col[8])
                    end_corner = list(col[8])
                elif shape==2:
                    centre = list(col[8])
                    radius = 1
                else:
                    start_line = list(col[8])
                    end_line = list(col[8])
        if previous_draw and current_draw:
            if shape!=0:
                if shape==1:
                    end_corner = list(col[8])
                    frame = cv2.rectangle(frame, start_corner, end_corner, colors[color_no], 2)
                    canvas = cv2.rectangle(canvas, start_corner, end_corner, colors[color_no], 2)
                elif shape==2:
                    radius = int(np.linalg.norm(np.array(col[8])-np.array(centre)))
                    frame = cv2.circle(frame, centre, radius, colors[color_no], 2)
                    canvas = cv2.circle(canvas, centre, radius, colors[color_no], 2)
                else:
                    end_line = list(col[8])
                    frame = cv2.line(frame, start_line, end_line, colors[color_no], 2)
                    canvas = cv2.line(canvas, start_line, end_line, colors[color_no], 2)
        if previous_draw and (not current_draw):
            if shape!=0:
                if shape==1:
                    if start_corner==end_corner:
                        continue
                    if (start_corner[0]>end_corner[0]) or (start_corner[0]>end_corner[0]):
                        start_corner[0], end_corner[0] = end_corner[0], start_corner[0]
                        start_corner[1], end_corner[1] = end_corner[1], start_corner[1]
                    for l in range(start_corner[1], end_corner[1]):
                        Points.append((start_corner[0], l))
                    for m in range(start_corner[0], end_corner[0]):
                        Points.append(list([m, end_corner[1]]))
                    for n in range(end_corner[1], start_corner[1], -1):
                        Points.append(list([end_corner[0], n]))
                    for o in range(end_corner[0], start_corner[0], -1):
                        Points.append(list([o, start_corner[1]]))
                    Drawing_pts.append([Points, color_no])
                    Points = []
                elif shape==2:
                    if radius==1:
                        continue
                    Points = []
                    for p in range(0, 360):
                        y2 = int(centre[1] + radius*np.sin(p))
                        x2 = int(centre[0]+ radius*np.cos(p))
                        Points.append((x2,y2))
                    Drawing_pts.append([Points, color_no])
                    Points = []
                else:
                    if start_line==end_line:
                        continue
                    Drawing_pts.append([getLine(start_line[0], start_line[1], end_line[0], end_line[1]), color_no])
        if eraser and current_draw:
            for Point1, ________ in Drawing_pts:
                for __ in Point1:
                    if np.linalg.norm(np.array(__)-np.array(col[8]))<=20:
                        Point1.insert(Point1.index(__), (0, 0))
                        Point1.remove(__)
    current_time = time.time()
    fps = 1/(current_time-previous_time)
    previous_time = current_time
    frame = cv2.putText(frame, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2.5, (173, 78, 132), 3)
    if Drawing_pts:
        for Point, color_ in Drawing_pts:
            for j in range(1, len(Point)):
                if Point[j-1]==(0, 0) or Point[j]==(0, 0):
                    continue
                frame = cv2.line(frame, Point[j-1], Point[j], colors[color_], 2)
                canvas = cv2.line(canvas, Point[j-1], Point[j], colors[color_], 2)
    if Points:
        for k in range(1, len(Points)):
            frame = cv2.line(frame, Points[k-1], Points[k], colors[color_no], 2)
            canvas = cv2.line(canvas, Points[k-1], Points[k], colors[color_no], 2)
    Draw_boxes_2(frame)
    previous_draw = current_draw
    previous_shape = current_shape
    if eraser:
        shape=0
    cv2.imshow('WebCam',frame)
    cv2.imshow('Canvas', canvas)
    if cv2.waitKey(20)==27:
        break
feed.release()
cv2.destroyAllWindows() 
