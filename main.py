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


def bot_action(target, one, two):
    pydirectinput.moveTo(target[0], target[1])
    pydirectinput.mouseDown()
    pydirectinput.moveTo(target[0] + 50 * one, target[1] + 50 * two)
    pydirectinput.mouseUp()
    sleep(1)
    global is_bot_in_action
    is_bot_in_action = False


def before_bot_action(point_target, text, one, two):
    global is_bot_in_action
    cv.putText(screenshot, text, (point_target[0][0], point_target[0][1]),
               cv.FONT_HERSHEY_SIMPLEX, .4, point_target[2])
    sleep(1)
    target_click = wincap.get_screen_position(point_target[0])
    if not is_bot_in_action:
        is_bot_in_action = True
        t = Thread(target=bot_action, args=(target_click, one, two))
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
                            #            cv.FONT_HERSHEY_SIMPLEX, .4, color)
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
                              # -12 -12 -12 -11  -11  -11  -10  -10  -10   -9   -9   -9   -8   -8   -8   -7   -7   -7
                              #  49  50  51  52   53   54   55   56   57   58   59   60   61   62   63   64   65   66
                              #   1   2   3   4    5    6    7    8    9   10   11   12   13   14   15   16   17   18
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              #  -1   0   1  -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #  -6  -6  -6  -5   -5   -5   -4   -4   -4   -3   -3   -3   -2   -2   -2
                              #  67  68  69  70   71   72   73   74   75   76   77   78   79   80   81     82
                              #  19  20  21  22   23   24   25   26   27   28   29   30   31   32   33      1
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'down',
                              #  -1  0   1   -1    0    1   -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #  12 12  12   11   11   11   10   10   10    9    9    9    8    8    8    7    7    7
                              #  83 84  85   86   87   88   89   90   91   92   93   94   95   96   97   98   99  100
                              #   1  2   3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18
                              'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                              #  -1   0   1  -1    0    1   -1    0    1   -1    0    1   -1    0    1
                              #   6   6   6   5    5    5    4    4    4    3    3    3    2    2    2
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
                        if x == 0 and (y == 1 or y == -1):
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
                            for (m, d) in zip((1, -1), (0, 12)):
                                for (r, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
                                    if r == y:
                                        # for r in range(-1, 2, 1):

                                        #  m  r(x) c(y)        n
                                        #  1 + -1 + -12 = -12 + 61 = 49
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
    # pointCheck = points[75]
    # print(pointCheck)
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
    # for (m, d) in zip((1, -1), (0, 12)):
    #     for (c, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
    #         for r in range(-1, 2, 1):
    #             cv.putText(screenshot, pointCheck[4][m + c + r + n], (pointCheck[0][0] + r * 50,
    #                                                                   pointCheck[0][1] + c * 50),
    #                        cv.FONT_HERSHEY_SIMPLEX, .4, pointCheck[2])
    # sleep(10)
    for (index, point) in enumerate(points):
        try:
            pointName = point[1]
            # [5]          0   1   2   3   4   5   6   7
            point.append(['l', 0, 'r', 0, 'u', 0, 'd', 0])
            for (stage, floor) in ((45, 19), (47, 21)):
                if point[4][stage] != 'X':
                    left = 0
                    right = 0
                    up_down = 0
                    for (a, b) in zip(range(floor, floor - 19, -3), range(1, 8)):
                        if point[4][a] or point[4][a + 22] or point[4][a + 61] == pointName:
                            if point[4][a] == pointName and left == b - 1:
                                left = b
                            if point[4][a + 22] == pointName and right == b - 1:
                                right = b
                            if point[4][a + 61] == pointName and up_down == b - 1:
                                up_down = b
                        else:
                            break
                    if left + right >= up_down:
                        point[5][stage - 40] = left + right + 1
                    else:
                        point[5][stage - 40] = up_down + 1
                    if point[5][stage - 40] >= 3:
                        cv.putText(screenshot, point[5][stage - 41] + str(point[5][stage - 40]), (point[0][0],
                                                                                                  point[0][1] -
                                                                                                  10),
                                   cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
                    # before_bot_action(point, str(point[5][5]), 0, -1)
            for (side, see) in ((17, 79), (39, 81)):
                if point[4][side + 3] != 'X':
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
                    if point[5][see - 78] >= 3:
                        cv.putText(screenshot, point[5][see - 79] + str(point[5][see - 78]), (point[0][0], point[0][1] +
                                                                                              side // 2),
                                   cv.FONT_HERSHEY_SIMPLEX, .4, (0, 0, 0))
        except IndexError or TypeError:
            cv.imwrite('C:/Users/retro/PycharmProjects/pythonProject/Screenshots/{}.jpg'.format(loop_time),
                       screenshot)
            print('error')
            break
    # print(points)
    # points_sort = sorted(points, key=lambda k: (k[5][1], k[5][3], k[5][5], k[5][7]), reverse=True)
    # for point in points_sort:
    #     print(point)
    try:
        # chance_points = [] for position in range(1, 8, 2): xy, name, _, rc, _, [direction, number, _, _, _, _, _,
        # _] = max(points, key=lambda l: (l[5][position], l[3][1])) chance_points.append([xy, name, rc, direction,
        # number]) print(chance_points)
        xy, name, _, rc, _, [_, number, _, _, _, _, _, _] = max(points, key=lambda l: (l[5][1], l[3][1]))
        max_l_point = xy, name, rc, direction, number
        xy, name, _, rc, _, [_, _, _, number, _, _, _, _] = max(points, key=lambda l: (l[5][3], l[3][1]))
        max_r_point = xy, name, rc, direction, number
        xy_u, _, _, rc_u, _, [_, _, _, _, _, max_u, _, _] = max(points, key=lambda l: (l[5][5], l[3][1]))
        max_u_point = xy_u, rc_u, max_u
        xy_d, _, _, rc_d, _, [_, _, _, _, _, _, _, max_d] = max(points, key=lambda l: (l[5][7], l[3][1]))
        max_d_point = xy_d, rc_d, max_d
        print(f' max_l_point {max_l_point} \n max_r_point {max_r_point} \n max_u_point {max_u_point} \n max_d_point '
              f'{max_d_point}')
        max_combo = max(max_l_point, max_r_point, max_u_point, max_d_point, key=lambda l: (l[2], l[1][1]))
        for chance_point in chance_points:
            print(f'{chance_point}')
        print(chance_points)
        max_combo = max(chance_points, key=lambda l: (l[4], l[1][2]))
        print(f'max_combo {max_combo}')
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
