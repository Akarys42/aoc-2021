import functools
import sys

with open("day_07/input.txt") as file:
    INPUT = [int(n) for n in file.read().split(",")]

sys.setrecursionlimit(10 ** 6)


@functools.lru_cache(None)
def cost(n: int) -> int:
    if n == 0:
        # This sin is why it isn't called factorial
        return 0

    return cost(n - 1) + n


best_score = None

for end in range(min(INPUT), max(INPUT) + 1):
    score = sum(cost(abs(n - end)) for n in INPUT)

    if not best_score or score < best_score:
        best_score = score

print(best_score)
