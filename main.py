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
                            # if [(x, y), (name, 't', 0, 'c', 0, 'g', 0), color, (column, row)] in points:
                            #     print(points)
                            #     print(point)
                            #     points.pop(index)
                            #     print(points)
                            # else:
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
        # pointCheck = points[3]
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
            # [5]               0       1        2      3        4       5        6      7
            point.append([('l', -1, 0), 0, ('r', 1, 0), 0, ('u', 0, -1), 0, ('d', 0, 1), 0])
            property_tape = point[1][2]
            if pointName != 'canister' and property_tape == 0:
                checkNames = ['cube', 'envelope', 'bomb', 'h_rocket', 'v_rocket']
                up2 = 80
                up1Left1 = 19
                down2 = 114
                down1Left1 = 21
                for (a, b) in ((up2, up1Left1), (down2, down1Left1)):
                    up1_down1 = point[4][b + 26]
                    property_tape = up1_down1[2]
                    if up1_down1 != 'X' and property_tape == 0:
                        # print(f'{point}\n {point[4][b + 26][2]}')
                        carpet = 0
                        carpet0 = 0
                        property_carpet = up1_down1[4]
                        if property_carpet == 1:
                            carpet0 = 1
                        if pointName not in checkNames:
                            left = 0
                            right = 0
                            up_down = 0
                            for (c, d) in zip(range(a, a - 31, -3), range(1, 8)):
                                property_carpet = point[4][c][4]
                                if property_carpet == 1:
                                    carpet = carpet + 1
                                if point[4][c][0] == pointName and up_down == d - 1:
                                    up_down = d + carpet
                                else:
                                    break
                            if point[4][b][0] == pointName:
                                left = 1
                                carpet = 0
                                for (c, d) in zip(range(b - 3, b - 19, -3), range(2, 8)):
                                    if point[4][c][4] == 1:
                                        carpet = carpet + 1
                                    if point[4][c][0] == pointName and left == d - 1:
                                        left = d + carpet
                                    else:
                                        break
                            if point[4][b + 22][0] == pointName:
                                right = 1
                                carpet = 0
                                for (c, d) in zip(range(b + 19, b + 3, -3), range(2, 8)):
                                    if point[4][c][4] == 1:
                                        carpet = carpet + 1
                                    if point[4][c][0] == pointName and right == d - 1:
                                        right = d + carpet
                                    else:
                                        break
                            if left + right + carpet >= up_down + carpet:
                                point[5][b - 14] = left + right + 1 + carpet
                            else:
                                point[5][b - 14] = up_down + 1 + carpet
                        else:
                            point[5][b - 14] = 3 + carpet
                        if point[5][b - 14] >= 3:
                            if b == 19:
                                c = 5
                            else:
                                c = -15
                            cv.putText(screenshot, point[5][b - 15][0] + str(point[5][b - 14]),
                                       (point[0][0] + c, point[0][1] - 5), cv.FONT_HERSHEY_SIMPLEX, .4,
                                       (0, 0, 0))
                for (side, see) in ((17, 79), (39, 81)):
                    if point[4][side + 3] != 'X' and point[4][side + 3][2] == 0:
                        if pointName not in checkNames:
                            left_right = 0
                            up = 0
                            down = 0
                            for (c, d) in zip(range(side, side - 16, -3), range(1, 8)):
                                if point[4][c][0] == pointName and left_right == d - 1:
                                    left_right = d
                                else:
                                    break
                            if point[4][side + 2][0] == pointName:
                                up = 1
                                for (c, d) in zip(range(see, see - 31, -3), range(2, 8)):
                                    if point[4][c][0] == pointName and up == d - 1:
                                        up = d
                                    else:
                                        break
                            if point[4][side + 4][0] == pointName:
                                down = 1
                                for (c, d) in zip(range(see + 34, see + 5, -3), range(2, 8)):
                                    if point[4][c][0] == pointName and down == d - 1:
                                        down = d
                                    else:
                                        break
                            if up + down >= left_right:
                                point[5][see - 78] = up + down + 1
                            else:
                                point[5][see - 78] = left_right + 1
                        else:
                            point[5][see - 78] = 3
                        if point[5][see - 78] >= 3:
                            cv.putText(screenshot, point[5][see - 79][0] + str(point[5][see - 78]),
                                       (point[0][0], point[0][1] + side // 2), cv.FONT_HERSHEY_SIMPLEX, .4,
                                       (0, 0, 0))
        chance_points = []
        for position in range(1, 8, 2):
            xy, name, _, rc, _, chances = max(points, key=lambda l: (l[5][position], l[3][1]))
            direction = chances[-1 + position]
            number = chances[0 + position]
            chance_points.append([xy, name, rc, direction, number])
            # print(f' max_point {[xy, name, rc, direction, number]}')
        max_combo = max(chance_points, key=lambda l: (l[4], l[2][1]))
        # print(f' max_combo {max_combo}')
        # before_bot_action(max_combo, max_combo[3][1], max_combo[3][2])
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
