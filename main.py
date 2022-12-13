from Picture import Picture
import cv2 as cv
from time import time
from windowcapture import WindowCapture

wincap = WindowCapture('MI 9')

threshold = .9

loop_time = time()

while True:
    screenshot = wincap.get_screenshot()

    Picture('duck', (0, 255, 255), screenshot)
    Picture('chip', (0, 0, 255), screenshot)
    Picture('ball', (0, 255, 0), screenshot)
    Picture('backpack', (255, 0, 0), screenshot)
    Picture('spruce', (0, 128, 0), screenshot)
    Picture('egg', (255, 0, 139), screenshot)

    cv.imshow('Map', screenshot)
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
