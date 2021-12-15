from __future__ import annotations

# Things are getting serious!
# We are going to use A* for that one, with the following functions:
# G cost: sum of the dangers in the path
# H cost: distance to the end point
#
# For more information: https://en.wikipedia.org/wiki/A*_search_algorithm

from functools import lru_cache
from math import sqrt
import bisect

with open("day_15/input.txt") as file:
    DANGER_MAP = [[int(n) for n in line.strip()] for line in file.readlines()]

SIZE = len(DANGER_MAP)
# Assert that it is a square
assert len(DANGER_MAP[0]) == SIZE

Coords: tuple[int, int]


def edge_g_cost(coords: Coords) -> int:
    offset = coords[0] // SIZE + coords[1] // SIZE

    return (DANGER_MAP[coords[1] % SIZE][coords[0] % SIZE] + offset - 1) % 9 + 1


@lru_cache
def h_cost(coords: Coords) -> float:
    return sqrt((SIZE - coords[0]) ** 2 + (SIZE - coords[1]) ** 2)


START = (0, 0)
GOAL = (5 * SIZE - 1, 5 * SIZE - 1)

NEIGHBORS = ((-1, 0), (0, 1), (1, 0), (0, -1))

open_set: list[Coords] = [START]
previous_node: dict[Coords, Coords] = {}

g_cost = {START: 0}
f_cost = {START: h_cost(START)}

while open_set:
    current = open_set.pop(0)
    if current == GOAL:
        print(g_cost[GOAL])
        exit()

    for dx, dy in NEIGHBORS:
        neighbor = (current[0] + dx, current[1] + dy)

        # Bound check
        if not (0 <= neighbor[0] < 5 * SIZE and 0 <= neighbor[1] < 5 * SIZE):
            continue

        tentative_g_cost = g_cost[current] + edge_g_cost(neighbor)
        # If it is a better path
        if tentative_g_cost < g_cost.get(neighbor, float("inf")):
            previous_node[neighbor] = current
            g_cost[neighbor] = tentative_g_cost
            f_cost[neighbor] = tentative_g_cost + h_cost(neighbor)

            # We keep our open_set sorted
            if neighbor not in open_set:
                bisect.insort(open_set, neighbor, key=f_cost.__getitem__)
