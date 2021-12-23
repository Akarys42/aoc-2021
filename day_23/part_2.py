import dataclasses

NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))

Board = list[list[str]]


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int

    def value(self, board: Board) -> str:
        return board[self.y][self.x]

    def set_value(self, board: Board, value: str) -> None:
        board[self.y][self.x] = value

    def is_free(self, board: Board) -> bool:
        return self.value(board) == "."


HALLWAY = [Point(x, 1) for x in (1, 2, 4, 6, 8, 10, 11)]
ROOMS = [(Point(x, 2), Point(x, 3), Point(x, 4), Point(x, 5)) for x in (3, 5, 7, 9)]
ROOMS_REVERSED = [list(reversed(points)) for points in ROOMS]
TYPES = dict(zip("ABCD", range(4)))
COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

EXTRA = ["  #D#C#B#A#  ", "  #D#B#A#C#  "]

cache = {}


def copy_board(board: Board) -> Board:
    return [line.copy() for line in board]


def pathfind(board: Board, start: Point, end: Point) -> int:
    backlog = [(start, 0)]
    explored = set()

    while len(backlog) != 0:
        current, cost = backlog.pop()

        if current in explored:
            continue
        explored.add(current)

        for dx, dy in NEIGHBORS:
            x = current.x + dx
            y = current.y + dy
            neighbor = Point(x, y)

            if neighbor == end:
                return cost + 1

            if neighbor.is_free(board):
                backlog.append((neighbor, cost + 1))
    return 0


def find_best(board: Board, score: int) -> int:
    current_best = float("inf")

    room_fill_level: list[int] = []
    room_correct_type: list[bool] = []

    for points, type_ in zip(ROOMS, "ABCD"):
        p1, p2, p3, p4 = points

        room_fill_level.append(sum(int(not p.is_free(board)) for p in points))
        room_correct_type.append(
            type_
            == p1.value(board)
            == p2.value(board)
            == p3.value(board)
            == p4.value(board)
        )

    if all(room_correct_type):
        print(f"Found one solution: {score}")
        return score

    cache_key = "".join("".join(line) for line in board)
    if cache_key in cache:
        return score + cache[cache_key]

    # First try to move any amphipod that is in the hallway to its room
    for point in HALLWAY:
        if not point.is_free(board):
            # Can only move to the correct room
            room = TYPES[point.value(board)]

            if room_fill_level[room] == 4:
                continue

            for i, target in enumerate(ROOMS_REVERSED[room]):
                if target.is_free(board):
                    break

            can_continue = True
            for remaining in ROOMS_REVERSED[room][:i]:
                assert remaining.y > target.y
                if TYPES[remaining.value(board)] != room:
                    assert ROOMS[room][3].value(board) != point.value(board)
                    can_continue = False
                    break

            if not can_continue:
                continue

            # Check we have a path
            if not (cost := pathfind(board, point, target) * COSTS[point.value(board)]):
                continue

            new_board = copy_board(board)

            assert target.is_free(board)
            point.set_value(new_board, ".")
            target.set_value(new_board, point.value(board))

            current_best = min(find_best(new_board, score + cost), current_best)

    # Now we try to move from the rooms to any point in the hallway
    for room in range(4):
        if room_correct_type[room]:
            continue

        if room_fill_level[room] == 0:
            continue

        for i, point in enumerate(ROOMS[room]):
            if not point.is_free(board):
                break

        if all(TYPES[p.value(board)] == room for p in ROOMS[room][i:]):
            continue

        # Try to move to any hallway point
        for target in HALLWAY:
            if not target.is_free(board):
                continue

            # Check we have a path
            if not (cost := pathfind(board, point, target) * COSTS[point.value(board)]):
                continue

            new_board = copy_board(board)

            assert target.is_free(board)
            point.set_value(new_board, ".")
            target.set_value(new_board, point.value(board))

            current_best = min(find_best(new_board, score + cost), current_best)

    cache[cache_key] = current_best - score

    return current_best


with open("day_23/input.txt") as file:
    lines = file.readlines()
    lines = lines[:3] + EXTRA + lines[3:]
    START_BOARD = [list(line) for line in lines]

print(find_best(START_BOARD, 0))
