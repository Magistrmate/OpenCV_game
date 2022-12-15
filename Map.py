import cv2 as cv
from windowcapture import WindowCapture

# wincap = WindowCapture('MI 9')

screenshot = cv.imread('jpg/Map_low.jpg', cv.IMREAD_UNCHANGED)

for x in range(65, 366, 50):
    for y in range(212, 763, 50):
        print(x, y)
        cv.drawMarker(screenshot, (x, y), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)

'''cv.drawMarker(screenshot, (x, 212), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)
cv.drawMarker(screenshot, (65, 212), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)
cv.drawMarker(screenshot, (65, 262), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)
cv.drawMarker(screenshot, (65, 312), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)
cv.drawMarker(screenshot, (65, 312), (0, 255, 0), cv.MARKER_CROSS, 20, 1, cv.LINE_4)'''

cv.imshow('Map', screenshot)
cv.waitKey()
cv.destroyAllWindows()