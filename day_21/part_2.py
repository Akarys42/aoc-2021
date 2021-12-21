import functools
import re
from itertools import product


ROLLS = [sum(elems) for elems in product(*[(1, 2, 3)] * 3)]


@functools.lru_cache(maxsize=None)
def total_wins(
    p1: int, p2: int, score1: int, score2: int, plays1: bool
) -> tuple[int, int]:
    if score1 >= 21:
        return 1, 0

    if score2 >= 21:
        return 0, 1

    wins1 = 0
    wins2 = 0

    for roll in ROLLS:
        if plays1:
            new_p1 = (p1 + roll - 1) % 10 + 1
            new_score1 = score1 + new_p1
            new_p2 = p2
            new_score2 = score2
        else:
            new_p1 = p1
            new_score1 = score1
            new_p2 = (p2 + roll - 1) % 10 + 1
            new_score2 = score2 + new_p2
        a, b = total_wins(new_p1, new_p2, new_score1, new_score2, not plays1)

        wins1 += a
        wins2 += b

    return wins1, wins2


with open("day_21/input.txt") as file:
    START_P1 = int(
        re.search(r"Player 1 starting position: (\d+)", file.readline()).group(1)
    )
    START_P2 = int(
        re.search(r"Player 2 starting position: (\d+)", file.readline()).group(1)
    )

print(max(total_wins(START_P1, START_P2, 0, 0, True)))
