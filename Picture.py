import os.path

import cv2 as cv
import numpy as np


class Picture:
    threshold = .76

    def __init__(self, name, color, space_hold, tape_hold, carpet_hold, ground_hold, screenshot, points):
        self.name = name
        self.color = color
        self.screenshot = screenshot
        self.space_hold = space_hold
        self.tape_hold = tape_hold
        self.carpet_hold = carpet_hold
        self.ground_hold = ground_hold
        self.threshold = space_hold
        for tape in range(0, 3):
            for carpet in range(0, 10):
                for ground in range(0, 2):
                    if os.path.exists(f'img/MatchThree/{name}_t{tape}c{carpet}g{ground}.jpg'):
                        img = cv.imread(f'img/MatchThree/{name}_t{tape}c{carpet}g{ground}.jpg', cv.IMREAD_UNCHANGED)
                        w = img.shape[1]
                        h = img.shape[0]
                        result = cv.matchTemplate(self.screenshot, img, cv.TM_CCOEFF_NORMED)
                        _, _, _, max_loc = cv.minMaxLoc(result)
                        if tape != 0:
                            self.threshold = tape_hold
                        if carpet != 0:
                            self.threshold = carpet_hold
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
                            # print(f'center_x {center_x}center_y {center_y}')
                            # for find_x in range(center_x - 2, center_x + 2):
                            #     for find_y in range(center_y - 2, center_y + 2):
                            #         print(f'find_x{find_x}find_y{find_y}')
                            #         if ([(find_x, find_y), (name, 't', tape, 'c', 0, 'g', ground), color]) in points:
                            #             print([(center_x, center_y), (name, 't', tape, 'c', carpet, 'g', ground), color])
                            #             print([(center_x, center_y), (name, 't', tape, 'c', 0, 'g', ground), color])
                            #             break
                            #         else:
                            points.append([(center_x, center_y), (name, 't', tape, 'c', carpet, 'g', ground),
                                           color])
