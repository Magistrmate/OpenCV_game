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
import psutil

flag = 1
for p in psutil.process_iter():
    if p.name() == "scrcpy.exe":
        flag = 0
        print('Find')
if flag == 1:
    subprocess.Popen([r'C:\Users\\retro\Downloads\scrcpy-win64-v1.24\scrcpy.exe', '-S', '-w', '--window-x=1485',
                      '--window-y=90'])
    sleep(5)

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
    points = []
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
                if x0 <= x <= (x0 + 50):
                    for (y0, row) in zip(range(first_point_for_y - 10, last_point_for_y + 5, 51), range(1, 11)):
                        if y0 <= y <= (y0 + 50):
                            points[index].append((column, row))
                            # cv.putText(screenshot, str(column) + " " + str(row) + " " + name, (x - 20, y - 20),
                            #           cv.FONT_HERSHEY_SIMPLEX, .4, color)
        for (index, point) in enumerate(points):
            try:
                point.append(['right', 'empty', 'empty', 'empty', 'rightUp', 'empty', 'empty', 'rightDown', 'empty',
                              'empty'])
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
                                break
                    elif pointColumnFind == pointColumn + 1:
                        for n in range(1, 3):
                            if pointRowFind == pointRow - n:
                                point[4][n + 4] = pointNameFind
                                break
            except IndexError or TypeError:
                cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                           screenshot)
                print('error')
                break
        pointsCheck = []
        for point in points:
            try:
                pointName = point[1]
                right1 = point[4][1]
                right2 = point[4][2]
                right3 = point[4][3]
                if pointName == right2 == right3 and right1 != 'empty':
                    pointsCheck.append(point)
                    # print(point)
                    # print('move')
                    # target_click = wincap.get_screen_position(point[0])
                    # if not is_bot_in_action:
                    #     is_bot_in_action = True
                    #     t = Thread(target=bot_action, args=(target_click,))
                    #     t.start()
            except IndexError or TypeError:
                cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                           screenshot)
                print('error')
                break
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    pointCheck = points[random.randint(1, len(points))]
    print(pointCheck)
    cv.putText(screenshot, pointCheck[4][6], (pointCheck[0][0] + 50, pointCheck[0][1] - 100),
               cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    cv.putText(screenshot, pointCheck[4][5], (pointCheck[0][0] + 50, pointCheck[0][1] - 50),
               cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    cv.putText(screenshot, pointCheck[1] + " " + pointCheck[4][1] + " " + pointCheck[4][2] + " " + pointCheck[4][3],
               (pointCheck[0][0], pointCheck[0][1]), cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    cv.imshow('Map', screenshot)
    sleep(5)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    # elif key == ord('f'):
    # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time), screenshot)
