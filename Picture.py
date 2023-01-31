import os.path

import cv2 as cv
import numpy as np


class Picture:
    threshold = .885

    def __init__(self, name, color, screenshot, points):
        self.name = name
        self.color = color
        self.screenshot = screenshot
        for tape in range(0, 3):
            for carpet in range(0, 2):
                for ground in range(0, 2):
                    if os.path.exists(f'img/MatchThree/{name}_t{tape}c{carpet}g{ground}.jpg'):
                        img = cv.imread(f'img/MatchThree/{name}_t{tape}c{carpet}g{ground}.jpg', cv.IMREAD_UNCHANGED)
                        w = img.shape[1]
                        h = img.shape[0]
                        result = cv.matchTemplate(self.screenshot, img, cv.TM_CCOEFF_NORMED)
                        _, _, _, max_loc = cv.minMaxLoc(result)
                        yloc, xloc = np.where(result >= self.threshold)
                        rectangles = []
                        for (x, y) in zip(xloc, yloc):
                            rectangles.append([int(x), int(y), int(w), int(h)])
                            rectangles.append([int(x), int(y), int(w), int(h)])

                        rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)

                        for (x, y, w, h) in rectangles:
                            # cv.rectangle(self.screenshot, (x, y), (x + w, y + h), color, 1)
                            center_x = x + int(w / 2)
                            center_y = y + int(h / 2)
                            points.append([(center_x, center_y), (name, 't', tape, 'c', carpet, 'g', ground), color])
