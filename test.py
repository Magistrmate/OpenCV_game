from operator import itemgetter
points = [[397, 362, 'duck', (0, 191, 255), (8, 3)], [295, 413, 'duck', (0, 191, 255), (6, 4)]]
for point in points:
    column = pointOne[4][0]
    row = pointOne[4][1]
    name = pointOne[2]
    print(itemgetter(0)(points))

    # ps = [(2, 4), (-1, 7), (4, 5), (3, -4), (-1, -5)]
    # got = itemgetter(0, 2, 3)(ps)
    # print(got)
