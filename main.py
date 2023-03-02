import operator
import random
import traceback

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
                      '--window-y=90', '--tcpip=192.168.137.35'])
    sleep(5)

wincap = WindowCapture('MI 9')

is_bot_in_action = False

loop_time = time()


def bot_action(target, one, two):
    pydirectinput.moveTo(target[0], target[1])
    pydirectinput.mouseDown()
    pydirectinput.moveTo(target[0] + 50 * one, target[1] + 50 * two)
    pydirectinput.mouseUp()
    sleep(10)
    global is_bot_in_action
    is_bot_in_action = False


def before_bot_action(point_target, one, two):
    global is_bot_in_action
    target_click = wincap.get_screen_position(point_target[0])
    if not is_bot_in_action:
        is_bot_in_action = True
        t = Thread(target=bot_action, args=(target_click, one, two))
        t.start()


while True:
    screenshot = wincap.get_screenshot()
    points = []
    namesColors = [('ball', (0, 255, 0), .85, .85, .7, .76, False), ('backpack', (255, 0, 0), .76, .85, .7, .76, False),
                   ('egg', (255, 0, 139), .77, .85, .7, .76, False), ('chip', (0, 0, 255), .79, .85, .74, .76, False),
                   ('duck', (0, 191, 255), .85, .9, .65, .76, False), ('spruce', (0, 128, 0), .76, .85, .7, .76, False),
                   ('h_rocket', (145, 101, 214), .76, .85, .7, .76, True),
                   ('v_rocket', (145, 101, 214), .76, .85, .7, .76, True),
                   ('envelope', (103, 90, 231), .76, .85, .7, .76, True),
                   ('bomb', (169, 133, 247), .76, .85, .65, .76, True),
                   ('cube', (0, 0, 0), .85, .9, .85, .76, True),
                   ('canister', (200, 200, 200), .85, .9, .65, .76, True)]
    for (name, color, space_hold, tape_hold, carpet_hold, ground_hold, pointPlus) in namesColors:
        Picture(name, color, space_hold, tape_hold, carpet_hold, ground_hold, pointPlus, screenshot, points)
    if len(points) > 0:
        (first_point_for_x, _), _, _ = min(points, key=lambda l: l[0][0])
        (last_point_for_x, _), _, _ = max(points, key=lambda l: l[0][0])
        (_, first_point_for_y), _, _ = min(points, key=lambda l: l[0][1])
        (_, last_point_for_y), _, _ = max(points, key=lambda l: l[0][1])
        for (index, point) in enumerate(points):
            x = point[0][0]
            y = point[0][1]
            name = point[1][0]
            properties = f't{point[1][2]}c{point[1][4]}g{point[1][6]}'
            color = point[2]
            for (x0, column) in zip(range(first_point_for_x - 5, last_point_for_x + 5, 51), range(1, 9)):
                if x0 <= x <= (x0 + 50):
                    for (y0, row) in zip(range(first_point_for_y - 10, last_point_for_y + 5, 51), range(1, 11)):
                        if y0 <= y <= (y0 + 50):
                            points[index].append((column, row))
                            # for (text, ya) in zip((f'{column} {row}', name, properties), (range(20, -1, -10))):
                            #     cv.putText(screenshot, text, (x - 20, y - ya), cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
        try:
            for point in points:
                # [4]           0
                point.append(['left', ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              'right', ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False), 'up0',
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), 'down0',
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), 'up', ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              'down', ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False),
                              ('', 't', 0, 'c', 0, 'g', 0, 'p', False), ('', 't', 0, 'c', 0, 'g', 0, 'p', False)])
                pointColumn = point[3][0]
                pointRow = point[3][1]
                pointName = point[1][0]
                for pointFind in points:
                    pointColumnFind = pointFind[3][0]
                    pointRowFind = pointFind[3][1]
                    pointNameFind = pointFind[1][0]
                    x = pointColumnFind - pointColumn
                    y = pointRowFind - pointRow
                    if -7 <= x <= 7 and -12 <= y <= 12:
                        if x == 0 and (y == 1 or y == -1):
                            point[4][46 + y] = (pointNameFind, 't', pointFind[1][2], 'c', pointFind[1][4], 'g',
                                                pointFind[1][6], 'p', pointFind[1][8])
                        if (-7 <= x <= -1 or 1 <= x <= 7) and -1 <= y <= 1:
                            for (m, d) in zip((1, -1), (0, 10)):
                                for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
                                    if c == x:
                                        point[4][m + x + y + n] = (pointNameFind, 't', pointFind[1][2], 'c',
                                                                   pointFind[1][4], 'g', pointFind[1][6], 'p',
                                                                   pointFind[1][8])
                                        break
                        if -1 <= x <= 1 and (-12 <= y <= -2 or 2 <= y <= 12):
                            for (m, d) in zip((1, -1), (0, 12)):
                                for (r, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
                                    if r == y:
                                        point[4][m + x + y + n] = (pointNameFind, 't', pointFind[1][2], 'c',
                                                                   pointFind[1][4], 'g', pointFind[1][6], 'p',
                                                                   pointFind[1][8])
                                        break
            # comment down
            for point in points:
                pointName = point[1][0]
                # [5]               0                    1                     2                   3
                point.append([('l', -1, 0), [0, 't', 0, 'c', 0, 'p', 0], ('r', 1, 0), [0, 't', 0, 'c', 0, 'p', 0],
                              #     4                    5                     6                     7
                              ('u', 0, -1), [0, 't', 0, 'c', 0, 'p', 0], ('d', 0, 1), [0, 't', 0, 'c', 0, 'p', 0]])
                property_tape0 = point[1][2]
                property_plus0 = point[1][8]
                if pointName != 'canister' and property_tape0 == 0:
                    pointStartUp = 80
                    pointStartLeftUp = 19
                    pointStartDown = 114
                    pointStartLeftDown = 21
                    for (startUp_Down, startLeftUp_Down) in ((pointStartUp, pointStartLeftUp), (pointStartDown,
                                                                                                pointStartLeftDown)):
                        carpetExistUp_Down = 0
                        tapeExistUp_Down = 0
                        pointUp_Down = point[4][startLeftUp_Down + 26]  # 45 or 47
                        if pointUp_Down[0] != '':
                            property_tape = pointUp_Down[2]
                            property_carpet = pointUp_Down[4]
                            property_plus = pointUp_Down[8]
                            if property_tape == 0:
                                if property_carpet == 1:
                                    carpetExistUp_Down = 1
                                leftMatch = 0
                                rightMatch = 0
                                up_downMatch = 0
                                if property_plus0 and property_plus:
                                    point[5][startLeftUp_Down - 14][6] = 1
                                else:
                                    endUp_Down = startUp_Down - 31
                                    for (moveUp_Down, order) in zip(range(startUp_Down, endUp_Down, -3), range(1, 13)):
                                        pointFind = point[4][moveUp_Down]
                                        pointNameFind = pointFind[0]
                                        pointTapeFind = pointFind[2]
                                        pointCarpetFind = pointFind[4]
                                        if pointNameFind == pointName and up_downMatch == order - 1:
                                            up_downMatch = order
                                            if pointTapeFind != 0 and tapeExistUp_Down == order - 1:
                                                tapeExistUp_Down = tapeExistUp_Down + pointTapeFind
                                            if pointCarpetFind == 1 and carpetExistUp_Down == order - 1:
                                                carpetExistUp_Down = carpetExistUp_Down + pointCarpetFind
                                        else:
                                            break
                                tapeExistLeft_RightUp_Down = 0
                                for (a, b, c) in zip((0, 22), (-19, 3), (-3, 19)):
                                    pointNameFind = point[4][startLeftUp_Down + a][0]  # (19 or 21) or (41 or 43)
                                    pointTapeFind = point[4][startLeftUp_Down + a][2]
                                    pointCarpetFind = point[4][startLeftUp_Down + a][4]
                                    if pointNameFind == pointName:
                                        if a == 0:
                                            leftMatch = 1
                                        else:
                                            rightMatch = 1
                                        if pointTapeFind != 0:
                                            tapeExistLeft_RightUp_Down = tapeExistLeft_RightUp_Down + pointTapeFind
                                        if pointCarpetFind == 1:
                                            carpetExistUp_Down = carpetExistUp_Down + pointCarpetFind
                                        endLeftUp_Down = startLeftUp_Down + b
                                        for (moveLeft, order) in zip(range(startLeftUp_Down + c, endLeftUp_Down, -3),
                                                                     range(2, 8)):
                                            pointFind = point[4][moveLeft]
                                            pointNameFind = pointFind[0]
                                            pointTapeFind = pointFind[2]
                                            pointCarpetFind = pointFind[4]
                                            if pointNameFind == pointName:
                                                if leftMatch == order - 1:
                                                    leftMatch = order
                                                elif rightMatch == order - 1:
                                                    rightMatch = order
                                                if pointCarpetFind == 1:
                                                    carpetExistUp_Down = carpetExistUp_Down + pointCarpetFind
                                                if pointTapeFind != 0:
                                                    tapeExistLeft_RightUp_Down = tapeExistLeft_RightUp_Down + \
                                                                                 pointTapeFind
                                            else:
                                                break
                                if property_plus0 and property_plus0 != property_plus:
                                    directionUp_Down = 3
                                elif leftMatch + rightMatch >= up_downMatch:
                                    directionUp_Down = leftMatch + rightMatch + 1
                                    if directionUp_Down >= 3:
                                        point[5][startLeftUp_Down - 14][2] = tapeExistLeft_RightUp_Down
                                else:
                                    directionUp_Down = up_downMatch + 1
                                    if directionUp_Down >= 3:
                                        point[5][startLeftUp_Down - 14][2] = tapeExistUp_Down
                                point[5][startLeftUp_Down - 14][0] = directionUp_Down
                                if carpetExistUp_Down != 0 and carpetExistUp_Down < directionUp_Down and \
                                        directionUp_Down >= 3:
                                    point[5][startLeftUp_Down - 14][4] = directionUp_Down - carpetExistUp_Down
                                if directionUp_Down >= 3:
                                    if startLeftUp_Down == 19:
                                        aprox = 0
                                    else:
                                        aprox = 10
                                    directionLetter = point[5][startLeftUp_Down - 15][0]
                                    cv.putText(screenshot, directionLetter + str(directionUp_Down) +
                                               point[5][startLeftUp_Down - 14][1] +
                                               str(point[5][startLeftUp_Down - 14][2]) +
                                               point[5][startLeftUp_Down - 14][3] +
                                               str(point[5][startLeftUp_Down - 14][4]),
                                               (point[0][0] - 5, point[0][1] - 10 + aprox), cv.FONT_HERSHEY_SIMPLEX, .4,
                                               (0, 0, 0))
                    pointStartLeft = 17
                    pointStartRight = 39
                    pointStartLeftUp2 = 79
                    pointStartRightUp2 = 81
                    for (startLeft_Right, startLeft_RightUp2) in ((pointStartLeft, pointStartLeftUp2),
                                                                  (pointStartRight, pointStartRightUp2)):
                        carpetExistLeft_Right = 0
                        tapeExistLeft_Right = 0
                        pointLeft_Right = point[4][startLeft_Right + 3]
                        if pointLeft_Right[0] != '':
                            property_tape = pointLeft_Right[2]
                            property_carpet = pointLeft_Right[4]
                            property_plus = pointLeft_Right[8]
                            if property_tape == 0:
                                if property_carpet == 1:
                                    carpetExistLeft_Right = 1
                                upMatch = 0
                                downMatch = 0
                                left_rightMatch = 0
                                if property_plus0 and property_plus:
                                    point[5][startLeft_RightUp2 - 78][6] = 1
                                else:
                                    endLeft_Right = startLeft_Right - 16
                                    for (moveLeft_Right, order) in zip(range(startLeft_Right, endLeft_Right, -3),
                                                                       range(1, 8)):
                                        pointFind = point[4][moveLeft_Right]
                                        pointNameFind = pointFind[0]
                                        pointTapeFind = pointFind[2]
                                        pointCarpetFind = pointFind[4]
                                        if pointNameFind == pointName and left_rightMatch == order - 1:
                                            left_rightMatch = order
                                            if pointTapeFind != 0 and tapeExistLeft_Right == order - 1:
                                                tapeExistLeft_Right = tapeExistLeft_Right + pointTapeFind
                                            if pointCarpetFind == 1 and carpetExistLeft_Right == order - 1:
                                                carpetExistLeft_Right = carpetExistLeft_Right + pointCarpetFind
                                        else:
                                            break
                                tapeExistLeft_RightUp_Down = 0
                                for (a, b, c) in zip((2, 4), (0, 34), (-31, 3)):
                                    pointNameFind = point[4][startLeft_Right + a][0]
                                    pointTapeFind = point[4][startLeft_Right + a][2]
                                    pointCarpetFind = point[4][startLeft_Right + a][4]
                                    if pointNameFind == pointName:
                                        if a == 2:
                                            upMatch = 1
                                        else:
                                            downMatch = 1
                                        if pointTapeFind != 0:
                                            tapeExistLeft_RightUp_Down = tapeExistLeft_RightUp_Down + pointTapeFind
                                        if pointCarpetFind == 1:
                                            carpetExistLeft_Right = carpetExistLeft_Right + pointCarpetFind
                                        startLeft_RightDown2 = startLeft_RightUp2 + b
                                        endLeft_RightDown2 = startLeft_RightUp2 + c
                                        for (moveDown, order) in zip(range(startLeft_RightDown2, endLeft_RightDown2,
                                                                           -3), range(2, 8)):
                                            pointFind = point[4][moveDown]
                                            pointNameFind = pointFind[0]
                                            pointTapeFind = pointFind[2]
                                            pointCarpetFind = pointFind[4]
                                            if pointNameFind == pointName:
                                                if downMatch == order - 1:
                                                    downMatch = order
                                                elif upMatch == order - 1:
                                                    upMatch = order
                                                if pointCarpetFind == 1:
                                                    carpetExistLeft_Right = carpetExistLeft_Right + pointCarpetFind
                                                if pointTapeFind != 0:
                                                    tapeExistLeft_RightUp_Down = tapeExistLeft_RightUp_Down + \
                                                                                 pointTapeFind
                                            else:
                                                break
                                if property_plus0 and property_plus0 != property_plus:
                                    directionLeft_Right = 3
                                elif upMatch + downMatch >= left_rightMatch:
                                    directionLeft_Right = upMatch + downMatch + 1
                                    if directionLeft_Right >= 3:
                                        point[5][startLeft_RightUp2 - 78][2] = tapeExistLeft_RightUp_Down
                                else:
                                    directionLeft_Right = left_rightMatch + 1
                                    if directionLeft_Right >= 3:
                                        point[5][startLeft_RightUp2 - 78][2] = tapeExistLeft_RightUp_Down
                                point[5][startLeft_RightUp2 - 78][0] = directionLeft_Right
                                if carpetExistLeft_Right != 0 and carpetExistLeft_Right < directionLeft_Right and \
                                        directionLeft_Right >= 3:
                                    point[5][startLeft_RightUp2 - 78][4] = directionLeft_Right - carpetExistLeft_Right
                                if directionLeft_Right >= 3:
                                    directionLetter = point[5][startLeft_RightUp2 - 79][0]
                                    cv.putText(screenshot, directionLetter + str(directionLeft_Right) +
                                               point[5][startLeft_RightUp2 - 78][1] +
                                               str(point[5][startLeft_RightUp2 - 78][2]) +
                                               point[5][startLeft_RightUp2 - 78][3] +
                                               str(point[5][startLeft_RightUp2 - 78][4]),
                                               (point[0][0] - 3, point[0][1] + startLeft_Right // 2),
                                               cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
            chance_points = []
            for position in range(1, 8, 2):
                xy, name, _, rc, _, chances = max(points, key=lambda l: (l[5][position][6], l[5][position][2],
                                                                         l[5][position][4], l[5][position][0], l[3][1]))
                direction = chances[position - 1]
                numberMatch = chances[position][0]
                numberTape = chances[position][2]
                numberCarpet = chances[position][4]
                numberPlus = chances[position][6]
                #                      0    1    2     3          4             5            6           7
                chance_points.append([xy, name, rc, direction, numberMatch, numberTape, numberCarpet, numberPlus])
            max_combo = max(chance_points, key=lambda l: (l[7], l[5], l[6], l[4], l[2][1]))
            before_bot_action(max_combo, max_combo[3][1], max_combo[3][2])
            cv.putText(screenshot, max_combo[3][0], (max_combo[0]),
                       cv.FONT_HERSHEY_SIMPLEX, .8, (255, 255, 255))
        except IndexError or TypeError or ValueError:
            print(IndexError or TypeError or ValueError)
            continue
    cv.imshow('Map', screenshot)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
        # print('FPS {}'.format(1 / (time() - loop_time)))
        # loop_time = time()
        # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
        #            screenshot)
        # pointCheck = points[39]
        # pointCheck = points[random.randint(0, len(points))]
        # print(pointCheck)
        # cv.putText(screenshot, pointCheck[1][0], (pointCheck[0][0], pointCheck[0][1]), cv.FONT_HERSHEY_DUPLEX,
        #            .6, pointCheck[2])
        # cv.putText(screenshot, pointCheck[4][45][0], (pointCheck[0][0], pointCheck[0][1] - 50),
        #            cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
        # cv.putText(screenshot, pointCheck[4][47][0], (pointCheck[0][0], pointCheck[0][1] + 50),
        #            cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
        # for (m, d) in zip((1, -1), (0, 10)):
        #     for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
        #         for r in range(-1, 2, 1):
        #             cv.putText(screenshot, pointCheck[4][m + c + r + n][0], (pointCheck[0][0] + c * 50,
        #                                                                      pointCheck[0][1] + r * 50),
        #                        cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
        # for (m, d) in zip((1, -1), (0, 12)):
        #     for (c, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
        #         for r in range(-1, 2, 1):
        #             cv.putText(screenshot, pointCheck[4][m + c + r + n][0], (pointCheck[0][0] + r * 50,
        #                                                                      pointCheck[0][1] + c * 50),
        #                        cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
        # sleep(5)
