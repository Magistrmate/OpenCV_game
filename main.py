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
        first_point_for_x, _, _, _ = min(points, key=lambda n: n[0])
        last_point_for_x, _, _, _ = max(points, key=lambda n: n[0])
        _, first_point_for_y, _, _ = min(points, key=lambda n: n[1])
        _, last_point_for_y, _, _ = max(points, key=lambda n: n[1])
        # print(f'points\n{points}')
        for (point, i) in zip(points, range(0, len(points))):
            x = point[0]
            y = point[1]
            name = point[2]
            color = point[3]
            for (x0, column) in zip(range(first_point_for_x - 5, last_point_for_x + 5, 51), range(1, 9)):
                if x0 <= x <= (x0 + 11):
                    for (y0, row) in zip(range(first_point_for_y - 5, last_point_for_y + 5, 51), range(1, 11)):
                        if y0 <= y <= (y0 + 11):
                            points[i].append((column, row))
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
        # [[142, 361, 'duck', (0, 191, 255), (3, 3)], [397, 362, 'duck', (0, 191, 255), (8, 3)], [295, 413, 'duck', (0, 191, 255), (6, 4)], [396, 463, 'duck', (0, 191, 255), (8, 5)], [92, 565, 'duck', (0, 191, 255), (2, 7)], [193, 565, 'duck', (0, 191, 255), (4, 7)], [244, 565, 'duck', (0, 191, 255), (5, 7)], [346, 565, 'duck', (0, 191, 255), (7, 7)], [142, 667, 'duck', (0, 191, 255), (3, 9)], [142, 717, 'duck', (0, 191, 255), (3, 10)], [38, 260, 'chip', (0, 0, 255), (1, 1)], [89, 311, 'chip', (0, 0, 255), (2, 2)], [191, 311, 'chip', (0, 0, 255), (4, 2)], [394, 311, 'chip', (0, 0, 255), (8, 2)], [191, 362, 'chip', (0, 0, 255), (4, 3)], [343, 413, 'chip', (0, 0, 255), (7, 4)], [394, 413, 'chip', (0, 0, 255), (8, 4)], [191, 464, 'chip', (0, 0, 255), (4, 5)], [394, 514, 'chip', (0, 0, 255), (8, 6)], [242, 616, 'chip', (0, 0, 255), (5, 8)], [394, 616, 'chip', (0, 0, 255), (8, 8)], [38, 667, 'chip', (0, 0, 255), (1, 9)], [89, 667, 'chip', (0, 0, 255), (2, 9)], [242, 667, 'chip', (0, 0, 255), (5, 9)], [293, 667, 'chip', (0, 0, 255), (6, 9)], [89, 260, 'ball', (0, 255, 0), (2, 1)], [292, 260, 'ball', (0, 255, 0), (6, 1)], [89, 362, 'ball', (0, 255, 0), (2, 3)], [343, 362, 'ball', (0, 255, 0), (7, 3)], [190, 412, 'ball', (0, 255, 0), (4, 4)], [292, 463, 'ball', (0, 255, 0), (6, 5)], [191, 514, 'ball', (0, 255, 0), (4, 6)], [241, 514, 'ball', (0, 255, 0), (5, 6)], [191, 616, 'ball', (0, 255, 0), (4, 8)], [241, 717, 'ball', (0, 255, 0), (5, 10)], [38, 362, 'backpack', (255, 0, 0), (1, 3)], [292, 362, 'backpack', (255, 0, 0), (6, 3)], [241, 412, 'backpack', (255, 0, 0), (5, 4)], [343, 514, 'backpack', (255, 0, 0), (7, 6)], [140, 514, 'backpack', (255, 0, 0), (3, 6)], [394, 565, 'backpack', (255, 0, 0), (8, 7)], [190, 667, 'backpack', (255, 0, 0), (4, 9)], [89, 718, 'backpack', (255, 0, 0), (2, 10)], [190, 718, 'backpack', (255, 0, 0), (4, 10)], [393, 264, 'spruce', (0, 128, 0), (8, 1)], [37, 315, 'spruce', (0, 128, 0), (1, 2)], [291, 315, 'spruce', (0, 128, 0), (6, 2)], [241, 366, 'spruce', (0, 128, 0), (5, 3)], [241, 467, 'spruce', (0, 128, 0), (5, 5)], [343, 467, 'spruce', (0, 128, 0), (7, 5)], [291, 519, 'spruce', (0, 128, 0), (6, 6)], [37, 620, 'spruce', (0, 128, 0), (1, 8)], [139, 620, 'spruce', (0, 128, 0), (3, 8)], [291, 722, 'spruce', (0, 128, 0), (6, 10)], [139, 262, 'egg', (255, 0, 139), (3, 1)], [190, 261, 'egg', (255, 0, 139), (4, 1)], [139, 312, 'egg', (255, 0, 139), (3, 2)], [241, 312, 'egg', (255, 0, 139), (5, 2)], [343, 312, 'egg', (255, 0, 139), (7, 2)], [89, 618, 'egg', (255, 0, 139), (2, 8)], [292, 617, 'egg', (255, 0, 139), (6, 8)], [343, 618, 'egg', (255, 0, 139), (7, 8)], [38, 719, 'egg', (255, 0, 139), (1, 10)]]
        for (index, point) in enumerate(points):
            print(f'point{point}')
            columnPoint = point[4][0]
            rowPoint = point[4][1]
            namePoint = point[2]
            for pointNext in points[index:]:
                columnPointNext = pointNext[4][0]
                rowPointNext = pointNext[4][1]
                namePointNext = pointNext[2]
                # for column in range(maxColumn):
                    # for row in range(maxRow):
                        # if column == columnPoint + 1 and row == rowPoint:
                if columnPointNext == columnPoint + 1 and rowPointNext == rowPoint:
                    pointMoveRight = pointNext
                    print(f'pointMoveRight{pointMoveRight}')
                    break
                else:
                    print('empty')

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
