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
                #    [4]         0      1     2      3           4    5    6    7    8      9       10   11  12   13
                point.append(['right', 'X', 'X', 'rightUpDown', 'X', 'X', 'X', 'X', 'X', 'UpDown', 'X', 'X', 'X', 'X',
                              # 14   15
                              'X', 'X'])
                pointColumn = point[3][0]
                pointRow = point[3][1]
                pointName = point[1]
                for pointFind in points:
                    pointColumnFind = pointFind[3][0]
                    pointRowFind = pointFind[3][1]
                    pointNameFind = pointFind[1]
                    if pointRowFind == pointRow and pointColumnFind != pointColumn + 1:
                        for i in range(2, 4):
                            if pointColumnFind == pointColumn + i:
                                point[4][i - 1] = pointNameFind
                                break
                    elif -2 <= abs(pointRowFind - pointRow) <= 2 and pointColumnFind == pointColumn + 1:
                        for i in range(2, -3, -1):
                            if pointRowFind == pointRow - i:
                                point[4][i + 6] = pointNameFind
                                break
                    elif -3 <= abs(pointRowFind - pointRow) <= 3 and pointColumnFind == pointColumn:
                        for i in range(3, -4, -1):
                            if pointRowFind == pointRow - i:
                                point[4][i + 12] = pointNameFind
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
        #                 pointsChance.append(point)
        #                 cv.putText(screenshot, point[1], (point[0][0], point[0][1]),
        #                            cv.FONT_HERSHEY_SIMPLEX, .4, point[2])
        #                 target_click = wincap.get_screen_position(point[0])
        #                 if not is_bot_in_action:
        #                     is_bot_in_action = True
        #                     t = Thread(target=bot_action, args=(target_click,))
        #                     t.start()
        #             if pointName == rightUp2 == rightUp1:
        #                 pointsChance.append(point)
        #                 cv.putText(screenshot, point[1], (point[0][0], point[0][1]),
        #                            cv.FONT_HERSHEY_SIMPLEX, .4, point[2])
        #                 target_click = wincap.get_screen_position(point[0])
        #                 if not is_bot_in_action:
        #                     is_bot_in_action = True
        #                     t = Thread(target=bot_action, args=(target_click,))
        #                     t.start()
        #             if pointName == rightDown2 == rightDown1:
        #                 pointsChance.append(point)
        #                 cv.putText(screenshot, point[1], (point[0][0], point[0][1]),
        #                            cv.FONT_HERSHEY_SIMPLEX, .4, point[2])
        #                 target_click = wincap.get_screen_position(point[0])
        #                 if not is_bot_in_action:
        #                     is_bot_in_action = True
        #                     t = Thread(target=bot_action, args=(target_click,))
        #                     t.start()
        #             if pointName == rightUp1 == rightDown1:
        #                 pointsChance.append(point)
        #                 cv.putText(screenshot, point[1], (point[0][0], point[0][1]),
        #                            cv.FONT_HERSHEY_SIMPLEX, .4, point[2])
        #                 target_click = wincap.get_screen_position(point[0])
        #                 if not is_bot_in_action:
        #                     is_bot_in_action = True
        #                     t = Thread(target=bot_action, args=(target_click,))
        #                     t.start()
        #     except IndexError or TypeError:
        #         cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
        #                    screenshot)
        #         print('error')
        #         break
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    pointCheck = points[random.randint(1, len(points))]
    print(pointCheck)
    for (k, l) in zip(range(8, 3, -1), range(-100, 101, 50)):
        cv.putText(screenshot, pointCheck[4][k], (pointCheck[0][0] + 50, pointCheck[0][1] + l),
                   cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    cv.putText(screenshot, pointCheck[1] + "           " + pointCheck[4][1] + " " + pointCheck[4][2],
               (pointCheck[0][0], pointCheck[0][1]), cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    cv.imshow('Map', screenshot)
    sleep(10)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    # elif key == ord('f'):
    # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time), screenshot)
