import cv2 as cv
import numpy as np


class Picture:
    threshold = .9

    def __init__(self, name, color, screenshot):
        self.name = name
        self.color = color
        self.screenshot = screenshot
        self.points = 0
        img = cv.imread(f'jpg/{name}_low.jpg', cv.IMREAD_UNCHANGED)
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
            cv.rectangle(self.screenshot, (x, y), (x + w, y + h), color, 1)
            cv.putText(self.screenshot, name, (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, color)

        points = []
        namePoints = []
        row = 0
        column = 0
        n = 1
        for (x, y, w, h) in rectangles:
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            print(n, center_x, center_y)
            points.append((center_x, center_y))
            for (a, c) in zip(range(60, 380, 50), range(1, 8)):
                if a <= center_x <= (a + 11):
                    column = c
                    print(f'{a}<x{center_x}<{a + 60}')
                    print(f'{n} {name} строка {row}')
                    for (b, r) in zip(range(310, 670, 50), range(1, 9)):
                        if b <= center_y <= (b + 11):
                            row = r
                            print(f'{b}<y{center_y}<{b + 60}')
                            print(f'{n} {name} столбец {column}')
                            namePoints.append((row, column, center_x, center_y, name))
                            print(f'{n} {name} строка {row} столбец {column}')
                            n = n + 1

        self.namePoints = namePoints
        self.points = points
        # print(f'{name}\n{points}')
