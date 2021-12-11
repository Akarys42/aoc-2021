from itertools import product, count
from queue import Queue

with open("day_11/input.txt") as file:
    board = [[int(n) for n in line.strip()] for line in file.readlines()]

SIZE_X = len(board[0])
SIZE_Y = len(board)

STEPS = 100

SQUID_COUNT = SIZE_X * SIZE_Y

for step in count(1):
    flashes = 0

    for x0, y0 in product(range(SIZE_X), range(SIZE_Y)):
        board[x0][y0] += 1

        # Only if it is equal to 10 as it can only flash once per step
        if board[x0][y0] == 10:
            flash_queue = Queue()
            flash_queue.put((x0, y0))

            while not flash_queue.empty():
                x0, y0 = flash_queue.get()
                flashes += 1

                for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
                    x = x0 + dx
                    y = y0 + dy

                    # Bound check
                    if not (0 <= x < SIZE_X and 0 <= y < SIZE_Y):
                        continue

                    board[x][y] += 1

                    # Check if this new cell flashed
                    if board[x][y] == 10:
                        flash_queue.put((x, y))

    if flashes == SQUID_COUNT:
        print(step)
        exit()

    # Normalize back to 0
    for x, y in product(range(SIZE_X), range(SIZE_Y)):
        if board[x][y] > 10:
            board[x][y] = 0
