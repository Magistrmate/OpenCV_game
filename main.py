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
    # pydirectinput.moveTo(target[0], target[1])
    pydirectinput.mouseDown()
    pydirectinput.moveTo(target[0] + 50, target[1])
    pydirectinput.mouseUp()
    sleep(5)
    global is_bot_in_action
    is_bot_in_action = False


def find_first_picture():
    print(ok)


while True:
    screenshot = wincap.get_screenshot()
    points = list()
    namesColors = [('duck', (0, 191, 255)), ('chip', (0, 0, 255)), ('ball', (0, 255, 0)), ('backpack', (255, 0, 0)),
                   ('spruce', (0, 128, 0)), ('egg', (255, 0, 139))]
    for (name, color) in namesColors:
        Picture(name, color, screenshot, points)
    if len(points) > 0:
        # first_point = min(points, key=lambda i: i[4])
        first_point_for_x = min(points, key=lambda n: n[0])
        last_point_for_x = max(points, key=lambda n: n[0])
        first_point_for_y = min(points, key=lambda n: n[1])
        last_point_for_y = max(points, key=lambda n: n[1])
        # last_point = max(points, key=lambda i: (i[1], i[1]))
        # last_point = max(points, key=lambda i: i[4])
        # print(f'last_point{last_point}')
        # print(f'first_point{first_point}')
        print(f'point\n{points}')
        for (point, i) in zip(points, range(0, len(points))):
            for (a, c) in zip(range(first_point_for_x[0] - 5, last_point_for_x[0] + 5, 51), range(1, 9)):
                if a <= point[0] <= (a + 11):
                    # print(f'{a}<x{point[0]}<{a + 11}')
                    # print(f'{n} {point[2]} столбец {c}')
                    for (b, r) in zip(range(first_point_for_y[1] - 5, last_point_for_y[1] + 5, 51), range(1, 11)):
                        if b <= point[1] <= (b + 11):
                            # print(f'{b}<y{point[1]}<{b + 11}')
                            # print(f'{n} {point[2]} строка {r}')
                            points[i].append([c, r])
                            cv.putText(screenshot, str(c) + " " + str(r) + " " + point[2], (point[0] - 20,
                                                                                            point[1] - 20),
                                       cv.FONT_HERSHEY_SIMPLEX, .4, point[3])
        print(f'point\n{points}')
    cv.imshow('Map', screenshot)

    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
