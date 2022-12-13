import cv2 as cv
import numpy as np
from time import time
from windowcapture import WindowCapture

wincap = WindowCapture('MI 9')

screenshot = cv.imread('jpg/Map.jpg', cv.IMREAD_UNCHANGED)
chip_img = cv.imread('jpg/chip_low.jpg', cv.IMREAD_UNCHANGED)
ball_img = cv.imread('jpg/ball_low.jpg', cv.IMREAD_UNCHANGED)
backpack_img = cv.imread('jpg/backpack_low.jpg', cv.IMREAD_UNCHANGED)
spruce_img = cv.imread('jpg/spruce_low.jpg', cv.IMREAD_UNCHANGED)
duck_img = cv.imread('jpg/duck_low.jpg', cv.IMREAD_UNCHANGED)
egg_img = cv.imread('jpg/egg_low.jpg', cv.IMREAD_UNCHANGED)

w_chip = chip_img.shape[1]
h_chip = chip_img.shape[0]
w_ball = ball_img.shape[1]
h_ball = ball_img.shape[0]
w_backpack = backpack_img.shape[1]
h_backpack = backpack_img.shape[0]
w_spruce = spruce_img.shape[1]
h_spruce = spruce_img.shape[0]
w_duck = duck_img.shape[1]
h_duck = duck_img.shape[0]
w_egg = egg_img.shape[1]
h_egg = egg_img.shape[0]

threshold = .9

loop_time = time()

while True:

    screenshot = wincap.get_screenshot()
    result_chip = cv.matchTemplate(screenshot, chip_img, cv.TM_CCOEFF_NORMED)
    result_ball = cv.matchTemplate(screenshot, ball_img, cv.TM_CCOEFF_NORMED)
    result_backpack = cv.matchTemplate(screenshot, backpack_img, cv.TM_CCOEFF_NORMED)
    result_spruce = cv.matchTemplate(screenshot, spruce_img, cv.TM_CCOEFF_NORMED)
    result_duck = cv.matchTemplate(screenshot, duck_img, cv.TM_CCOEFF_NORMED)
    result_egg = cv.matchTemplate(screenshot, egg_img, cv.TM_CCOEFF_NORMED)

    _, _, _, max_loc_chip = cv.minMaxLoc(result_chip)
    _, _, _, max_loc_ball = cv.minMaxLoc(result_ball)
    _, _, _, max_loc_backpack = cv.minMaxLoc(result_backpack)
    _, _, _, max_loc_spruce = cv.minMaxLoc(result_spruce)
    _, _, _, max_loc_duck = cv.minMaxLoc(result_duck)
    _, _, _, max_loc_egg = cv.minMaxLoc(result_egg)

    yloc_chip, xloc_chip = np.where(result_chip >= threshold)
    yloc_ball, xloc_ball = np.where(result_ball >= threshold)
    yloc_backpack, xloc_backpack = np.where(result_backpack >= threshold)
    yloc_spruce, xloc_spruce = np.where(result_spruce >= threshold)
    yloc_duck, xloc_duck = np.where(result_duck >= threshold)
    yloc_egg, xloc_egg = np.where(result_egg >= threshold)

    rectangles_chip = []

    for (x, y) in zip(xloc_chip, yloc_chip):
        rectangles_chip.append([int(x), int(y), int(w_chip), int(h_chip)])
        rectangles_chip.append([int(x), int(y), int(w_chip), int(h_chip)])

    rectangles_chip, weights = cv.groupRectangles(rectangles_chip, 1, 0.2)

    for (x, y, w_chip, h_chip) in rectangles_chip:
        cv.rectangle(screenshot, (x, y), (x + w_chip, y + h_chip), (0, 0, 255), 1)
        cv.putText(screenshot, 'Chip', (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255))

    rectangles_ball = []

    for (x, y) in zip(xloc_ball, yloc_ball):
        rectangles_ball.append([int(x), int(y), int(w_ball), int(h_ball)])
        # rectangles_ball.append([int(x), int(y), int(w_ball), int(h_ball)])

    rectangles_ball, weights = cv.groupRectangles(rectangles_ball, 1, 0.2)

    for (x, y, w_ball, h_ball) in rectangles_ball:
        cv.rectangle(screenshot, (x, y), (x + w_ball, y + h_ball), (0, 255, 0), 1)
        cv.putText(screenshot, 'Ball', (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0))

    rectangles_backpack = []

    for (x, y) in zip(xloc_backpack, yloc_backpack):
        rectangles_backpack.append([int(x), int(y), int(w_backpack), int(h_backpack)])
        # rectangles_backpack.append([int(x), int(y), int(w_backpack), int(h_backpack)])

    rectangles_backpack, weights = cv.groupRectangles(rectangles_backpack, 1, 0.2)

    for (x, y, w_backpack, h_backpack) in rectangles_backpack:
        cv.rectangle(screenshot, (x, y), (x + w_backpack, y + h_backpack), (255, 0, 0), 1)
        cv.putText(screenshot, 'Backpack', (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 0))

    rectangles_spruce = []

    for (x, y) in zip(xloc_spruce, yloc_spruce):
        rectangles_spruce.append([int(x), int(y), int(w_spruce), int(h_spruce)])
        # rectangles_spruce.append([int(x), int(y), int(w_spruce), int(h_spruce)])

    rectangles_spruce, weights = cv.groupRectangles(rectangles_spruce, 1, 0.2)

    for (x, y, w_spruce, h_spruce) in rectangles_spruce:
        cv.rectangle(screenshot, (x, y), (x + w_spruce, y + h_spruce), (0, 128, 0), 1)
        cv.putText(screenshot, 'Spruce', (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 128, 0))

    rectangles_duck = []

    for (x, y) in zip(xloc_duck, yloc_duck):
        rectangles_duck.append([int(x), int(y), int(w_duck), int(h_duck)])
        # rectangles_duck.append([int(x), int(y), int(w_duck), int(h_duck)])

    rectangles_duck, weights = cv.groupRectangles(rectangles_duck, 1, 0.2)

    for (x, y, w_duck, h_duck) in rectangles_duck:
        cv.rectangle(screenshot, (x, y), (x + w_duck, y + h_duck), (0, 255, 255), 1)
        cv.putText(screenshot, 'Duck', (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 255))

    rectangles_egg = []

    for (x, y) in zip(xloc_egg, yloc_egg):
        rectangles_egg.append([int(x), int(y), int(w_egg), int(h_egg)])
        # rectangles_egg.append([int(x), int(y), int(w_egg), int(h_egg)])

    rectangles_egg, weights = cv.groupRectangles(rectangles_egg, 1, 0.2)

    for (x, y, w_egg, h_egg) in rectangles_egg:
        cv.rectangle(screenshot, (x, y), (x + w_egg, y + h_egg), (255, 0, 139), 1)
        cv.putText(screenshot, 'Egg', (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 0, 139))

    cv.imshow('Map', screenshot)
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
