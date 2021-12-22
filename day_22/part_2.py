import dataclasses
import re
from math import prod


@dataclasses.dataclass
class Cube:
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int
    value: bool

    def overlaps(self, other: "Cube") -> bool:
        return not any(
            a[1] < b[0] or b[1] < a[0] for a, b in zip(self.bounds, other.bounds)
        )

    def intersection(self, other: "Cube", value: bool) -> "Cube":
        assert self.overlaps(other)
        return Cube(
            max(self.x_min, other.x_min),
            min(self.x_max, other.x_max),
            max(self.y_min, other.y_min),
            min(self.y_max, other.y_max),
            max(self.z_min, other.z_min),
            min(self.z_max, other.z_max),
            value,
        )

    @property
    def bounds(self) -> tuple[tuple[int, int], ...]:
        return (
            (self.x_min, self.x_max),
            (self.y_min, self.y_max),
            (self.z_min, self.z_max),
        )

    @property
    def volume(self) -> int:
        return prod(max_ - min_ + 1 for min_, max_ in self.bounds)

    @property
    def eff_volume(self) -> int:
        return (1 if self.value else -1) * self.volume

    @classmethod
    def from_parts(cls, *parts: str) -> "Cube":
        assert len(parts) == 7
        return cls(*map(int, parts[1:]), parts[0] == "on")


INSTRUCTION_REGEX = re.compile(
    r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
)


with open("day_22/sample.txt") as file:
    INSTRUCTIONS = [
        Cube.from_parts(*INSTRUCTION_REGEX.search(line).groups())
        for line in file.readlines()
    ]

cubes: list[Cube] = []

for instruction in INSTRUCTIONS:
    new_cubes: list[Cube] = []

    for other_cube in cubes:
        if instruction.overlaps(other_cube):
            new_cubes.append(instruction.intersection(other_cube, not other_cube.value))

    cubes.extend(new_cubes)

    if instruction.value:
        cubes.append(instruction)

print(sum(cube.eff_volume for cube in cubes))
