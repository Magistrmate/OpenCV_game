import operator
import random
import traceback

import numpy as np
from Picture import Picture
import cv2 as cv
from time import time, sleep
import time
from datetime import datetime
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
    subprocess.Popen([r'C:\Users\\retro\Downloads\scrcpy-win64-v1.24\scrcpy.exe', '-S', '-w', '--window-x=1500',
                      '--window-y=90', '--tcpip=192.168.1.77'])
    sleep(5)

wincap = WindowCapture('22071212AG')
is_bot_in_action = False
countdown_start = False
bot = False
countdown_in_action = False
botCapture = 'off'
TIMER = int(10)


def bot_action(target, one, two):
    global botCapture
    if botCapture != 'off':
        pydirectinput.moveTo(target[0], target[1])
        if one == 0 and two == 0:
            pydirectinput.doubleClick()
        else:
            pydirectinput.mouseDown()
            pydirectinput.moveTo(target[0] + 50 * one, target[1] + 50 * two)
            pydirectinput.mouseUp()
    global TIMER
    TIMER = 10
    AxisX = AxisX0 = 530
    AxisY = 1602
    prev = time.time()
    while TIMER >= 0:
        if botCapture != 'off':
            if botCapture == 'click now':
                break
            else:
                cv.rectangle(screenshot, (263, 799), (317, 818), (0, 0, 0), 1)
                cv.rectangle(screenshot, (AxisX0, AxisY), (AxisX, AxisY + 30), (255, 255, 255), cv.FILLED, cv.FILLED, 1)
                cur = time.time()
                if cur - prev >= 1:
                    prev = cur
                    TIMER = TIMER - 1
                    AxisX = AxisX + 10
        else:
            break
    global is_bot_in_action
    is_bot_in_action = False


def before_bot_action(point_target, one, two):
    global is_bot_in_action
    target_click = wincap.get_screen_position(point_target[0])
    if not is_bot_in_action:
        is_bot_in_action = True
        t = Thread(target=bot_action, args=(target_click, one, two))
        t.start()


def matchNull(pointStart, pointLeftEnd, pointRightStart, pointEnd, stepOne, stepTwo, tapeMatchNull=0, carpetMatchNull=0,
              directionMatchNull=0, pointNoCarpet=0):
    for (pointStart, pointEnd, step) in zip((pointStart, pointRightStart), (pointLeftEnd, pointEnd),
                                            (stepOne, stepTwo)):
        for pointMiddleNumber in range(pointStart, pointEnd, step):
            pointMiddle = point[3][pointMiddleNumber]
            pointMiddleName = pointMiddle[0]
            pointMiddleTape = pointMiddle[2]
            pointMiddleCarpet = pointMiddle[4]
            if pointMiddleName != '':
                tapeMatchNull = tapeMatchNull + pointMiddleTape
                if pointMiddleCarpet == 0:
                    pointNoCarpet = pointNoCarpet + 1
                if pointCarpet == 1:
                    carpetMatchNull = pointNoCarpet
                directionMatchNull = directionMatchNull + 1
    if pointName == 'v_rocket' or pointName == 'envelope':
        for pointMoveUpDownNumber in moveUp, moveDown:
            pointMiddle = point[3][pointMoveUpDownNumber]
            pointMiddleName = pointMiddle[0]
            pointMiddleTape = pointMiddle[2]
            pointMiddleCarpet = pointMiddle[4]
            if pointMiddleName != '':
                tapeMatchNull = tapeMatchNull + pointMiddleTape
                if pointMiddleCarpet == 0:
                    pointNoCarpet = pointNoCarpet + 1
                if pointCarpet == 1:
                    carpetMatchNull = pointNoCarpet
                directionMatchNull = directionMatchNull + 1
    else:
        directionMatchNull = 5
    point[4][9][0] = directionMatchNull
    point[4][9][2] = tapeMatchNull
    point[4][9][4] = carpetMatchNull
    directionLetter = point[4][8][0]
    cv.putText(screenshot, directionLetter + str(directionMatchNull) + point[4][9][1] +
               str(point[4][9][2]) + point[4][9][3] + str(point[4][9][4]),
               (point[0][0] - 20, point[0][1] + 2), cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))


def match(pointMoveNumber, passDirection, pointStart, pointEnd, pointAcrossLeft, pointAcrossRight, pointStartAcrossLeft,
          pointStartAcrossRight, pointEndAcrossLeft, pointEndAcrossRight, approxX, approxY, cornerEnvelope, rocketSide,
          sideTape=0, sideCarpet=0, frontCarpet=0, frontTape=0, tapeMatch=0, carpetMatch=0, leftMatch=0, rightMatch=0,
          frontMatch=0, envelopeMatchLeft=0, envelopeMatchRight=0, envelopeTape=0, envelopeTapeLeft=0,
          envelopeTapeRight=0, envelopeCarpetLeft=0, envelopeCarpetRight=0, rocketTape=0, canisterMatch=0,
          rocket=False, border_h=3, border_a=3, rocketNoCarpet=0,  pointsMatch=2, rocketCarpetPass=False,
          rocketCarpet=0):
    pointMove = point[3][pointMoveNumber]  # 45, 47, 20, 42
    pointMoveName = pointMove[0]
    if pointMoveName != '' and not (pointMoveName == 'canister' and pointName == 'cube'):
        pointMoveTape = pointMove[2]
        pointMoveCarpet = pointMove[4]
        pointMovePlus = pointMove[8]
        if pointMoveTape == 0:
            if pointPlus and pointMovePlus and not ('rocket' in (pointName and pointMoveName)):
                #    5 or 7 or 1 or 3
                point[4][passDirection][6] = True
            else:
                if 'rocket' in pointName:
                    rocket = True
                    border_h = 1
                    border_a = 13
                for (pointMiddleNumber, order) in zip(range(pointStart, pointEnd - 1, -3), range(1, border_h)):
                    pointMiddle = point[3][pointMiddleNumber]
                    pointMiddleName = pointMiddle[0]
                    pointMiddleTape = pointMiddle[2]
                    pointMiddleCarpet = pointMiddle[4]
                    if pointMiddleName == pointName and frontMatch == order - 1:
                        frontMatch = order
                        frontTape = pointMiddleTape
                        frontCarpet = frontCarpet + pointMiddleCarpet
                        if order == 1:
                            envelopeMatchLeft = envelopeMatchRight = 1
                            pointEnvelopeLeft = point[3][pointMiddleNumber - cornerEnvelope]  # 79 or 18 or 113 or 38
                            pointEnvelopeNameLeft = pointEnvelopeLeft[0]
                            pointEnvelopeTapeLeft = pointEnvelopeLeft[2]
                            pointEnvelopeCarpetLeft = pointEnvelopeLeft[4]
                            pointEnvelopeRight = point[3][pointMiddleNumber + cornerEnvelope]  # 81 or 16 or 115 or 40
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
                pointAcross = point[3][pointAcrossNumber]
                pointNameAcross = pointAcross[0]
                pointTapeAcross = pointAcross[2]
                pointCarpetAcross = pointAcross[4]
                if pointCarpetAcross == 0 and pointMoveCarpet == 1:
                    rocketNoCarpet = 1
                if pointNameAcross == pointName or pointName == 'envelope' or rocket:
                    if rocket is False:
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
                    #                                          16,40,113,81            1,25,83,51
                    #                                          38,18,79, 115          23,3, 49,85
                    for (pointMiddleNumber, order) in zip(range(pointStartAcrossNumber, pointEndAcrossNumber - 1, -3),
                                                          range(2, border_a)):
                        pointMiddle = point[3][pointMiddleNumber]
                        pointMiddleName = pointMiddle[0]
                        if pointMiddleName != '':
                            pointMiddleTape = pointMiddle[2]
                            pointMiddleCarpet = pointMiddle[4]
                            if pointMiddleName == pointName:
                                if leftMatch == order - 1:
                                    leftMatch = order
                                elif rightMatch == order - 1:
                                    rightMatch = order
                                sideTape = sideTape + pointMiddleTape
                                sideCarpet = sideCarpet + pointMiddleCarpet
                            rocketTape = rocketTape + pointMiddleTape
                            if rocketCarpetPass and pointMiddleTape == 0:
                                rocketCarpet = rocketCarpet + 1
                            if pointMiddleCarpet != 0 and rocketCarpetPass is False:
                                rocketCarpetPass = True
                            pointsMatch = pointsMatch + 1
                            if pointMoveCarpet != 0 and pointMiddleCarpet == 0:
                                rocketNoCarpet = rocketNoCarpet + 1
                            if pointMiddleName == 'canister':
                                canisterMatch = canisterMatch + 1
            if pointPlus and pointName != rocketSide:
                directionMatch = 5
                if rocket:
                    if pointMoveCarpet == 0:
                        directionMatch = pointsMatch + canisterMatch
                    tapeMatch = rocketTape + sideTape
                    carpetMatch = rocketCarpet
            elif envelopeMatchLeft == 3 or envelopeMatchRight == 3:
                directionMatch = 4
                if envelopeMatchLeft == 3:
                    tapeMatch = envelopeTape
                    carpetMatch = envelopeCarpetLeft + frontCarpet + pointMoveCarpet
                else:
                    tapeMatch = envelopeTape
                    carpetMatch = envelopeCarpetRight + frontCarpet + pointMoveCarpet
            elif leftMatch + rightMatch >= frontMatch:
                directionMatch = leftMatch + rightMatch + 1
                if directionMatch >= 3:
                    tapeMatch = sideTape
                    carpetMatch = sideCarpet + pointMoveCarpet
            else:
                directionMatch = frontMatch + 1
                if directionMatch >= 3:
                    tapeMatch = frontTape
                    carpetMatch = frontCarpet + pointMoveCarpet
            if carpetMatch != 0 and carpetMatch <= directionMatch and directionMatch >= 3 and 'rocket' not in pointName:
                carpetMatch = directionMatch - carpetMatch
            point[4][passDirection][0] = directionMatch
            point[4][passDirection][2] = tapeMatch
            point[4][passDirection][4] = carpetMatch
            # if directionMatch >= 3:
            #     directionLetter = point[4][passDirection - 1][0]
            #     cv.putText(screenshot, directionLetter + str(directionMatch) + point[4][passDirection][1] +
            #                str(point[4][passDirection][2]) + point[4][passDirection][3] +
            #                str(point[4][passDirection][4]), (point[0][0] - approxX, point[0][1] - approxY),
            #                cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))


while True:
    screenshot = wincap.get_screenshot()
    cv.putText(screenshot, 'bot ' + botCapture, (150, 815), cv.FONT_HERSHEY_SIMPLEX, .8, (255, 255, 255))
    points = []
    namesColors = [('ball', .85, .85, .7, .8, False), ('backpack', .76, .85, .7, .85, False),
                   ('egg', .77, .85, .7, .85, False), ('chip', .79, .85, .74, .8, False),
                   ('duck', .85, .9, .65, .95, False), ('spruce', .76, .85, .7, .8, False),
                   ('h_rocket', .76, .85, .7, .76, True), ('v_rocket', .76, .85, .7, .76, True),
                   ('envelope', .76, .85, .7, .76, True), ('bomb', .76, .85, .65, .76, True),
                   ('cube', .85, .9, .85, .76, True), ('canister', .85, .9, .65, .76, False),
                   ('ground', .8, .9, .65, .85, False)]
    for (name, space_hold, tape_hold, carpet_hold, ground_hold, pointPlus) in namesColors:
        Picture(name, space_hold, tape_hold, carpet_hold, ground_hold, pointPlus, screenshot, points)
    if len(points) > 0:
        (first_point_for_x, _), _ = min(points, key=lambda l: l[0][0])
        (last_point_for_x, _), _ = max(points, key=lambda l: l[0][0])
        (_, first_point_for_y), _ = min(points, key=lambda l: l[0][1])
        (_, last_point_for_y), _ = max(points, key=lambda l: l[0][1])
        for (index, point) in enumerate(points):
            x = point[0][0]
            y = point[0][1]
            name = point[1][0]
            properties = f't{point[1][2]}c{point[1][4]}g{point[1][6]}'
            for (x0, column) in zip(range(first_point_for_x - 5, last_point_for_x + 5, 51), range(1, 9)):
                if x0 <= x <= (x0 + 50):
                    for (y0, row) in zip(range(first_point_for_y - 10, last_point_for_y + 5, 51), range(1, 11)):
                        if y0 <= y <= (y0 + 50):
                            points[index].append((column, row))
                            for (text, ya) in zip((f'{column} {row}', name, properties), (range(20, -1, -10))):
                                cv.putText(screenshot, text, (x - 20, y - ya), cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
        for point in points:
            # [3]           0
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
            pointColumn = point[2][0]
            pointRow = point[2][1]
            pointName = point[1][0]
            try:
                for pointFind in points:
                    pointColumnFind = pointFind[2][0]
                    pointRowFind = pointFind[2][1]
                    pointNameFind = pointFind[1][0]
                    x = pointColumnFind - pointColumn
                    y = pointRowFind - pointRow
                    if -7 <= x <= 7 and -12 <= y <= 12:
                        if x == 0 and (y == 1 or y == -1):
                            point[3][46 + y] = (pointNameFind, 't', pointFind[1][2], 'c', pointFind[1][4], 'g',
                                                pointFind[1][6], 'p', pointFind[1][8])
                        if (-7 <= x <= -1 or 1 <= x <= 7) and -1 <= y <= 1:
                            for (m, d) in zip((1, -1), (0, 10)):
                                for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
                                    if c == x:
                                        point[3][m + x + y + n] = (pointNameFind, 't', pointFind[1][2], 'c',
                                                                   pointFind[1][4], 'g', pointFind[1][6], 'p',
                                                                   pointFind[1][8])
                                        break
                        if -1 <= x <= 1 and (-12 <= y <= -2 or 2 <= y <= 12):
                            for (m, d) in zip((1, -1), (0, 12)):
                                for (r, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
                                    if r == y:
                                        point[3][m + x + y + n] = (pointNameFind, 't', pointFind[1][2], 'c',
                                                                   pointFind[1][4], 'g', pointFind[1][6], 'p',
                                                                   pointFind[1][8])
                                        break
            except IndexError or TypeError:
                continue
        for point in points:
            pointName = point[1][0]
            point.append([('l', -1, 0), [0, 't', 0, 'c', 0, 'p', False],
                          ('r', 1, 0), [0, 't', 0, 'c', 0, 'p', False],
                          ('u', 0, -1), [0, 't', 0, 'c', 0, 'p', False],
                          ('d', 0, 1), [0, 't', 0, 'c', 0, 'p', False],
                          ('n', 0, 0), [0, 't', 0, 'c', 0, 'p', False]])
            pointTape = point[1][2]
            pointCarpet = point[1][4]
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
                moveUp = 45
                moveDown = 47
                moveLeft = 20
                moveRight = 42
                noMove = 0
                if pointName == 'h_rocket':
                    matchNull(pointEndLeft, moveLeft + 1, moveRight, pointEndRight - 1, 3, -3)
                elif pointName == 'v_rocket':
                    matchNull(pointEndUp, pointStartUp + 1, pointStartDown, pointEndDown - 1, 3, -3)
                elif pointName == 'envelope' or pointName == 'bomb' or pointName == 'cube':
                    matchNull(moveLeft, moveRight, moveLeft, moveRight, 22, 22)
                match(moveUp, 5, pointStartUp, pointEndUp, pointUpLeft, pointUpRight, pointStartLeft - 1,
                      pointStartRight - 1, pointEndLeft - 1, pointEndRight - 1, 20, 18, 1, 'v_rocket')
                match(moveDown, 7, pointStartDown, pointEndDown, pointDownRight, pointDownLeft, pointStartRight + 1,
                      pointStartLeft + 1, pointEndRight + 1, pointEndLeft + 1, 20, -22, -1, 'v_rocket')
                match(moveLeft, 1, pointStartLeft, pointEndLeft, pointDownLeft, pointUpLeft, pointStartDown - 1,
                      pointStartUp - 1, pointEndDown - 1, pointEndUp - 1, 16, -12, -1, 'h_rocket')
                match(moveRight, 3, pointStartRight, pointEndRight, pointUpRight, pointDownRight, pointStartUp + 1,
                      pointStartDown + 1, pointEndUp + 1, pointEndDown + 1, 18, 8, 1, 'h_rocket')
        chance_points = []
        for position in range(1, 10, 2):
            xy, name, rc, _, chances = max(points, key=lambda l: (l[4][position][6], l[4][position][4],
                                                                  l[4][position][2], l[4][position][0], l[2][1]))
            direction = chances[position - 1]
            numberMatch = chances[position][0]
            numberTape = chances[position][2]
            numberCarpet = chances[position][4]
            numberPlus = chances[position][6]
            #                      0    1    2     3          4             5            6           7
            chance_points.append([xy, name, rc, direction, numberMatch, numberTape, numberCarpet, numberPlus])
        max_combo = max(chance_points, key=lambda l: (l[7], l[6], l[5], l[4], l[2][1]))
        if bot:
            before_bot_action(max_combo, max_combo[3][1], max_combo[3][2])
        # cv.putText(screenshot, max_combo[3][0], (max_combo[0]), cv.FONT_HERSHEY_SIMPLEX, .8, (255, 255, 255))
    if botCapture != 'off':
        if TIMER <= 2:
            botCapture = 'click'
        else:
            botCapture = 'wait'
    cv.imshow('Map', screenshot)
    key = cv.waitKey(1)
    if key != -1:
        if key == ord('q'):
            cv.destroyAllWindows()
            break
        if key == ord('n') or key == 242:
            bot = False
            botCapture = 'off'
        if key == ord('y') or key == 237:
            bot = True
            botCapture = 'wait'
        if key == 32:
            botCapture = 'click now'
