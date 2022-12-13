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

    duck = Picture('duck', (0, 255, 255), screenshot)
    Picture('chip', (0, 0, 255), screenshot)
    Picture('ball', (0, 255, 0), screenshot)
    Picture('backpack', (255, 0, 0), screenshot)
    Picture('spruce', (0, 128, 0), screenshot)
    Picture('egg', (255, 0, 139), screenshot)

    cv.imshow('Map', screenshot)

    targets = duck.points
    '''if len(targets) > 0:
        target_click = wincap.get_screen_position(targets[0])
        if not is_bot_in_action:
            is_bot_in_action = True
            t = Thread(target=bot_action, args=(target_click,))
            t.start()'''

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
