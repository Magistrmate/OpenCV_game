import operator
import random

import numpy as np
from Picture import Picture
import cv2 as cv
from time import time, sleep
from windowcapture import WindowCapture
from threading import Thread
import pydirectinput
import subprocess
from random import randint

# subprocess.Popen([r"C:\Users\\retro\Downloads\scrcpy-win64-v1.24\scrcpy.exe", "-S", "-w"])
# sleep(2)
wincap = WindowCapture('MI 9')

is_bot_in_action = False

loop_time = time()


def bot_action(target):
    pydirectinput.moveTo(target[0])
    pydirectinput.mouseDown()
    pydirectinput.moveTo(target[0] + 50, target[1])
    pydirectinput.mouseUp()
    sleep(5)
    global is_bot_in_action
    is_bot_in_action = False


while True:
    screenshot = wincap.get_screenshot()
    points = list()
    namesColors = [('duck', (0, 191, 255)), ('chip', (0, 0, 255)), ('ball', (0, 255, 0)), ('backpack', (255, 0, 0)),
                   ('spruce', (0, 128, 0)), ('egg', (255, 0, 139))]
    for (name, color) in namesColors:
        Picture(name, color, screenshot, points)
    if len(points) > 0:
        (first_point_for_x, _), _, _ = min(points, key=lambda n: n[0][0])
        (last_point_for_x, _), _, _ = max(points, key=lambda n: n[0][0])
        (_, first_point_for_y), _, _ = min(points, key=lambda n: n[0][1])
        (_, last_point_for_y), _, _ = max(points, key=lambda n: n[0][1])
        for (index, point) in enumerate(points):
            x = point[0][0]
            y = point[0][1]
            name = point[1]
            color = point[2]
            for (x0, column) in zip(range(first_point_for_x - 5, last_point_for_x + 5, 51), range(1, 9)):
                if x0 <= x <= (x0 + 11):
                    for (y0, row) in zip(range(first_point_for_y - 5, last_point_for_y + 5, 51), range(1, 11)):
                        if y0 <= y <= (y0 + 11):
                            points[index].append((column, row))
                            cv.putText(screenshot, str(column) + " " + str(row) + " " + name, (x - 20, y - 20),
                                       cv.FONT_HERSHEY_SIMPLEX, .4, color)
        # print(f'points\n{points}')
        for (index, point) in enumerate(points):
            point.append(['right', 'empty', 'empty', 'empty'])
            # print(point)
            # print('len')
            # print(len(point))
            # print(f'point{point}')
            pointColumn = point[3][0]
            pointRow = point[3][1]
            pointName = point[1]
            for pointFind in points:
                pointColumnFind = pointFind[3][0]
                pointRowFind = pointFind[3][1]
                pointNameFind = pointFind[1]
                if pointRowFind == pointRow:
                    for i in range(1, 4):
                        if pointColumnFind == pointColumn + i:
                            point[4][i] = pointNameFind
                            continue
                    # if pointColumnFind == pointColumn + 1:
                    #     # if len(point) == 4:
                    #     point[4][1] = pointNameFind
                    #     # point.insert(4, ('right1', pointNameFind))
                    #     continue
                    # if pointColumnFind == pointColumn + 2:
                    #     # if len(point) == 5:
                    #     #     point.insert(5, ('right2', pointNameFind))
                    #     # else:
                    #     point[4][2] = pointNameFind
                    #     # point.insert(5, ('right2', pointNameFind))
                    #     continue
                    #     # print(f'exist{point[4]}')
                    # if pointColumnFind == pointColumn + 3:
                    #     point[4][3] = pointNameFind
                    #     # point.insert(6, ('right3', pointNameFind))
                    #     continue
                        # print(f'pointRight3{pointRight3}')
                        # point.append(('right3', pointNameFind))
            # if len(point) == 4:
            #     point.insert(4, ('right1', 'empty'))
            #     point.insert(5, ('right2', 'empty'))
            #     point.insert(6, ('right3', 'empty'))
            # elif len(point) == 5:
            #     if point[4][0] == 'right2':
            #         point.insert(4, ('right1', 'empty'))
            #     else:
            #         point.insert(5, ('right2', 'empty'))
            #     point.insert(6, ('right3', 'empty'))
            # elif len(point) == 6:
            #     if point[4][0] == 'right2':
            #         point.insert(4, ('right1', 'empty'))
            #     elif point[5][0] == 'right3':
            #         point.insert(5, ('right2', 'empty'))
            #     else:
            #         point.insert(6, ('right3', 'empty'))
                # print(f'pointRight empty')
        # print(random.randint(1, len(points)))
        # print(points[random.randint(1, len(points))])
        print(points)
    cv.imshow('Map', screenshot)

    targets = points
    # if len(targets) > 0:
    #     target_click = wincap.get_screen_position(targets[0])
    #     if not is_bot_in_action:
    #         is_bot_in_action = True
    #         t = Thread(target=bot_action, args=(target_click,))
    #         t.start()

    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
