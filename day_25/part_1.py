import itertools

with open("day_25/input.txt") as file:
    board = [list(line.strip()) for line in file.readlines()]

SIZE_X = len(board[0])
SIZE_Y = len(board)

STEP_COUNTER = itertools.count(1)
has_changed = True

while has_changed:
    has_changed = False
    step = next(STEP_COUNTER)

    for direction, size in zip((">", "v"), (SIZE_X, SIZE_Y)):
        for i, line in enumerate(board):
            new_line = line.copy()

            for j, cucumber in enumerate(line):
                if direction != cucumber:
                    continue

                next_location = (j + 1) % size

                if line[next_location] == ".":
                    new_line[next_location] = direction
                    new_line[j] = "."
                    has_changed = True

            board[i] = new_line

        board = list(map(list, zip(*board)))  # Turn the board sideway

print(step)
