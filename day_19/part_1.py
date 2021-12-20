import dataclasses
from decimal import Decimal
from itertools import count, chain, product
from typing import Optional, Literal

REQUIRED_COMMON = 12
AXIS = [*"xyz"]

Axis = Literal["x", "y", "z"]


@dataclasses.dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int
    z: int

    def get(self, axis: Axis) -> int:
        return {"x": self.x, "y": self.y, "z": self.z}[axis]


@dataclasses.dataclass()
class Alignment:
    axis_mapping: dict[Axis, Axis]
    axis_direction: dict[Axis, int]
    offsets: dict[Axis, int]


class Scanner:
    id_counter = count(0)

    def __init__(self, points: list[Point]) -> None:
        self.id = next(self.id_counter)
        self.points = points
        self._distances: Optional[list[set[Decimal]]] = None
        self.to_origin = None

    @property
    def distances(self) -> list[set[Decimal]]:
        if not self._distances:
            self._distances = [set() for _ in range(len(self.points))]

            for i, p1 in enumerate(self.points):
                for j, p2 in enumerate(self.points):
                    self._distances[i].add(
                        Decimal(
                            (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2
                        ).sqrt()
                    )

                self._distances[i].remove(Decimal(0))

        return self._distances

    def find_commons(self, other: "Scanner") -> dict[Point, Point]:
        mapping = {}

        for i, distances_1 in enumerate(self.distances):
            for j, distances_2 in enumerate(other.distances):
                if len(distances_1 & distances_2) >= REQUIRED_COMMON - 1:
                    mapping[self.points[i]] = other.points[j]

        return mapping

    def align(self, commons: dict[Point, Point]) -> Alignment:
        assert len(commons) == 12

        axis_mapping = {}
        axis_direction = {}
        offsets = {}

        # Try each possible mapping for each axis
        for axis in AXIS:
            for mapped_axis, direction in product(AXIS, (-1, 1)):
                deltas = set()

                for p1, p2 in commons.items():
                    deltas.add(p2.get(axis) - p1.get(mapped_axis) * direction)

                # All the points are correctly aligned
                if len(deltas) == 1:
                    axis_mapping[mapped_axis] = axis
                    axis_direction[axis] = direction
                    offsets[axis] = next(iter(deltas))
                    break

        return Alignment(axis_mapping, axis_direction, offsets)

    def set_coordinates(self, al: Alignment) -> None:
        self.to_origin = [
            -1
            * al.offsets[al.axis_mapping[axis]]
            * al.axis_direction[al.axis_mapping[axis]]
            for axis in AXIS
        ]

        new_points = []
        for point in self.points:
            coords = [
                -1
                * al.axis_direction[al.axis_mapping[axis]]
                * (al.offsets[al.axis_mapping[axis]] - point.get(al.axis_mapping[axis]))
                for axis in AXIS
            ]

            new_points.append(Point(*coords))

        self.points = new_points

    def __repr__(self) -> str:
        return f"<Scanner {self.id}>"


scanners: list[Scanner] = []

with open("day_19/input.txt") as file:
    points = []

    for line in chain(file.readlines(), ("--- end of input ---",)):
        # Skip empty lines
        if len(line) == 1:
            continue

        if line.startswith("---"):
            if points:
                scanners.append(Scanner(points))
                points = []
        else:
            points.append(Point(*map(int, line.split(","))))

scanners[0].to_origin = (0, 0, 0)

unchecked = scanners[1:]
checked = [scanners[0]]

while unchecked:
    match = False

    for current, other in product(checked, unchecked):
        commons = current.find_commons(other)

        if len(commons) < REQUIRED_COMMON:
            continue

        alignment = other.align(commons)
        other.set_coordinates(alignment)

        assert len(set(current.points) & set(other.points)) == 12
        match = True
        break

    if not match:
        print(f"Couldn't find any match! {unchecked = }")
        exit(1)
    else:
        unchecked.remove(other)
        checked.append(other)

all_points = set()

for scanner in scanners:
    for point in scanner.points:
        all_points.add(point)

print(len(all_points))
