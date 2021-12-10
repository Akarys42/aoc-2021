with open("day_10/input.txt") as file:
    INPUT = file.readlines()


OPENING = [*"({[<"]
CLOSING = [*")}]>"]
MAPPING = dict(zip(CLOSING, OPENING))
SCORE = {"(": 1, "[": 2, "{": 3, "<": 4}

scores = []

for line in INPUT:
    symbol_stack = []
    is_valid = True

    for symbol in line.strip():
        if symbol in OPENING:
            symbol_stack.append(symbol)
        else:
            # Check if it is closing the right symbol
            if symbol_stack.pop() != MAPPING[symbol]:
                is_valid = False
                break

    if is_valid:
        score = 0

        symbol_stack.reverse()
        for remaining in symbol_stack:
            score = score * 5 + SCORE[remaining]

        scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
