from itertools import product

with open("day_09/input.txt") as file:
    BOARD = [[int(n) for n in line.strip()] for line in file.readlines()]

NEIGHBOURS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

SIZE_Y = len(BOARD[0])
SIZE_X = len(BOARD)

risk = 0

for x0, y0 in product(range(SIZE_X), range(SIZE_Y)):
    height = BOARD[x0][y0]

    lowest_point = True

    for dx, dy in NEIGHBOURS:
        x = x0 + dx
        y = y0 + dy

        # Bound check
        if not (0 <= x < SIZE_X and 0 <= y < SIZE_Y):
            continue

        if BOARD[x][y] <= height:
            lowest_point = False
            break

    if lowest_point:
        risk += height + 1

print(risk)
