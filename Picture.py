import cv2 as cv
import numpy as np


class Picture:
    threshold = .9

    def __init__(self, name, color, screenshot, points):
        self.name = name
        self.color = color
        self.screenshot = screenshot
        self.points = 0
        self.rectangles = []
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
            # cv.putText(self.screenshot, name, (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, color)

        # points = []
        n = 1
        if len(rectangles) > 0:
            start_rectangle = min(rectangles, key=lambda i: i[0])
            print(start_rectangle)
            start_center_x = start_rectangle[0] + int(start_rectangle[2]/2)
            print(start_center_x)
            start_center_y = start_rectangle[1] + int(start_rectangle[3]/2)
            print(start_center_y)
            for (x, y, w, h) in rectangles:
                center_x = x + int(w / 2)
                center_y = y + int(h / 2)
                print(n, center_x, center_y)
                points.append((center_x, center_y))
                # print(name, center_x, center_y)
                '''                for (a, c) in zip(range(center_x - 5, center_x + 5, 50), range(1, 9)):
                    if a <= center_x <= (a + 11):
                        # print("ok")
                        column = c
                        print(f'{a}<x{center_x}<{a + 60}')
                        print(f'{n} {name} столбец {column}')
                        for (b, r) in zip(range(center_y - 5, center_y + 5, 50), range(1, 13)):
                            if b <= center_y <= (b + 11):
                                row = r
                                print(f'{b}<y{center_y}<{b + 60}')
                                print(f'{n} {name} строка {row}')
                                points.append((row, column, center_x, center_y, name))
                                print(f'{n} {name} строка {row} столбец {column}')
                                n = n + 1
                                cv.putText(self.screenshot, str(column) + " " + str(row) + " " + name, (x-20, y), cv.FONT_HERSHEY_SIMPLEX, .4, color)'''

            # self.namePoints = namePoints
            # print(f'anybody\n{points}')
            self.points = points
            self.rectangles = rectangles
            # print(rectangles)
            # print(f'{name}\n{points}')
