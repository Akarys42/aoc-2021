import re
from typing import Iterator

with open("day_21/input.txt") as file:
    p1 = int(re.search(r"Player 1 starting position: (\d+)", file.readline()).group(1))
    p2 = int(re.search(r"Player 2 starting position: (\d+)", file.readline()).group(1))


class Dice:
    def __init__(self) -> None:
        self.count = 0
        self.value = 0

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        self.count += 1
        self.value += 1

        if self.value == 101:
            self.value = 1

        return self.value


DICE = Dice()
IDICE = iter(DICE)
score1 = 0
score2 = 0

while True:
    p1 = (p1 + next(IDICE) + next(IDICE) + next(IDICE) - 1) % 10 + 1
    score1 += p1

    if score1 >= 1000:
        break

    p2 = (p2 + next(IDICE) + next(IDICE) + next(IDICE) - 1) % 10 + 1
    score2 += p2

    if score2 >= 1000:
        break

print(min(score1, score2) * DICE.count)
