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

for (m, d) in zip((1, -1), (0, 7)):  # 2 4
    for (c, n) in zip(range(-4 * m, m, m), range(5 + d, 12 + d * 2, (3 - m))):
        print('\n')
        for r in range(-1, 2, 1):
            print(f'{m} + {c} + {r} = {m + c + r} + {n} = {m + c + r + n}')
