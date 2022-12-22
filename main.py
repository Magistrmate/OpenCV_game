import operator

import numpy as np
from Picture import Picture
import cv2 as cv
from time import time, sleep
from windowcapture import WindowCapture
from threading import Thread
import pydirectinput
import subprocess
from random import randint

# subprocess.Popen([r"C:\Users\\retro\Downloads\scrcpy-win64-v1.24\scrcpy.exe", "-S", "-w"])
# sleep(2)
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
    points = list()
    namesColors = [('duck', (0, 191, 255)), ('chip', (0, 0, 255)), ('ball', (0, 255, 0)), ('backpack', (255, 0, 0)),
                   ('spruce', (0, 128, 0)), ('egg', (255, 0, 139))]
    for (name, color) in namesColors:
        Picture(name, color, screenshot, points)
    if len(points) > 0:
        # first_point = min(points, key=lambda i: i[4])
        (first_point_for_x, _), _, _ = min(points, key=lambda n: n[0][0])
        (last_point_for_x, _), _, _ = max(points, key=lambda n: n[0][0])
        (_, first_point_for_y), _, _ = min(points, key=lambda n: n[0][1])
        (_, last_point_for_y), _, _ = max(points, key=lambda n: n[0][1])
        # print(f'points\n{points}')
        # for (point, i) in zip(points, range(0, len(points))):
        for (index, point) in enumerate(points):
            x = point[0][0]
            y = point[0][1]
            name = point[1]
            color = point[2]
            for (x0, column) in zip(range(first_point_for_x - 5, last_point_for_x + 5, 51), range(1, 9)):
                if x0 <= x <= (x0 + 11):
                    for (y0, row) in zip(range(first_point_for_y - 5, last_point_for_y + 5, 51), range(1, 11)):
                        if y0 <= y <= (y0 + 11):
                            points[index].append((column, row))
                            cv.putText(screenshot, str(column) + " " + str(row) + " " + name, (x - 20, y - 20),
                                       cv.FONT_HERSHEY_SIMPLEX, .4, color)
                            # cv.drawMarker(screenshot, (point[0], point[1]), point[3], cv.MARKER_CROSS, 5, 5,
                            # cv.LINE_4)
        # print(f'points\n{points}')
        # for (pointOne, i) in zip(points, range(0, len(points))):
        #     columnOne = pointOne[4][0]
        #     rowOne = pointOne[4][1]
        #     nameOne = pointOne[2]
        #     # print(f'pointOne{pointOne}')
        #     for pointBetweenOne in points:
        #         columnBetweenOne = pointBetweenOne[4][0]
        #         rowBetweenOne = pointBetweenOne[4][1]
        #         nameBetweenOne = pointBetweenOne[2]
        #         for pointBetweenTwo in points:
        #             if pointBetweenOne == pointBetweenTwo:
        #                 continue
        #             columnBetweenTwo = pointBetweenTwo[4][0]
        #             rowBetweenTwo = pointBetweenTwo[4][1]
        #             nameBetweenTwo = pointBetweenTwo[2]
        #             if columnBetweenTwo == columnBetweenOne - 1 and \
        #                     rowBetweenTwo == rowBetweenOne and nameBetweenTwo == nameBetweenOne:
        #                 for pointTwo in points:
        #                     if pointOne == pointTwo:
        #                         continue
        #                     columnTwo = pointTwo[4][0]
        #                     rowTwo = pointTwo[4][1]
        #                     nameTwo = pointTwo[2]
        #                     # print(f'pointTwo{pointTwo}')
        #                     if columnTwo == columnOne + 2 and nameOne == nameTwo and rowTwo == rowOne:
        #                         for pointThree in points:
        #                             if pointOne == pointThree or pointTwo == pointThree:
        #                                 continue
        #                             columnThree = pointThree[4][0]
        #                             rowThree = pointThree[4][1]
        #                             nameThree = pointThree[2]
        #                             # print(f'pointThree{pointThree}')
        #                             if columnThree == columnOne + 3 and nameThree == nameOne and rowThree == rowOne:
        #                                 print(f'pointOne{pointOne}')
        #                                 print(f'pointTwo{pointTwo}')
        #                                 print(f'pointThree{pointThree}')
        #                                 print('move')

        # _, _, _, _, (minColumn, _) = min(points, key=lambda n: n[4])
        # print(f'minColumn {minColumn}')
        # _, _, _, _, (maxColumn, _) = max(points, key=lambda n: n[4])
        # print(f'maxColumn {maxColumn}')
        # _, _, _, _, (_, maxRow) = max(points, key=lambda n: n[4][1])
        # print(f'maxRow {maxRow}')
        # _, _, _, _, (_, minRow) = min(points, key=lambda n: n[4][1])
        # print(f'minRow {minRow}')
        # for column in range(maxColumn):
        # for row in range(maxRow):
        # if column == pointColumn + 1 and row == pointRow:
        # for (index, point) in enumerate(points):
        #     pointRight1 = 0
        #     print(f'point{point}')
        #     pointColumn = point[4][0]
        #     pointRow = point[4][1]
        #     pointName = point[2]
        #     for pointFind in points[index:]:
        #         pointColumnFind = pointFind[4][0]
        #         pointRowFind = pointFind[4][1]
        #         pointNameFind = pointFind[2]
        #         if pointRowFind == pointRow:
        #             if pointColumnFind == pointColumn + 1:
        #                 pointRight1 = pointFind
        #                 print(f'pointRight1{pointRight1}')
        #                 point.append(('right1', pointNameFind))
        #             if pointColumnFind == pointColumn + 2:
        #                 pointRight2 = pointFind
        #                 print(f'pointRight2{pointRight2}')
        #                 if point[5]
        #                 point.append(('right2', pointNameFind))
        #             if pointColumnFind == pointColumn + 3:
        #                 pointRight3 = pointFind
        #                 print(f'pointRight3{pointRight3}')
        #                 point.append(('right3', pointNameFind))
        #     if pointRight1 == 0:
        #         print(f'pointRight1 empty')
        #     print(points)

    cv.imshow('Map', screenshot)

    targets = points
    # if len(targets) > 0:
    #     target_click = wincap.get_screen_position(targets[0])
    #     if not is_bot_in_action:
    #         is_bot_in_action = True
    #         t = Thread(target=bot_action, args=(target_click,))
    #         t.start()

    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
