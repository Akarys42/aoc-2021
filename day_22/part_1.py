import dataclasses
import re
from itertools import product


@dataclasses.dataclass
class Instruction:
    value: bool
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int

    @property
    def bounds(self) -> tuple[tuple[int, int], ...]:
        return (
            (self.x_min, self.x_max),
            (self.y_min, self.y_max),
            (self.z_min, self.z_max),
        )

    @classmethod
    def from_parts(cls, *parts: str) -> "Instruction":
        assert len(parts) == 7
        return cls(parts[0] == "on", *map(int, parts[1:]))


INSTRUCTION_REGEX = re.compile(
    r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
)


with open("day_22/input.txt") as file:
    INSTRUCTIONS = [
        Instruction.from_parts(*INSTRUCTION_REGEX.search(line).groups())
        for line in file.readlines()
    ]

turned_on = set()

for instruction in INSTRUCTIONS:
    for x, y, z in product(
        *[
            range(max((-50, min_bound)), min((50, max_bound)) + 1)
            for min_bound, max_bound in instruction.bounds
        ]
    ):
        if instruction.value:
            turned_on.add((x, y, z))
        else:
            turned_on.discard((x, y, z))

print(len(turned_on))
