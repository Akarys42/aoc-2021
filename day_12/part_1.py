PATHS = {}

with open("day_12/input.txt") as file:
    for line in file.readlines():
        a, b = line.strip().split("-")

        PATHS.setdefault(a, []).append(b)
        PATHS.setdefault(b, []).append(a)


def find_path_count(explored: set[str], next_: str) -> int:
    if next_ == "end":
        return 1

    total = 0

    if next_.islower():
        explored.add(next_)

    for node in PATHS.get(next_, []):
        if node not in explored:
            total += find_path_count(explored.copy(), node)

    return total


print(find_path_count(set(), "start"))
