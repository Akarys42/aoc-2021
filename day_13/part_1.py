with open("day_13/input.txt") as file:
    input_, instructions = file.read().split("\n\n")

INPUT = [[int(n) for n in line.split(",")] for line in input_.splitlines()]
INSTRUCTIONS = [
    instruction.removeprefix("fold along ").split("=")
    for instruction in instructions.splitlines()
]

size_x = max(p[0] for p in INPUT) + 1
size_y = max(p[1] for p in INPUT) + 1

board = [[False for _ in range(size_x)] for _ in range(size_y)]

for x, y in INPUT:
    board[y][x] = True

direction, middle = INSTRUCTIONS[0]
middle = int(middle)

if direction == "y":
    size_y = middle

    new_board = [[False for _ in range(size_x)] for _ in range(size_y)]

    for y, line in enumerate(board):
        if y < middle:
            eff_y = y
        elif y > middle:
            eff_y = 2 * middle - y
        else:
            # the middle line is discarded
            continue

        for x, value in enumerate(line):
            new_board[eff_y][x] |= value
else:
    size_x = middle

    new_board = [[False for _ in range(size_x)] for _ in range(size_y)]

    for y, line in enumerate(board):
        for x, value in enumerate(line):
            if x < middle:
                eff_x = x
            elif x > middle:
                eff_x = 2 * middle - x
            else:
                # the middle line is discarded
                continue

            new_board[y][eff_x] |= value

print(sum(sum(line) for line in new_board))
