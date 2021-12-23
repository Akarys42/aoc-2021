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
ROOMS = [(Point(x, 2), Point(x, 3)) for x in (3, 5, 7, 9)]
TYPES = dict(zip("ABCD", range(4)))
COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

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
        top, bottom = points

        room_fill_level.append(
            int(not top.is_free(board)) + int(not bottom.is_free(board))
        )
        room_correct_type.append(type_ == top.value(board) == bottom.value(board))

    if all(room_correct_type):
        return score

    cache_key = "".join("".join(line) for line in board)
    if cache_key in cache:
        return score + cache[cache_key]

    # First try to move any amphipod that is in the hallway to its room
    for point in HALLWAY:
        if not point.is_free(board):
            # Can only move if the type of the room is correct
            room = TYPES[point.value(board)]
            top, bottom = ROOMS[room]

            if room_fill_level[room] == 2:
                continue

            if room_fill_level[room] == 1:
                target = top

                if TYPES[bottom.value(board)] != room:
                    continue
            else:
                target = bottom

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

    # Now we try to move from the rooms to any point in the hallway
    for room in range(4):
        top, bottom = ROOMS[room]

        if room_correct_type[room]:
            assert TYPES[top.value(board)] == TYPES[bottom.value(board)] == room
            continue

        if room_fill_level[room] == 0:
            assert top.value(board) == bottom.value(board) == "."
            continue

        if top.is_free(board):
            point = bottom

            if TYPES[bottom.value(board)] == room:
                continue
        else:
            point = top

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

    if current_best != float("inf"):
        cache[cache_key] = current_best - score

    return current_best


with open("day_23/input.txt") as file:
    START_BOARD = [list(line) for line in file.readlines()]

print(find_best(START_BOARD, 0))
