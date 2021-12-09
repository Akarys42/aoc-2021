from functools import reduce
from itertools import product
from operator import mul
from typing import Deque

with open("day_9/input.txt") as file:
    BOARD = [[int(n) for n in line.strip()] for line in file.readlines()]

NEIGHBOURS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

SIZE_Y = len(BOARD[0])
SIZE_X = len(BOARD)

totals = []
# vis = [["o"]*SIZE_Y for _ in range(SIZE_X)]

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
        checked = set()
        count = set([(x0, y0)])

        queue = Deque([(x0, y0, -1)])

        while len(queue) != 0:
            x0, y0, prev = queue.popleft()

            if (x0, y0, prev) in checked:
                continue
            checked.add((x0, y0, prev))

            height = BOARD[x0][y0]
            # vis[x0][y0] = "x"

            for dx, dy in NEIGHBOURS:
                x = x0 + dx
                y = y0 + dy

                # Bound check
                if not (0 <= x < SIZE_X and 0 <= y < SIZE_Y):
                    continue

                if BOARD[x][y] >= height and BOARD[x][y] != 9:
                    # Skip if we already took care of it
                    if (x, y, prev) not in checked:
                        queue.append((x, y, height))

                    count.add((x, y))

        totals.append(len(count))

totals.sort()
print(reduce(mul, totals[-3:], 1))
