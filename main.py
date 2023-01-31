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
    sleep(1)
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
    namesColors = [('duck', (0, 191, 255)), ('chip', (0, 0, 255)), ('ball', (0, 255, 0)),
                   ('backpack', (255, 0, 0)), ('backpack', (255, 0, 0)), ('spruce', (0, 128, 0)),
                   ('egg', (255, 0, 139)), ('canister', (99, 103, 106)), ('h_rocket', (145, 101, 214)),
                   ('v_rocket', (145, 101, 214)), ('cube', (57, 138, 250)), ('envelope', (103, 90, 231)),
                   ('bomb', (169, 133, 247))]
    # namesColors = [('chip', (0, 0, 255))]
    for (name, color) in namesColors:
        Picture(name, color, screenshot, points)
    if len(points) > 0:
        (first_point_for_x, _), _, _ = min(points, key=lambda l: l[0][0])
        (last_point_for_x, _), _, _ = max(points, key=lambda l: l[0][0])
        (_, first_point_for_y), _, _ = min(points, key=lambda l: l[0][1])
        (_, last_point_for_y), _, _ = max(points, key=lambda l: l[0][1])
        for (index, point) in enumerate(points):
            x = point[0][0]
            y = point[0][1]
            name = point[1][0]
            properties = point[1][1]
            color = point[2]
            for (x0, column) in zip(range(first_point_for_x - 5, last_point_for_x + 5, 51), range(1, 9)):
                if x0 <= x <= (x0 + 50):
                    for (y0, row) in zip(range(first_point_for_y - 10, last_point_for_y + 5, 51), range(1, 11)):
                        if y0 <= y <= (y0 + 50):
                            points[index].append((column, row))
                            cv.putText(screenshot, str(column) + " " + str(row), (x - 20, y - 20),
                                       cv.FONT_HERSHEY_SIMPLEX, .4, color)
                            cv.putText(screenshot, name, (x - 20, y - 10),
                                       cv.FONT_HERSHEY_SIMPLEX, .4, color)
                            cv.putText(screenshot, properties, (x - 20, y),
                                       cv.FONT_HERSHEY_SIMPLEX, .4, color)
        try:
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
                pointName = point[1]
                for pointFind in points:
                    pointColumnFind = pointFind[3][0]
                    pointRowFind = pointFind[3][1]
                    pointNameFind = pointFind[1]
                    x = pointColumnFind - pointColumn
                    y = pointRowFind - pointRow
                    if -7 <= x <= 7 and -12 <= y <= 12:
                        if x == 0 and (y == 1 or y == -1):
                            point[4][46 + y] = pointNameFind
                        if (-7 <= x <= -1 or 1 <= x <= 7) and -1 <= y <= 1:
                            for (m, d) in zip((1, -1), (0, 10)):
                                for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
                                    if c == x:
                                        point[4][m + x + y + n] = pointNameFind
                                        break
                        if -1 <= x <= 1 and (-12 <= y <= -2 or 2 <= y <= 12):
                            for (m, d) in zip((1, -1), (0, 12)):
                                for (r, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
                                    if r == y:
                                        point[4][m + x + y + n] = pointNameFind
                                        break

            # print('FPS {}'.format(1 / (time() - loop_time)))
            # loop_time = time()
            # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
            #            screenshot)
            # pointCheck = points[3]
            # pointCheck = points[random.randint(0, len(points))]
            # print(pointCheck)
            # cv.putText(screenshot, pointCheck[1], (pointCheck[0][0], pointCheck[0][1]), cv.FONT_HERSHEY_DUPLEX,
            #            .6, pointCheck[2])
            # cv.putText(screenshot, pointCheck[4][45], (pointCheck[0][0], pointCheck[0][1] - 50),
            #            cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
            # cv.putText(screenshot, pointCheck[4][47], (pointCheck[0][0], pointCheck[0][1] + 50),
            #            cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
            # for (m, d) in zip((1, -1), (0, 10)):
            #     for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
            #         for r in range(-1, 2, 1):
            #             cv.putText(screenshot, pointCheck[4][m + c + r + n], (pointCheck[0][0] + c * 50,
            #                                                                   pointCheck[0][1] + r * 50),
            #                        cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
            # for (m, d) in zip((1, -1), (0, 12)):
            #     for (c, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
            #         for r in range(-1, 2, 1):
            #             cv.putText(screenshot, pointCheck[4][m + c + r + n], (pointCheck[0][0] + r * 50,
            #                                                                   pointCheck[0][1] + c * 50),
            #                        cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
            # sleep(1)
            for point in points:
                pointName = point[1]
                # [5]               0       1        2      3        4       5        6      7
                point.append([('l', -1, 0), 0, ('r', 1, 0), 0, ('u', 0, -1), 0, ('d', 0, 1), 0])
                if pointName != 'canister':
                    checkNames = ['cube', 'envelope', 'bomb', 'h_rocket', 'v_rocket']
                    for (stage, floor) in ((80, 19), (114, 21)):
                        if point[4][floor + 26] != 'X':
                            if pointName not in checkNames:
                                left = 0
                                right = 0
                                up_down = 0
                                for (a, b) in zip(range(stage, stage - 31, -3), range(1, 8)):
                                    if point[4][a] == pointName and up_down == b - 1:
                                        up_down = b
                                    else:
                                        break
                                if point[4][floor] == pointName:
                                    left = 1
                                    for (a, b) in zip(range(floor - 3, floor - 19, -3), range(2, 8)):
                                        if point[4][a] == pointName and left == b - 1:
                                            left = b
                                        else:
                                            break
                                if point[4][floor + 22] == pointName:
                                    right = 1
                                    for (a, b) in zip(range(floor + 19, floor + 3, -3), range(2, 8)):
                                        if point[4][a] == pointName and right == b - 1:
                                            right = b
                                        else:
                                            break
                                if left + right >= up_down:
                                    point[5][floor - 14] = left + right + 1
                                else:
                                    point[5][floor - 14] = up_down + 1
                            else:
                                point[5][floor - 14] = 3
                            # if point[5][floor - 14] >= 3:
                            #     if floor == 19:
                            #         a = 5
                            #     else:
                            #         a = -15
                            #     cv.putText(screenshot, point[5][floor - 15][0] + str(point[5][floor - 14]),
                            #                (point[0][0] + a, point[0][1] - 5), cv.FONT_HERSHEY_SIMPLEX, .4,
                            #                (0, 0, 0))
                    for (side, see) in ((17, 79), (39, 81)):
                        if point[4][side + 3] != 'X':
                            if pointName not in checkNames:
                                left_right = 0
                                up = 0
                                down = 0
                                for (a, b) in zip(range(side, side - 16, -3), range(1, 8)):
                                    if point[4][a] == pointName and left_right == b - 1:
                                        left_right = b
                                    else:
                                        break
                                if point[4][side + 2] == pointName:
                                    up = 1
                                    for (a, b) in zip(range(see, see - 31, -3), range(2, 8)):
                                        if point[4][a] == pointName and up == b - 1:
                                            up = b
                                        else:
                                            break
                                if point[4][side + 4] == pointName:
                                    down = 1
                                    for (a, b) in zip(range(see + 34, see + 5, -3), range(2, 8)):
                                        if point[4][a] == pointName and down == b - 1:
                                            down = b
                                        else:
                                            break
                                if up + down >= left_right:
                                    point[5][see - 78] = up + down + 1
                                else:
                                    point[5][see - 78] = left_right + 1
                            else:
                                point[5][see - 78] = 3
                            # if point[5][see - 78] >= 3:
                            #     cv.putText(screenshot, point[5][see - 79][0] + str(point[5][see - 78]),
                            #                (point[0][0], point[0][1] + side // 2), cv.FONT_HERSHEY_SIMPLEX, .4,
                            #                (0, 0, 0))
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
        except IndexError or TypeError or ValueError:
            # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
            #            screenshot)
            print(IndexError or TypeError or ValueError)
            continue
    cv.imshow('Map', screenshot)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
