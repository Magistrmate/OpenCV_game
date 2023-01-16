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
    # pydirectinput.moveTo(target[0], target[1])
    # pydirectinput.mouseDown()
    # pydirectinput.moveTo(target[0] + 50 * a, target[1] + 50 * b)
    # pydirectinput.mouseUp()
    # sleep(1)
    global is_bot_in_action
    is_bot_in_action = False


def before_bot_action(point_target, text, a, b):
    global is_bot_in_action
    cv.putText(screenshot, text, (point_target[0][0], point_target[0][1]),
               cv.FONT_HERSHEY_SIMPLEX, .4, point_target[2])
    sleep(1)
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
                # [4]           0
                point.append(['left',
                              # -7 -7   -7   -6   -6   -6   -5   -5   -5   -4   -4   -4   -3   -3   -3   -2   -2   -2
                              # -1  0    1   -1    0    1   -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #  1  2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              # -1 -1   -1
                              # -1  0    1
                              # 19 20   21     22
                              'X', 'X', 'X', 'right',
                              #  7  7    7    6    6    6    5    5    5    4    4    4    3    3    3    2    2    2
                              # -1  0    1   -1    0    1   -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              # 23 24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40
                              #  1  2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              #  1  1    1           0            -1
                              # -1  0    1          -1             0
                              # 41 42   43    44    45     46     47    48
                              # 19 20   21     1     2      1      2     1
                              'X', 'X', 'X', 'up0', 'X', 'down0', 'X', 'up',
                              #  -1   0   1  -1    0    1   -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #  12  12  12  11   11   11   10   10   10    9    9    9    8    8    8    7    7    7
                              #  49  50  51  52   53   54   55   56   57   58   59   60   61   62   63   64   65   66
                              #   1   2   3   4    5    6    7    8    9   10   11   12   13   14   15   16   17   18
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              #  -1   0   1  -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #   6   6   6   5    5    5    4    4    4    3    3    3    2    2    2
                              #  67  68  69  70   71   72   73   74   75   76   77   78   79   80   81     82
                              #  19  20  21  22   23   24   25   26   27   28   29   30   31   32   33      1
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'down',
                              #  -1  0   1   -1    0    1   -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #  -2 -2  -2   -3   -3   -3   -4   -4   -4   -5   -5   -5   -6   -6   -6   -7   -7   -7
                              #  83 84  85   86   87   88   89   90   91   92   93   94   95   96   97   98   99  100
                              #   1  2   3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              #  -1   0   1  -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #  -8  -8  -8  -9   -9   -9  -10  -10  -10  -11  -11  -11  -12  -12  -12
                              # 101 102 103 104  105  106  107  108  109  110  111  112  113   114 115
                              #  19  20  21  22   23   24   25   26   27   28   29   30   31   32   33
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
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
                        if x == 0 and y != 0:
                            point[4][46 + y] = pointNameFind
                        if (-7 <= x <= -1 or 1 <= x <= 7) and -1 <= y <= 1:
                            for (m, d) in zip((1, -1), (0, 10)):
                                for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
                                    if c == x:
                                        # for r in range(-1, 2, 1):

                                        #  m   c(x) r(y)      n
                                        #  1 + -7 + -1 = -7 + 8  = 1
                                        #  1 + -7 +  0 = -6 + 8  = 2
                                        #  1 + -7 +  1 = -

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
                                        #                        = 13

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
                        if -1 <= x <= 1 and (-12 <= y <= -2 or 2 <= y <= 12):
                            for (m, d) in zip((-1, 1), (0, 56)):
                                for (r, n) in zip(range(-12 * m, -1 * m, m), range(39 + d, 93 + d * 3, (3 - m))):
                                    if r == y:
                                        # for r in range(-1, 2, 1):

                                        #  m  r(x) c(y)        n
                                        # -1 + -1 + 12 = 10 + 39 = 49
                                        #  1 + -12 +  0 = -11 + 61 = 50
                                        #  1 + -12 +  1 = -10 + 61 = 51

                                        #  1 + -11 + -1 = -11 + 63  = 52
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
                                        #                        = 13

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
            except IndexError or TypeError:
                cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                           screenshot)
                print('error')
                break
    # print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    # pointCheck = points[random.randint(0, len(points))]
    # print(pointCheck)
    # # for (a, b) in zip(range(-1, 2, 1), (1, 45, 47)):
    # #     cv.putText(screenshot, pointCheck[b], (pointCheck[0][0], pointCheck[0][1] + a * 50), cv.FONT_HERSHEY_DUPLEX,
    # #                .4, pointCheck[2])
    # cv.putText(screenshot, pointCheck[1], (pointCheck[0][0], pointCheck[0][1]), cv.FONT_HERSHEY_DUPLEX,
    #            .6, pointCheck[2])
    # cv.putText(screenshot, pointCheck[4][45], (pointCheck[0][0], pointCheck[0][1] - 50), cv.FONT_HERSHEY_SIMPLEX,
    #            .4, pointCheck[2])
    # cv.putText(screenshot, pointCheck[4][47], (pointCheck[0][0], pointCheck[0][1] + 50), cv.FONT_HERSHEY_SIMPLEX,
    #            .4, pointCheck[2])
    # for (m, d) in zip((1, -1), (0, 10)):
    #     for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
    #         for r in range(-1, 2, 1):
    #             cv.putText(screenshot, pointCheck[4][m + c + r + n], (pointCheck[0][0] + c * 50,
    #                                                                   pointCheck[0][1] + r * 50),
    #                        cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    # for (m, d) in zip((-1, 1), (0, 56)):
    #     for (c, n) in zip(range(-12 * m, -1 * m, m), range(39 + d, 93 + d * 2, (3 - m))):
    #         for r in range(-1, 2, 1):
    #             cv.putText(screenshot, pointCheck[4][m + c + r + n], (pointCheck[0][0] + r * 50,
    #                                                                   pointCheck[0][1] + c * 50),
    #                        cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    # sleep(10)
    for point in points:
        try:
            pointName = point[1]
            # [5]           0     1     2     3    4   5    6     7
            point.append(['left', 0, 'right', 0, 'up', 0, 'down', 0])
            # print(point)
            i = 0
            if point[4][45] != 'X':
                # if point[4][19] == point[4][16] == pointName:
                #     i = 3
                #     point[5][5] = i
                #     print(point)
                #     if point[4][13] == pointName:
                #         i = 4
                #         if point[4][10] == pointName:
                #             i = 5
                for (o, p) in zip(range(19, 1, -3), range(3, 7)):
                    if point[4][o] == point[4][o - 3] == pointName:
                        point[5][5] = p
                        print(point)
                        cv.putText(screenshot, str(point[5][5]), (point[0][0], point[0][1]),
                                   cv.FONT_HERSHEY_SIMPLEX, .4, point[2])
                        break
            # point[5][5] = i
            # before_bot_action(point, str(point[5][5]), 0, -1)
            # right1 = point[4][5]
            # right2 = point[4][9]
            # right3 = point[4][1]
            # rightUp1 = point[4][7]
            # rightUp2 = point[4][6]
            # rightUp3 = point[4][10]
            # rightDown1 = point[4][4]
            # rightDown2 = point[4][3]
            # rightDown3 = point[4][8]
            # up1 = point[4][17]
            # up2 = point[4][16]
            # up3 = point[4][15]
            # down1 = point[4][14]
            # down2 = point[4][13]
            # down3 = point[4][12]
            # left1 = point[4][23]
            # left2 = point[4][27]
            # left3 = point[4][19]
            # leftUp1 = point[4][25]
            # leftUp2 = point[4][24]
            # leftUp3 = point[4][28]
            # leftDown1 = point[4][22]
            # leftDown2 = point[4][21]
            # leftDown3 = point[4][26]
            # #                 0        1        2       3          4        5            6      7  8    9
            # pointAround = [(right1, right2, right3, rightUp1, rightUp2, rightDown1, rightDown2, 1, 0, 'right'),
            #                # 0       1      2        3       4        5           6
            #                (left1, left2, left3, leftUp1, leftUp2, leftDown1, leftDown2, -1, 0, 'left'),
            #                # 0    1    2     3         4           5       6
            #                (up3, up1, up2, rightUp3, rightUp2, leftUp2, leftUp3, 0, -1, 'up'),
            #                # 0       1      2         3          4           5          6
            #                (down1, down2, down3, rightDown3, rightDown1, leftDown1, leftDown3, 0, 1, 'down')]
            # for pointCheck in pointAround:
            #     if pointCheck[0] != 'X':
            #         # if pointName ==
            #         if pointName == pointCheck[1] == pointCheck[2]:
            #             before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
            #         if pointName == pointCheck[3] == pointCheck[4]:
            #             before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
            #         if pointName == pointCheck[5] == pointCheck[6]:
            #             before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
            #         if pointName == pointCheck[4] == pointCheck[5]:
            #             before_bot_action(point, pointCheck[9], pointCheck[7], pointCheck[8])
        except IndexError or TypeError:
            cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                       screenshot)
            print('error')
            break
    cv.imshow('Map', screenshot)
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    # cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time), screenshot)
