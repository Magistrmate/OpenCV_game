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


def bot_action(target, a, b):
    pydirectinput.moveTo(target[0], target[1])
    pydirectinput.mouseDown()
    pydirectinput.moveTo(target[0] + 50 * a, target[1] + 50 * b)
    pydirectinput.mouseUp()
    sleep(1)
    global is_bot_in_action
    is_bot_in_action = False


def before_bot_action(point_target, direction, a, b):
    global is_bot_in_action
    # pointsChance.append(point_target)
    cv.putText(screenshot, direction, (point_target[0][0], point_target[0][1]),
               cv.FONT_HERSHEY_SIMPLEX, .4, point_target[2])
    target_click = wincap.get_screen_position(point_target[0])
    if not is_bot_in_action:
        is_bot_in_action = True
        t = Thread(target=bot_action, args=(target_click, a, b))
        t.start()


while True:
    screenshot = wincap.get_screenshot()
    points = []
    namesColors = [('duck', (0, 191, 255)), ('chip', (0, 0, 255)), ('ball', (0, 255, 0)), ('backpack', (255, 0, 0)),
                   ('spruce', (0, 128, 0)), ('egg', (255, 0, 139))]
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
                # #    [4]         0      1          2        3    4    5    6    7    8    9   10       11     12   13
                # point.append(['right', 'X', 'rightUpDown', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'UpDown', 'X', 'X',
                #               # 14  15   16   17    18     19     20          21   22   23   24   25   26   27   28
                #               'X', 'X', 'X', 'X', 'left', 'X', 'leftUpDown', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
                #    [4]         0     1    2    3    4    5    6    7    8    9    10   11   12
                point.append(['left', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              # 13 14(1)|15(2)|16(3)|17(4)|18(5)|19(6)|20(7)|21(8)|22(9)|23(10)|24(11)|25(12)
                              'right', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              # 26   27     28      29
                              'Up0', 'X', 'Down0', 'X',
                              # 30 31(1)|32(2)|33(3)|34(4)|35(5)|36(6)|37(7)|38(8)|39(9)|40(10)|41(11)|42(12)|43(13)
                              #                                                                        44(14)|45(15)
                              'Up', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              # 46 47(1)|48(2)|49(3)|50(4)|51(5)|52(6)|53(7)|54(8)|55(9)|56(10)|57(11)|58(12)|59(13)
                              #                                                                        60(14)|61(15)
                              'Down', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
                pointColumn = point[3][0]
                pointRow = point[3][1]
                pointName = point[1]
                for pointFind in points:
                    pointColumnFind = pointFind[3][0]
                    pointRowFind = pointFind[3][1]
                    pointNameFind = pointFind[1]
                    x = pointColumnFind - pointColumn
                    y = pointRowFind - pointRow
                    if -4 <= x <= 4 and -1 <= y <= 1:
                        for (m, d) in zip((1, -1), (0, 7)):
                            #  4 + 1 =  5
                            # -4 + 1 = -3

                            #  4 + 2 =  6
                            # -4 + 2 = -2

                            #  4 + 3 =  7
                            # -4 + 3 = -1

                            #  4 + 4 =  8
                            # -4 + 4 =  0

                            #  4 - 4 =  0
                            # -4 - 4 = -8

                            #  4 - 3 =  1
                            # -4 - 3 = -7

                            #  4 - 2 =  2
                            # -4 - 2 = -6

                            #  4 - 1 =  3
                            # -4 - 1 = -5
                            # if (4 * m + x) <= 0:
                            for (c, n) in zip(range(-4 * m, m, m), range(5 + d, 12 + d * 2, (3 - m))):
                                if c == x:
                                    # for r in range(-1, 2, 1):
                                    # m    x    y   n
                                    # 1 + -4 + -1 + 5 = 1

                                    #  m    c    r        n
                                    #  1 + -4 + -1 = -4 + 5  = 1
                                    #  1 + -4 +  0 = -3 + 5  = 2
                                    #  1 + -4 +  1 = -2 + 5  = 3

                                    #  1 + -3 + -1 = -3 + 7  = 4
                                    #  1 + -3 +  0 = -2 + 7  = 5
                                    #  1 + -3 +  1 = -1 + 7  = 6

                                    #  1 + -2 + -1 = -2 + 9  = 7
                                    #  1 + -2 +  0 = -1 + 9  = 8
                                    #  1 + -2 +  1 =  0 + 9  = 9

                                    #  1 + -1 + -1 = -1 + 11 = 10
                                    #  1 + -1 +  0 =  0 + 11 = 11
                                    #  1 + -1 +  1 =  1 + 11 = 12

                                    # -1 +  4 + -1 =  2 + 12 = 14
                                    # -1 +  4 +  0 =  3 + 12 = 15
                                    # -1 +  4 +  1 =  4 + 12 = 16

                                    # -1 +  3 + -1 =  1 + 16 = 17
                                    # -1 +  3 +  0 =  2 + 16 = 18
                                    # -1 +  3 +  1 =  3 + 16 = 19

                                    # -1 +  2 + -1 =  0 + 20 = 20
                                    # -1 +  2 +  0 =  1 + 20 = 21
                                    # -1 +  2 +  1 =  2 + 20 = 22

                                    # -1 +  1 + -1 = -1 + 24 = 23
                                    # -1 +  1 +  0 =  0 + 24 = 24
                                    # -1 +  1 +  1 =  1 + 24 = 25
                                    point[4][m + x + y + n] = pointNameFind
                                    break
                    #          4             6
                    # if pointRowFind == pointRow + r and pointColumnFind == pointColumn + c:
                    #     point[4][-4 + 5] = pointNameFind
                    #     break
                    # for (r, o, c, k) in zip((1, -1), (1, 19), (5, 23), (9, 27)):
                    #     if pointRowFind == pointRow and pointColumnFind == pointColumn + 3 * r:
                    #         point[4][o] = pointNameFind
                    #         break
                    #     elif -2 <= abs(pointRowFind - pointRow) <= 2 and (pointColumnFind == pointColumn + 1 * r or
                    #                                                       pointColumnFind == pointColumn + 2 * r):
                    #         if pointColumnFind == pointColumn + 1 * r:
                    #             for i in range(2, -3, -1):
                    #                 if pointRowFind == pointRow - i:
                    #                     point[4][i + c] = pointNameFind
                    #                     break
                    #             break
                    #         elif pointColumnFind == pointColumn + 2 * r:
                    #             for i in range(1, -2, -1):
                    #                 if pointRowFind == pointRow - i:
                    #                     point[4][i + k] = pointNameFind
                    #                     break
                    #             break
                    # if 0 < abs(pointRowFind - pointRow) <= 3 and pointColumnFind == pointColumn:
                    #     if -3 <= pointRowFind - pointRow < 0:
                    #         for i in range(1, 4):
                    #             if pointRowFind == pointRow - i:
                    #                 point[4][14 + i] = pointNameFind
                    #                 break
                    #     else:
                    #         for i in range(1, 4):
                    #             if pointRowFind == pointRow + i:
                    #                 point[4][15 - i] = pointNameFind
                    #                 break
            except IndexError or TypeError:
                cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                           screenshot)
                print('error')
                break
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    pointCheck = points[random.randint(0, len(points))]
    print(pointCheck)
    cv.putText(screenshot, pointCheck[1], (pointCheck[0][0], pointCheck[0][1]), cv.FONT_HERSHEY_SIMPLEX,
               .8, pointCheck[2])
    # for (m, d) in zip(range(-200, 200, 50), (1, 12)):
    #     for (r, k) in zip(range(-50, 51, 50), range():
    for (m, d) in zip((1, -1), (0, 7)):
        for (c, n) in zip(range(-4 * m, m, m), range(5 + d, 12 + d * 2, (3 - m))):
            for r in range(-1, 2, 1):
                cv.putText(screenshot, pointCheck[4][m + c + r + n], (pointCheck[0][0] + c * 50,
                                                                      pointCheck[0][1] + r * 50),
                           cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    #      x
    #  -4 * 50 = -200
    #  -3 * 50 = -150
    #  -2 * 50 = -100
    #  -1 * 50 = -50
    #   1 * 50 =  50
    # for (c, k) in zip((1, -1), (0, 18)):
    #     for (i, n) in zip(range(7, 2, -1), range(-100, 101, 50)):
    #         cv.putText(screenshot, pointCheck[4][i + k], (pointCheck[0][0] + 50 * c, pointCheck[0][1] + n),
    #                    cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    #     for (i, n) in zip(range(10, 7, -1), range(-50, 51, 50)):
    #         cv.putText(screenshot, pointCheck[4][i + k], (pointCheck[0][0] + 100 * c, pointCheck[0][1] + n),
    #                    cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    # for (i, n) in zip(range(17, 14, -1), range(-150, -49, 50)):
    #     cv.putText(screenshot, pointCheck[4][i], (pointCheck[0][0], pointCheck[0][1] + n),
    #                cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    # for (i, n) in zip(range(14, 11, -1), range(50, 151, 50)):
    #     cv.putText(screenshot, pointCheck[4][i], (pointCheck[0][0], pointCheck[0][1] + n),
    #                cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    sleep(10)
    '''for point in points:
        try:
            pointName = point[1]
            right1 = point[4][5]
            right2 = point[4][9]
            right3 = point[4][1]
            rightUp1 = point[4][7]
            rightUp2 = point[4][6]
            rightUp3 = point[4][10]
            rightDown1 = point[4][4]
            rightDown2 = point[4][3]
            rightDown3 = point[4][8]
            up1 = point[4][17]
            up2 = point[4][16]
            up3 = point[4][15]
            down1 = point[4][14]
            down2 = point[4][13]
            down3 = point[4][12]
            left1 = point[4][23]
            left2 = point[4][27]
            left3 = point[4][19]
            leftUp1 = point[4][25]
            leftUp2 = point[4][24]
            leftUp3 = point[4][28]
            leftDown1 = point[4][22]
            leftDown2 = point[4][21]
            leftDown3 = point[4][26]
            #                 0        1        2       3          4        5            6      7  8    9
            pointAround = [(right1, right2, right3, rightUp1, rightUp2, rightDown1, rightDown2, 1, 0, 'right'),
                           # 0       1      2        3       4        5           6
                           (left1, left2, left3, leftUp1, leftUp2, leftDown1, leftDown2, -1, 0, 'left'),
                           # 0    1    2     3         4           5       6
                           (up3, up1, up2, rightUp3, rightUp2, leftUp2, leftUp3, 0, -1, 'up'),
                           # 0       1      2         3          4           5          6
                           (down1, down2, down3, rightDown3, rightDown1, leftDown1, leftDown3, 0, 1, 'down')]
            for pointCheck in pointAround:
                if pointCheck[0] != 'X':
                    # if pointName ==
                    if pointName == pointCheck[1] == pointCheck[2]:
                        before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
                    if pointName == pointCheck[3] == pointCheck[4]:
                        before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
                    if pointName == pointCheck[5] == pointCheck[6]:
                        before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
                    if pointName == pointCheck[4] == pointCheck[5]:
                        before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
        except IndexError or TypeError:
            cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                       screenshot)
            print('error')
            break'''
    cv.imshow('Map', screenshot)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time), screenshot)
