import dataclasses


@dataclasses.dataclass
class Point:
    x: int
    y: int


def interval(a: int, b: int) -> range:
    return range(min(a, b), max(a, b) + 1)

def drange(a: int, b: int) -> range:
    if a < b:
        return range(a, b + 1)
    return range(a, b - 1, -1)


with open("day_5/input.txt") as file:
    INPUT = [[Point(*(int(n) for n in pair.split(","))) for pair in line.split(" -> ")] for line in file.readlines()]

board = {}

for p1, p2 in INPUT:
    # Horizontal line
    if p1.x == p2.x:
        for i in interval(p1.y, p2.y):
            board[(p1.x, i)] = board.get((p1.x, i), 0) + 1
    
    # Vertical line
    elif p1.y == p2.y:
        for i in interval(p1.x, p2.x):
            board[(i, p1.y)] = board.get((i, p1.y), 0) + 1
    
    # Diagonal line
    elif abs(p1.x - p2.x) == abs(p1.y - p2.y):
        for x, y in zip(drange(p1.x, p2.x), drange(p1.y, p2.y)):
            board[(x, y)] = board.get((x, y), 0) + 1

print(sum(1 for v in board.values() if v > 1))