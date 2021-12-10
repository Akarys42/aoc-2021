import matplotlib.pyplot as plt
import sys
import functools

with open("day_07/input.txt") as file:
    INPUT = [int(n) for n in file.read().split(",")]

sys.setrecursionlimit(10 ** 6)


@functools.lru_cache(None)
def cost(n: int) -> int:
    if n == 0:
        # This sin is why it isn't called factorial
        return 0

    return cost(n - 1) + n


scores_1 = []
scores_2 = []
keys = []

for end in range(min(INPUT), max(INPUT) + 1):
    keys.append(end)

    scores_1.append(sum(abs(start - end) for start in INPUT))
    scores_2.append(sum(cost(abs(start - end)) for start in INPUT))

plt1 = plt.figure(1)
plt.plot(scores_1)
plt.xlabel("End position")
plt.ylabel("Score")
plt.title("Day 7 part 1")
plt.savefig("images/7-1.png")

plt2 = plt.figure(2)
plt.plot(scores_2)
plt.title("Day 7 part 2")
plt.savefig("images/7-2.png")
