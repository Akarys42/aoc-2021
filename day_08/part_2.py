from functools import reduce
import itertools
from typing import Optional

with open("day_08/input.txt") as file:
    INPUT = [[part.split() for part in line.split(" | ")] for line in file.readlines()]

# We note every segment as a bitmask to make things easier
a = 1 << 0
b = 1 << 1
c = 1 << 2
d = 1 << 3
e = 1 << 4
f = 1 << 5
g = 1 << 6
SEGMENTS = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g}


def pattern_to_hash(pattern: str) -> int:
    hash_ = 0

    for segment in pattern:
        hash_ |= SEGMENTS[segment]

    return hash_


WIRES = [*"abcdefg"]
DIGITS = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]
HASH_TO_DIGIT = {pattern_to_hash(pattern): i for i, pattern in enumerate(DIGITS)}


def validate_pattern(pattern: str, mapping: dict[str, str]) -> Optional[int]:
    new_pattern = "".join(mapping[segment] for segment in pattern)

    return HASH_TO_DIGIT.get(pattern_to_hash(new_pattern), None)


total = 0

for line in INPUT:
    patterns = list(itertools.chain(*line))

    resolved = False

    for out_mapping in itertools.permutations(WIRES):
        mapping = dict(zip(WIRES, out_mapping))

        if not all(
            validate_pattern(pattern, mapping) is not None for pattern in patterns
        ):
            continue

        resolved = True

        total += reduce(
            lambda previous, pattern: previous * 10
            + validate_pattern(pattern, mapping),
            line[1],
            0,
        )
        break

    assert resolved

print(total)
