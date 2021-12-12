PATHS = {}

with open("day_12/input.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split("-")

        PATHS.setdefault(a, []).append(b)
        if a != "start":
            PATHS.setdefault(b, []).append(a)


def find_path_count(explored: set[str], visited_twice: bool, next_: str) -> int:
    if next_ == "end":
        return 1

    total = 0

    if next_.islower():
        explored.add(next_)

    for node in PATHS.get(next_, []):
        # For each iteration our new visited_twice value may be different
        _visited_twice = visited_twice

        # The start node cannot be revisited
        if node == "start":
            continue

        # The node has already been explored and we used the second visit, this path is dead
        if node in explored and _visited_twice:
            continue

        # The node has already been visited but we didn't do any second visit yet, this path can continue
        if node in explored and not _visited_twice:
            _visited_twice = True

        total += find_path_count(explored.copy(), _visited_twice, node)

    return total


print(find_path_count(set(), False, "start"))
