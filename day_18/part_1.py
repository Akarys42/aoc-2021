import ast
from math import ceil, floor
from typing import Optional, Union, Iterator


class Operand:
    def __init__(
        self, l: ["Operand", int], r: ["Operand", int], parent: Optional["Operand"]
    ) -> None:
        self.l = l
        self.r = r

        if isinstance(l, Operand):
            l.parent = self
        if isinstance(r, Operand):
            r.parent = self

        self.parent = parent

    def count_parents(self) -> int:
        parents = 0
        current = self.parent

        while current is not None:
            parents += 1
            current = current.parent

        return parents

    @property
    def leftmost(self) -> "Operand":
        return self if isinstance(self.l, int) else self.l.leftmost

    @property
    def rightmost(self) -> "Operand":
        return self if isinstance(self.r, int) else self.r.rightmost

    @property
    def previous_node(self) -> Optional["Operand"]:
        if not self.parent:
            return

        if self.parent.l is self:
            return self.parent.previous_node

        if not isinstance(self.parent.l, int):
            return self.parent.l.rightmost

        return self.parent

    @property
    def next_node(self) -> Optional["Operand"]:
        if not self.parent:
            return

        if self.parent.r is self:
            return self.parent.next_node

        if not isinstance(self.parent.r, int):
            return self.parent.r.leftmost

        return self.parent

    def explode(self) -> bool:
        if self.count_parents() < 4:
            return False

        # Get the appropriate nodes
        previous_node, next_node = self.previous_node, self.next_node

        if previous_node:
            if not isinstance(previous_node.r, int):
                previous_node.l += self.l
            else:
                previous_node.r += self.l

        if next_node:
            if not isinstance(next_node.l, int):
                next_node.r += self.r
            else:
                next_node.l += self.r

        # Replace itself with 0
        if self.parent:
            if self.parent.l is self:
                self.parent.l = 0
            else:
                self.parent.r = 0

        return True

    def split(self) -> bool:
        if isinstance(self.l, int) and self.l > 9:
            self.l = Operand(floor(self.l / 2), ceil(self.l / 2), self)
            return True

        if isinstance(self.r, int) and self.r > 9:
            self.r = Operand(floor(self.r / 2), ceil(self.r / 2), self)
            return True

        return False

    def reduce(self) -> None:
        while any(node.explode() for node in self.iter_down()) or any(
            node.split() for node in self.iter_down()
        ):
            continue

    def iter_down(self) -> Iterator["Operand"]:
        if not isinstance(self.l, int):
            yield from self.l.iter_down()

        yield self

        if not isinstance(self.r, int):
            yield from self.r.iter_down()

    @property
    def magnitude(self) -> int:
        total = 0

        if isinstance(self.l, int):
            total += 3 * self.l
        else:
            total += 3 * self.l.magnitude

        if isinstance(self.r, int):
            total += 2 * self.r
        else:
            total += 2 * self.r.magnitude

        return total

    @classmethod
    def from_input(
        cls, input_: Union[str, list[...]], parent: Optional["Operand"] = None
    ) -> "Operand":
        if isinstance(input_, str):
            parsed = ast.literal_eval(input_)
        else:
            parsed = input_
        assert len(parsed) == 2

        operand = cls(None, None, parent)

        l, r = parsed
        if not isinstance(l, int):
            l = cls.from_input(l, operand)
        if not isinstance(r, int):
            r = cls.from_input(r, operand)

        operand.l = l
        operand.r = r

        return operand

    def __add__(self, other: "Operand") -> "Operand":
        if not isinstance(other, Operand):
            return NotImplemented

        op = type(self)(self, other, None)
        self.parent = op
        other.parent = op

        op.reduce()
        return op

    def __str__(self) -> str:
        return f"[{self.l},{self.r}]"


total = None

with open("day_18/input.txt") as file:
    for line in file.readlines():
        new_operand = Operand.from_input(line)

        if total:
            total = total + new_operand
        else:
            total = new_operand

print(total.magnitude)
