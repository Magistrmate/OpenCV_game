import operator

import numpy as np
from Picture import Picture
import cv2 as cv
from time import time, sleep
from windowcapture import WindowCapture
from threading import Thread
import pydirectinput

wincap = WindowCapture('MI 9')

threshold = .9

is_bot_in_action = False


def bot_action(target):
    pydirectinput.moveTo(target[0], target[1])
    pydirectinput.mouseDown()
    pydirectinput.moveTo(target[0] + 50, target[1])
    pydirectinput.mouseUp()
    sleep(5)
    global is_bot_in_action
    is_bot_in_action = False


loop_time = time()
while True:
    screenshot = wincap.get_screenshot()
    mas = []
    duck = Picture('duck', (0, 255, 255), screenshot)
    mas.append(duck.namePoints)
    chip = Picture('chip', (0, 0, 255), screenshot)
    mas.append(chip.namePoints)
    ball = Picture('ball', (0, 255, 0), screenshot)
    mas.append(ball.namePoints)
    backpack = Picture('backpack', (255, 0, 0), screenshot)
    mas.append(backpack.namePoints)
    spruce = Picture('spruce', (0, 128, 0), screenshot)
    mas.append(spruce.namePoints)
    egg = Picture('egg', (255, 0, 139), screenshot)
    mas.append(egg.namePoints)
    print(f'mas\n{mas}')
    mas2 = []
    for i in mas:
        for i2 in i:
            mas2.append(i2)
    mas2Sorted = sorted(mas)
    print(f'mas2 \n {mas2Sorted} \n')
    for x in range(0, len(mas2Sorted), 7):
        e_c = mas2Sorted[x: 7 + x]
        print(list(e_c))

    # for x in range(63, 375, 51):
    #     for y in range(189, 795, 50):
    #         # print(x, y)
    #         cv.drawMarker(screenshot, (x, y), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)

    cv.imshow('Map', screenshot)

    '''    targets = duck.points
    if len(targets) > 0:
        target_click = wincap.get_screen_position(targets[0])
        if not is_bot_in_action:
            is_bot_in_action = True
            t = Thread(target=bot_action, args=(target_click,))
            t.start()'''

    # print('FPS {}'.format(1 / (time() - loop_time)))
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
