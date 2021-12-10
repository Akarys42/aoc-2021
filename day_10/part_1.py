with open("day_10/input.txt") as file:
    INPUT = file.readlines()


OPENING = [*"({[<"]
CLOSING = [*")}]>"]
MAPPING = dict(zip(CLOSING, OPENING))
SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}

total_score = 0

for line in INPUT:
    symbol_stack = []

    for symbol in line.strip():
        if symbol in OPENING:
            symbol_stack.append(symbol)
        else:
            # Check if it is closing the right symbol
            if symbol_stack.pop() != MAPPING[symbol]:
                total_score += SCORE[symbol]
                break

print(total_score)
