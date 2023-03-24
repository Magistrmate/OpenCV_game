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


def numberMatch(passDirection, directionMatch, tapeMatch, carpetMatch, approxX, approxY):
    point[5][passDirection][0] = directionMatch
    point[5][passDirection][2] = tapeMatch
    point[5][passDirection][4] = carpetMatch
    if directionMatch >= 3:
        directionLetter = point[5][passDirection - 1][0]
        cv.putText(screenshot, directionLetter + str(directionMatch) + point[5][passDirection][1] +
                   str(point[5][passDirection][2]) + point[5][passDirection][3] +
                   str(point[5][passDirection][4]), (point[0][0] - approxX, point[0][1] - approxY),
                   cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))

#              1           2           3           4            5               6                     7                 8                      9                         10           11      12          13           14
#         45,47,20,42|5,7,1,3       80,114,17,39|50,84,2,24|19,43,21,41    41,21,19,43       16,40,113,81          38,18,79,115           1,25,83,51          23,3,49,85           20,20,16,18|12,-18,-8,2|
def match(pointMove, passDirection, pointStart, pointEnd, pointAcrossLeft, pointAcrossRight, pointStartAcrossLeft, pointStartAcrossRight, pointEndAcrossLeft, pointEndAcrossRight, approxX, approxY, cornerEnvelope, rocketSide,
          sideTape=0, sideCarpet=0, frontTape=0, tapeMatch=0, leftMatch=0, rightMatch=0, frontMatch=0,
          envelopeMatchLeft=0, envelopeMatchRight=0, envelopeTapeLeft=0, envelopeTapeRight=0, envelopeCarpetLeft=0,
          envelopeCarpetRight=0, rocketTape=0, rocketCarpet=0):
    pointMove = point[4][pointMove]  # 45, 47, 20, 42
    pointMoveName = pointMove[0]
    if pointMoveName != '':
        pointMoveTape = pointMove[2]
        pointMoveCarpet = pointMove[4]
        pointMovePlus = pointMove[8]
        if pointMoveTape == 0:
            frontCarpet = pointMoveCarpet
            if pointPlus and pointMovePlus and pointName != pointMoveName:
                #    5 or 7 or 1 or 3
                point[5][passDirection][6] = True
            else:
                for (pointMiddleNumber, order) in zip(range(pointStart, pointEnd - 1, -3), range(1, 10)):
                    pointMiddle = point[4][pointMiddleNumber]
                    pointMiddleName = pointMiddle[0]
                    pointMiddleTape = pointMiddle[2]
                    pointMiddleCarpet = pointMiddle[4]
                    if pointMiddleName == pointName and frontMatch == order - 1:
                        frontMatch = order
                        frontTape = pointMiddleTape
                        frontCarpet = frontCarpet + pointMiddleCarpet
                        if order == 1:
                            envelopeMatchLeft = envelopeMatchRight = 1
                            pointEnvelopeLeft = point[4][pointMiddleNumber - cornerEnvelope]  # 79 or 18 or 113 or 38
                            pointEnvelopeNameLeft = pointEnvelopeLeft[0]
                            pointEnvelopeTapeLeft = pointEnvelopeLeft[2]
                            pointEnvelopeCarpetLeft = pointEnvelopeLeft[4]
                            pointEnvelopeRight = point[4][pointMiddleNumber + cornerEnvelope]  # 81 or 16 or 115 or 40
                            pointEnvelopeNameRight = pointEnvelopeRight[0]
                            pointEnvelopeTapeRight = pointEnvelopeRight[2]
                            pointEnvelopeCarpetRight = pointEnvelopeRight[4]
                            if pointEnvelopeNameLeft == pointName:
                                envelopeMatchLeft = envelopeMatchLeft + 1
                                envelopeTapeLeft = pointEnvelopeTapeLeft
                                envelopeCarpetLeft = pointEnvelopeCarpetLeft
                            if pointEnvelopeNameRight == pointName:
                                envelopeMatchRight = envelopeMatchRight + 1
                                envelopeTapeRight = pointEnvelopeTapeRight
                                envelopeCarpetRight = pointEnvelopeCarpetRight
                    else:
                        break
            #       19,43,21,41          16,40,113,81            1,25,83,51
            #       41,21,19,43          38,18,79, 115           23,3,49,85
            for (pointAcrossNumber, pointStartAcrossNumber, pointEndAcrossNumber) in \
                    (pointAcrossLeft, pointStartAcrossLeft, pointEndAcrossLeft), \
                    (pointAcrossRight, pointStartAcrossRight, pointEndAcrossRight):
                pointAcross = point[4][pointAcrossNumber]
                pointNameAcross = pointAcross[0]
                pointTapeAcross = pointAcross[2]
                pointCarpetAcross = pointAcross[4]
                if pointNameAcross == pointName or pointName == 'envelope':
                    if pointAcrossNumber == pointAcrossLeft:
                        leftMatch = 1
                        envelopeMatchLeft = envelopeMatchLeft + 1
                        envelopeTapeLeft = envelopeTapeLeft + pointTapeAcross
                        envelopeCarpetLeft = envelopeCarpetLeft + pointCarpetAcross
                    elif pointAcrossNumber == pointAcrossRight:
                        rightMatch = 1
                        envelopeMatchRight = envelopeMatchRight + 1
                        envelopeTapeRight = envelopeTapeRight + pointTapeAcross
                        envelopeCarpetRight = envelopeCarpetRight + pointCarpetAcross
                    sideTape = sideTape + pointTapeAcross
                    sideCarpet = sideCarpet + pointCarpetAcross
                    envelopeTape = sideTape + pointTapeAcross
                    envelopeCarpet = sideCarpet + pointMiddleCarpet
                    #                                          16,40,113,81            1,25,83,51
                    #                                          38,18,79, 115          23,3, 49,85
                    for (pointMiddle, order) in zip(range(pointStartAcrossNumber, pointEndAcrossNumber - 1, -3),
                                                    range(2, 6)):
                        pointMiddle = point[4][pointMiddle]  # (16 or 38) or (18 or 40)
                        pointMiddleName = pointMiddle[0]
                        pointMiddleTape = pointMiddle[2]
                        pointMiddleCarpet = pointMiddle[4]
                        if pointMiddleName == pointName:
                            if leftMatch == order - 1:
                                leftMatch = order
                            elif rightMatch == order - 1:
                                rightMatch = order
                            sideTape = sideTape + pointMiddleTape
                            sideCarpet = sideCarpet + pointMiddleCarpet
                        rocketTape = envelopeTape + pointMiddleTape
                        rocketCarpet = envelopeCarpet + pointMiddleCarpet
            if pointPlus and pointPlus != pointMovePlus and pointName != rocketSide:
                directionMatch = 5
                tapeMatch = rocketTape
                carpetMatch = rocketCarpet
            elif envelopeMatchLeft == 3 or envelopeMatchRight == 3:
                directionMatch = 4
                if envelopeMatchLeft == 3:
                    tapeMatch = envelopeTapeLeft
                    carpetMatch = envelopeCarpetLeft
                else:
                    tapeMatch = envelopeTapeRight
                    carpetMatch = envelopeCarpetRight
                # tapeMatch = envelopeTape
                # carpetMatch = envelopeCarpet
            elif leftMatch + rightMatch >= frontMatch:
                directionMatch = leftMatch + rightMatch + 1
                if directionMatch >= 3:
                    tapeMatch = sideTape
                carpetMatch = sideCarpet
            else:
                directionMatch = frontMatch + 1
                if directionMatch >= 3:
                    tapeMatch = frontTape
                carpetMatch = frontCarpet
            if carpetMatch != 0 and carpetMatch < directionMatch and directionMatch >= 3 and pointName != 'v_rocket':
                carpetMatch = directionMatch - frontCarpet
            point[5][passDirection][0] = directionMatch
            point[5][passDirection][2] = tapeMatch
            point[5][passDirection][4] = carpetMatch
            if directionMatch >= 3:
                directionLetter = point[5][passDirection - 1][0]
                cv.putText(screenshot, directionLetter + str(directionMatch) + point[5][passDirection][1] +
                           str(point[5][passDirection][2]) + point[5][passDirection][3] +
                           str(point[5][passDirection][4]), (point[0][0] - approxX, point[0][1] - approxY),
                           cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))


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
                   ('canister', (200, 200, 200), .85, .9, .65, .76, False)]
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
        # try:
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
        for point in points:
            pointName = point[1][0]
            point.append([('l', -1, 0), [0, 't', 0, 'c', 0, 'p', False],
                          ('r', 1, 0), [0, 't', 0, 'c', 0, 'p', False],
                          ('u', 0, -1), [0, 't', 0, 'c', 0, 'p', False],
                          ('d', 0, 1), [0, 't', 0, 'c', 0, 'p', False],
                          ('n', 0, 0), [0, 't', 0, 'c', 0, 'p', False]])
            pointTape = point[1][2]
            pointPlus = point[1][8]
            if pointName != 'canister' and pointTape == 0:
                pointStartUp = 80
                pointStartDown = 114
                pointEndUp = 50
                pointEndDown = 84
                pointEndLeft = 2
                pointEndRight = 24
                pointUpLeft = 19
                pointUpRight = 41
                pointDownLeft = 21
                pointDownRight = 43
                pointStartLeft = 17
                pointStartRight = 39
                #      1  2       3               4              5               6                7                        8                 9                    10         11  12   13      14
                match(45, 5, pointStartUp,    pointEndUp,    pointUpLeft,    pointUpRight,   pointStartLeft - 1, pointStartRight - 1,  pointEndLeft - 1,  pointEndRight - 1, 20, 12,  1,  'v_rocket')
                match(47, 7, pointStartDown,  pointEndDown,  pointDownRight, pointDownLeft,  pointStartRight + 1,  pointStartLeft + 1, pointEndRight + 1, pointEndLeft + 1,  20, -18, -1, 'v_rocket')
                match(20, 1, pointStartLeft,  pointEndLeft,  pointDownLeft,  pointUpLeft,    pointStartDown - 1,  pointStartUp - 1,    pointEndDown - 1,  pointEndUp - 1,    16, -8,  -1, 'h_rocket')
                match(42, 3, pointStartRight, pointEndRight, pointUpRight,   pointDownRight, pointStartUp + 1,    pointStartDown + 1,  pointEndUp + 1,    pointEndDown + 1,  18,  2,  1,  'h_rocket')
                # match(0, 9, pointStartLeft, pointEndRight, pointUpRight, pointDownRight, pointStartUp + 1,
                #       pointStartDown + 1, pointEndUp + 1, pointEndDown + 1, 18, 2, 1, '')
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
        # before_bot_action(max_combo, max_combo[3][1], max_combo[3][2])
        cv.putText(screenshot, max_combo[3][0], (max_combo[0]),
                   cv.FONT_HERSHEY_SIMPLEX, .8, (255, 255, 255))
        # except IndexError or TypeError or ValueError:
        #     print(IndexError or TypeError or ValueError)
        #     continue
    cv.imshow('Map', screenshot)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
