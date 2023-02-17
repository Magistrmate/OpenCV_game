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
                      '--window-y=90'])
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
    namesColors = [('ball', (0, 255, 0), .76, .85, .7, .76), ('backpack', (255, 0, 0), .76, .85, .7, .76),
                   ('egg', (255, 0, 139), .77, .85, .7, .76), ('chip', (0, 0, 255), .79, .85, .74, .76),
                   ('duck', (0, 191, 255), .76, .9, .65, .76), ('spruce', (0, 128, 0), .76, .85, .7, .76),
                   ('h_rocket', (145, 101, 214), .76, .85, .7, .76), ('v_rocket', (145, 101, 214), .76, .85, .7, .76),
                   ('envelope', (103, 90, 231), .76, .85, .7, .76), ('bomb', (169, 133, 247), .76, .85, .65, .76)]
    # namesColors = [('chip', (0, 0, 255), .7, .76, .76, .76)]
    for (name, color, space_hold, tape_hold, carpet_hold, ground_hold) in namesColors:
        Picture(name, color, space_hold, tape_hold, carpet_hold, ground_hold, screenshot, points)
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
                            # cv.putText(screenshot, str(column) + " " + str(row), (x - 20, y - 20),
                            #            cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
                            # cv.putText(screenshot, name, (x - 20, y - 10),
                            #            cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
                            # cv.putText(screenshot, properties, (x - 20, y),
                            #            cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
        # try:
        for point in points:
            # [4]           0
            point.append(['left', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                          'X', 'X', 'X', 'X', 'X', 'right', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                          'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'up0', 'X', 'down0', 'X', 'up', 'X',
                          'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                          'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'down', 'X', 'X',
                          'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                          'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
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
                                            pointFind[1][6])
                    if (-7 <= x <= -1 or 1 <= x <= 7) and -1 <= y <= 1:
                        for (m, d) in zip((1, -1), (0, 10)):
                            for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
                                if c == x:
                                    point[4][m + x + y + n] = (pointNameFind, 't', pointFind[1][2], 'c',
                                                               pointFind[1][4], 'g', pointFind[1][6])
                                    break
                    if -1 <= x <= 1 and (-12 <= y <= -2 or 2 <= y <= 12):
                        for (m, d) in zip((1, -1), (0, 12)):
                            for (r, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
                                if r == y:
                                    point[4][m + x + y + n] = (pointNameFind, 't', pointFind[1][2], 'c',
                                                               pointFind[1][4], 'g', pointFind[1][6])
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
        for point in points:
            pointName = point[1][0]
            # [5]               0            1             2           3             4            5             6
            point.append([('l', -1, 0), [0, 'c', 0], ('r', 1, 0), [0, 'c', 0], ('u', 0, -1), [0, 'c', 0], ('d', 0, 1),
                          #    7
                          [0, 'c', 0]])
            property_tape0 = point[1][2]
            if pointName != 'canister' and property_tape0 == 0:
                checkNames = ['cube', 'envelope', 'bomb', 'h_rocket', 'v_rocket']
                pointStartUp = 80
                pointStartLeftUp = 19
                pointStartDown = 114
                pointStartLeftDown = 21
                for (startUp_Down, startLeftUp_Down) in ((pointStartUp, pointStartLeftUp), (pointStartDown,
                                                                                            pointStartLeftDown)):
                    carpetExistUp_Down = 0
                    pointUp_Down = point[4][startLeftUp_Down + 26]
                    if pointUp_Down != 'X':
                        if pointUp_Down[4] == 1:
                            carpetExistUp_Down = 1
                        leftMatch = 0
                        rightMatch = 0
                        up_downMatch = 0
                        endUp_Down = startUp_Down - 31
                        for (moveUp_Down, order) in zip(range(startUp_Down, endUp_Down, -3), range(1, 13)):
                            pointFind = point[4][moveUp_Down]
                            if pointFind != 'X':
                                pointNameFind = pointFind[0]
                                if pointNameFind == pointName and up_downMatch == order - 1:
                                    up_downMatch = order
                                    if pointFind[4] == 1:
                                        carpetExistUp_Down = carpetExistUp_Down + 1
                                else:
                                    break
                            else:
                                break
                        pointNameFind = point[4][startLeftUp_Down][0]
                        if pointNameFind == pointName:
                            leftMatch = 1
                            if point[4][startLeftUp_Down][4] == 1:
                                carpetExistUp_Down = carpetExistUp_Down + 1
                            endLeftUp_Down = startLeftUp_Down - 19
                            for (moveLeft, order) in zip(range(startLeftUp_Down - 3, endLeftUp_Down, -3),
                                                         range(2, 8)):
                                pointFind = point[4][moveLeft]
                                if pointFind != 'X':
                                    pointNameFind = pointFind[0]
                                    if pointNameFind == pointName and leftMatch == order - 1:
                                        leftMatch = order
                                        if pointFind[4] == 1:
                                            carpetExistUp_Down = carpetExistUp_Down + 1
                                    else:
                                        break
                                else:
                                    break
                        pointNameFind = point[4][startLeftUp_Down + 22][0]
                        if pointNameFind == pointName:
                            rightMatch = 1
                            if point[4][startLeftUp_Down + 22][4] == 1:
                                carpetExistUp_Down = carpetExistUp_Down + 1
                            endUp_DownRight = startLeftUp_Down + 3
                            for (moveRight, order) in zip(range(startLeftUp_Down + 19, endUp_DownRight, -3),
                                                          range(2, 8)):
                                pointFind = point[4][moveRight]
                                if pointFind != 'X':
                                    pointNameFind = pointFind[0]
                                    if pointNameFind == pointName and rightMatch == order - 1:
                                        rightMatch = order
                                        if pointFind[4] == 1:
                                            carpetExistUp_Down = carpetExistUp_Down + 1
                                    else:
                                        break
                                else:
                                    break
                        if pointName in checkNames:
                            directionUp_Down = 3
                        elif leftMatch + rightMatch >= up_downMatch:
                            directionUp_Down = leftMatch + rightMatch + 1
                        else:
                            directionUp_Down = up_downMatch + 1
                        point[5][startLeftUp_Down - 14][0] = directionUp_Down
                        if directionUp_Down != carpetExistUp_Down and directionUp_Down >= 3:
                            point[5][startLeftUp_Down - 14][2] = carpetExistUp_Down
                        if directionUp_Down >= 3:
                            if startLeftUp_Down == 19:
                                aprox = 5
                            else:
                                aprox = -20
                            directionLetter = point[5][startLeftUp_Down - 15][0]
                            cv.putText(screenshot, directionLetter + str(directionUp_Down) +
                                       point[5][startLeftUp_Down - 14][1] + str(point[5][startLeftUp_Down - 14][2]),
                                       (point[0][0] + aprox, point[0][1] - 5), cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
                pointStartLeft = 17
                pointStartRight = 39
                pointStartLeftUp2 = 79
                pointStartRightUp2 = 81
                for (startLeft_Right, startLeft_RightUp2) in ((pointStartLeft, pointStartLeftUp2),
                                                              (pointStartRight, pointStartRightUp2)):
                    carpetExistLeft_Right = 0
                    carpetExistUp_Down = 0
                    pointLeft_Right = point[4][startLeft_Right + 3]
                    if pointLeft_Right != 'X':
                        if pointLeft_Right[4] == 1:
                            carpetExistLeft_Right = 1
                        upMatch = 0
                        downMatch = 0
                        left_rightMatch = 0
                        endLeft_Right = startLeft_Right - 16
                        for (moveLeft_Right, order) in zip(range(startLeft_Right, endLeft_Right, -3), range(1, 8)):
                            pointFind = point[4][moveLeft_Right]
                            if pointFind != 'X':
                                pointNameFind = pointFind[0]
                                if pointNameFind == pointName and left_rightMatch == order - 1:
                                    left_rightMatch = order
                                    if pointFind[4] == 1:
                                        carpetExistLeft_Right = carpetExistLeft_Right + 1
                                else:
                                    break
                            else:
                                break
                        pointNameFind = point[4][startLeft_Right + 2][0]
                        if pointNameFind == pointName:
                            upMatch = 1
                            if point[4][startLeft_Right + 2][4] == 1:
                                carpetExistLeft_Right = carpetExistLeft_Right + 1
                            endLeft_RightUp2 = startLeft_RightUp2 - 31
                            for (moveUp, order) in zip(range(startLeft_RightUp2, endLeft_RightUp2, -3),
                                                       range(2, 8)):
                                pointFind = point[4][moveUp]
                                if pointFind != 'X':
                                    pointNameFind = pointFind[0]
                                    if pointNameFind == pointName and upMatch == order - 1:
                                        upMatch = order
                                        if pointFind[4] == 1:
                                            carpetExistUp_Down = carpetExistUp_Down + 1
                                    else:
                                        break
                                else:
                                    break
                        pointNameFind = point[4][startLeft_Right + 4][0]
                        if pointNameFind == pointName:
                            downMatch = 1
                            if point[4][startLeft_Right + 4][4] == 1:
                                carpetExistUp_Down = carpetExistUp_Down + 1
                            startLeft_RightDown2 = startLeft_RightUp2 + 34
                            endLeft_RightDown2 = startLeft_RightUp2 + 3
                            for (moveDown, order) in zip(range(startLeft_RightDown2, endLeft_RightDown2, -3),
                                                         range(2, 8)):
                                pointFind = point[4][moveDown]
                                if pointFind != 'X':
                                    pointNameFind = pointFind[0]
                                    if pointNameFind == pointName and downMatch == order - 1:
                                        downMatch = order
                                        if pointFind[4] == 1:
                                            carpetExistUp_Down = carpetExistUp_Down + 1
                                    else:
                                        break
                                else:
                                    break
                        if pointName in checkNames:
                            directionLeft_Right = 3
                        elif upMatch + downMatch >= left_rightMatch:
                            directionLeft_Right = upMatch + downMatch + 1
                            carpetExistLeft_Right = carpetExistUp_Down
                        else:
                            directionLeft_Right = left_rightMatch + 1
                        point[5][startLeft_RightUp2 - 78][0] = directionLeft_Right
                        if directionLeft_Right != carpetExistLeft_Right and directionLeft_Right >= 3:
                            point[5][startLeft_RightUp2 - 78][2] = carpetExistLeft_Right
                        if directionLeft_Right >= 3:
                            directionLetter = point[5][startLeft_RightUp2 - 79][0]
                            cv.putText(screenshot, directionLetter + str(directionLeft_Right) +
                                       point[5][startLeft_RightUp2 - 78][1] + str(point[5][startLeft_RightUp2 - 78][2]),
                                       (point[0][0], point[0][1] + startLeft_Right // 2),
                                       cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
        chance_points = []
        for position in range(1, 8, 2):
            # print(points)
            xy, name, _, rc, _, chances = max(points, key=lambda l: (l[5][position][2], l[5][position][0], l[3][1]))
            print(f'xy, name, _, rc, _, chances {xy, name, _, rc, _, chances}')
            direction = chances[position - 1]
            numberMatch = chances[position][0]
            numberCarpet = chances[position][2]
            chance_points.append([xy, name, rc, direction, numberMatch, numberCarpet])
            print(f' max_point {[xy, name, rc, direction, numberMatch, numberCarpet]}')
        max_combo = max(chance_points, key=lambda l: (l[5], l[4], l[2][1]))
        print(f' max_combo {max_combo}')
        # before_bot_action(max_combo, max_combo[3][1], max_combo[3][2])
        cv.putText(screenshot, max_combo[3][0], (max_combo[0]),
                   cv.FONT_HERSHEY_SIMPLEX, .8, (255, 255, 255))
        # except IndexError or TypeError or ValueError:
        #     # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
        #     #            screenshot)
        #     print(IndexError or TypeError or ValueError)
        #     continue
    cv.imshow('Map', screenshot)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
