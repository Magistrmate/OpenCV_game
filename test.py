# from operator import itemgetter
# points = [[(397, 362), 'duck', (0, 191, 255), (8, 3)], [(295, 413), 'duck', (0, 191, 255), (6, 4)]]
# for point in points:
#     point.insert(3, 'right2')
#
# print(points)

# for i in range(2, -3, -1):
#     print(f'i {i}')
#     # for n in range(3 - i, -1, -1):
#     #     print(f'n {n}')

# for i in range(1, -2, -1):
#     print(i)
#     print(9 + i)

# pointChance = [('right1', 'right2'), ('left1', 'left2'), (-1, 0, 1)]
# for (r, i) in zip(pointChance, enumerate(pointChance[2])):
#     print(r)
#     print(i[0])
#     # 0
#     # 1 0
#     #
#     print(i[2], i[3])
#     # 1
#     # -1 0
#     # 1 - 2
#     print(i[0], i[1])
#     # 2
#     # 0 -1
#     # 2 - 2
#     print(i[1], i[0])
#     # 3 0
#     # 1
#     # 3 - 3
#     print(i[1], i[2])

# for (m, d) in zip((1, -1), (0, 10)):  # 2 4
#     for (c, n) in zip(range(-7 * m, 0, m), range(8 + d, 21 + d * 3, (3 - m))):
#         print('\n')
#         for r in range(-1, 2, 1):
#             print(f'{m} + {c} + {r} = {m + c + r} + {n} = {m + c + r + n}')
# for (m, d) in zip((1, -1), (0, 12)):
#     for (c, n) in zip(range(-12 * m, -1 * m, m), range(61 + d, 91 + d * 2, (3 - m))):
#         print('\n')
#         for r in range(-1, 2, 1):
#             print(f'{m} + {r} + {c} = {m + r + c} + {n} = {m + r + c + n}')
# points = [[(38, 260), ('ball', 't', 0, 'c', 0, 'g', 0, 'p', False), (0, 255, 0), (1, 1)],
#           [(38, 311), ('ball', 't', 0, 'c', 0, 'g', 0, 'p', False), (0, 255, 0), (1, 2)]]
# subPoint = ('', 't', 0, 'c', 0, 'g', 0, 'p', False)
# for point in points:
#     point.append(['left', [['', 't', 0, 'c', 0, 'g', 0, 'p', False]] * 2])
# print(points)
# envelopeMatchUpDown = ['l', [0, 't', 0, 'c', 0], 'r', [0, 't', 0, 'c', 0]]
# envelopeMatchUpDown[1][0] = envelopeMatchUpDown[3][0] = 1
# envelopeMatchUpDown[1][2] = envelopeMatchUpDown[3][2] = 1
# envelopeMatchUpDown[1][0] = envelopeMatchUpDown[1][0] + 3
# print(envelopeMatchUpDown)
import cv2
import time
from windowcapture import WindowCapture
# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
TIMER = int(20)

wincap = WindowCapture('22071212AG')

while True:

    # Read and display each frame
    screenshot = wincap.get_screenshot()
    cv2.imshow('Map', screenshot)
    # check for the key pressed
    k = cv2.waitKey(125)

    # set the key for the countdown
    # to begin. Here we set q
    # if key pressed is q
    if k == ord('q'):
        prev = time.time()

        while TIMER >= 0:
            screenshot = wincap.get_screenshot()

            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(screenshot, str(TIMER),
                        (200, 250), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('a', screenshot)
            cv2.waitKey(125)

            # current time
            cur = time.time()

            # Update and keep track of Countdown
            # if time elapsed is one second
            # then decrease the counter
            if cur - prev >= 1:
                prev = cur
                TIMER = TIMER - 1

        else:
            ret, img = cap.read()

            # Display the clicked frame for 2
            # sec.You can increase time in
            # waitKey also
            cv2.imshow('a', img)

            # time for which image displayed
            cv2.waitKey(2000)

            # Save the frame
            cv2.imwrite('camera.jpg', img)

        # HERE we can reset the Countdown timer
        # if we want more Capture without closing
        # the camera

    # Press Esc to exit
    elif k == 27:
        break

# close the camera
cap.release()

# close all the opened windows
cv2.destroyAllWindows()
