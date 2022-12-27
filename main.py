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


def before_bot_action(point_target):
    global is_bot_in_action
    pointsChance.append(point_target)
    cv.putText(screenshot, point_target[1], (point_target[0][0], point_target[0][1]),
               cv.FONT_HERSHEY_SIMPLEX, .4, point_target[2])
    target_click = wincap.get_screen_position(point_target[0])
    if not is_bot_in_action:
        is_bot_in_action = True
        t = Thread(target=bot_action, args=(target_click,))
        t.start()


while True:
    screenshot = wincap.get_screenshot()
    points = []
    namesColors = [('duck', (0, 191, 255)), ('chip', (0, 0, 255)), ('ball', (0, 255, 0)), ('backpack', (255, 0, 0)),
                   ('spruce', (0, 128, 0)), ('egg', (255, 0, 139))]
    for (name, color) in namesColors:
        Picture(name, color, screenshot, points)
    if len(points) > 0:
        (first_point_for_x, _), _, _ = min(points, key=lambda k: k[0][0])
        (last_point_for_x, _), _, _ = max(points, key=lambda k: k[0][0])
        (_, first_point_for_y), _, _ = min(points, key=lambda k: k[0][1])
        (_, last_point_for_y), _, _ = max(points, key=lambda k: k[0][1])
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
                #    [4]         0      1          2        3    4    5    6    7    8    9   10       11     12   13
                point.append(['right', 'X', 'rightUpDown', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'UpDown', 'X', 'X',
                              # 14  15   16   17
                              'X', 'X', 'X', 'X', 'left', ])
                pointColumn = point[3][0]
                pointRow = point[3][1]
                pointName = point[1]
                for pointFind in points:
                    pointColumnFind = pointFind[3][0]
                    pointRowFind = pointFind[3][1]
                    pointNameFind = pointFind[1]
                    if pointRowFind == pointRow and pointColumnFind == pointColumn + 3:
                        point[4][1] = pointNameFind
                    # if pointRowFind == pointRow and pointColumnFind != pointColumn + 1:
                    #     for i in range(2, 4):
                    #         if pointColumnFind == pointColumn + i:
                    #             point[4][i - 1] = pointNameFind
                    #             break
                    elif -2 <= abs(pointRowFind - pointRow) <= 2 and (pointColumnFind == pointColumn + 1 or
                                                                      pointColumnFind == pointColumn + 2):
                        if pointColumnFind == pointColumn + 1:
                            for i in range(2, -3, -1):
                                if pointRowFind == pointRow - i:
                                    point[4][i + 5] = pointNameFind
                                    break
                        elif pointColumnFind == pointColumn + 2:
                            for i in range(1, -2, -1):
                                if pointRowFind == pointRow - i:
                                    point[4][9 + i] = pointNameFind
                                    break
                            # if pointRowFind == pointRow - 1:
                            #     point[4][10] = pointNameFind
                            # elif pointRowFind == pointRow + 1:
                            #     point[4][9] = pointNameFind
                    elif 0 < abs(pointRowFind - pointRow) <= 3 and pointColumnFind == pointColumn:
                        if -3 <= pointRowFind - pointRow < 0:
                            for i in range(1, 4):
                                if pointRowFind == pointRow - i:
                                    point[4][14 + i] = pointNameFind
                                    break
                        else:
                            for i in range(1, 4):
                                if pointRowFind == pointRow + i:
                                    point[4][15 - i] = pointNameFind
                                    break
            except IndexError or TypeError:
                cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                           screenshot)
                print('error')
                break
        # pointsChance = []
        # for point in points:
        #     try:
        #         pointName = point[1]
        #         right2 = point[4][1]
        #         right3 = point[4][2]
        #         rightUp2 = point[4][8]
        #         rightUp1 = point[4][7]
        #         right1 = point[4][6]
        #         rightDown1 = point[4][5]
        #         rightDown2 = point[4][4]
        #         if right1 != 'X':
        #             if pointName == right2 == right3:
        #                 before_bot_action(point)
        #             if pointName == rightUp2 == rightUp1:
        #                 before_bot_action(point)
        #             if pointName == rightDown2 == rightDown1:
        #                 before_bot_action(point)
        #             if pointName == rightUp1 == rightDown1:
        #                 before_bot_action(point)
        #     except IndexError or TypeError:
        #         cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
        #                    screenshot)
        #         print('error')
        #         break
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    pointCheck = points[random.randint(0, len(points))]
    print(pointCheck)
    cv.putText(screenshot, pointCheck[1], (pointCheck[0][0], pointCheck[0][1]), cv.FONT_HERSHEY_SIMPLEX,
               .8, pointCheck[2])
    cv.putText(screenshot, pointCheck[4][1], (pointCheck[0][0] + 150, pointCheck[0][1]), cv.FONT_HERSHEY_SIMPLEX,
               .4, pointCheck[2])
    for (i, n) in zip(range(7, 2, -1), range(-100, 101, 50)):
        cv.putText(screenshot, pointCheck[4][i], (pointCheck[0][0] + 50, pointCheck[0][1] + n),
                   cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    for (i, n) in zip(range(10, 7, -1), range(-50, 51, 50)):
        cv.putText(screenshot, pointCheck[4][i], (pointCheck[0][0] + 100, pointCheck[0][1] + n),
                   cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    for (i, n) in zip(range(17, 14, -1), range(-150, -49, 50)):
        cv.putText(screenshot, pointCheck[4][i], (pointCheck[0][0], pointCheck[0][1] + n),
                   cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    for (i, n) in zip(range(14, 11, -1), range(50, 151, 50)):
        cv.putText(screenshot, pointCheck[4][i], (pointCheck[0][0], pointCheck[0][1] + n),
                   cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    cv.imshow('Map', screenshot)
    sleep(10)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    # elif key == ord('f'):
    # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time), screenshot)
