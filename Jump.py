import cv2 as cv
import numpy as np
from time import time, sleep
import pydirectinput
from windowcapture import WindowCapture

wincap = WindowCapture('MI 9')
pictures = ['barrier', 'cactus_big', 'cactus_small', 'cat', 'pit', 'rock', 'scooter', 'stick']
for picture in pictures:
    screenshot = cv.imread(f'jpg/{picture}.jpg', cv.IMREAD_UNCHANGED)
    cactus = cv.imread('jpg/cactus.jpg', cv.IMREAD_UNCHANGED)
    reload = cv.imread('jpg/reload.jpg', cv.IMREAD_UNCHANGED)

    w = cactus.shape[1]
    h = cactus.shape[0]

    threshold = .9

    loop_time = time()
    x_old = 0
    finish = 0
    fly = False
    jumpStart = 0
    jump = False
    pressJump = False
    while True:

        screenshot = wincap.get_screenshot()
        result_cactus = cv.matchTemplate(screenshot, cactus, cv.TM_CCOEFF_NORMED)
        result_reload = cv.matchTemplate(screenshot, reload, cv.TM_CCOEFF_NORMED)
        _, _, _, max_loc_chip = cv.minMaxLoc(result_cactus)

        yloc, xloc = np.where(result_cactus >= threshold)

        rectangles = []
        # print(time() - jumpStart)
        # if not fly and time() - jumpStart > 0.2:
        #     pydirectinput.click()
        #     jump = True
        #     jumpStart = time()
        #     print('Jump')
        # elif jump and 0 < time() < 0.2:
        #     fly = True
        # else:
        #     fly = False

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])
            print(f'x {x}')
            if 130 < x < 170:
                print(time() - jumpStart)
                if (not fly and time() - jumpStart > 0.2) or pressJump:
                    pydirectinput.click()
                    jump = True
                    jumpStart = time()
                    print('Jump')
                    pressJump = False
                elif jump and 0.01 < time() - jumpStart < 0.2:
                    fly = True
                    print('flying')
                    pressJump = True
                else:
                    fly = False
                    print('not flying')
                    jumpStart = 0

        if pressJump and 0.01 < time() - jumpStart < 0.2:
            pydirectinput.click()
            print(f'pressJump {time() - jumpStart}')

        rectangles_chip, weights = cv.groupRectangles(rectangles, 1, 0.2)

        for (x, y, w, h) in rectangles:
            cv.rectangle(screenshot, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv.putText(screenshot, 'Chip', (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255))
            # print(f'x {x}')

        # cv.drawMarker(screenshot, (110, 695), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)
        cv.rectangle(screenshot, (110, 500), (150, 700), (0, 255, 0), 1)
        cv.imshow('MapDino', screenshot)
        # print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()
        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
            break
