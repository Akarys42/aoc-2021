from typing import Optional
from math import prod

with open("day_16/input.txt") as file:
    INPUT = "".join(bin(int(n, base=16))[2:].zfill(4) for n in file.read().strip())


def parse_packet(start: int, end: Optional[int] = None) -> tuple[int, int]:
    version = int(INPUT[start : start + 3], base=2)
    type_ = int(INPUT[start + 3 : start + 6], base=2)

    index = start + 6

    # Literal type
    if type_ == 4:
        parts = []

        while True:
            parts.append(INPUT[index + 1 : index + 5])

            if INPUT[index] == "0":
                index += 5
                break
            index += 5

        return int("".join(parts), base=2), index
    else:
        values = []

        # Sized packet
        if INPUT[index] == "0":
            size = int(INPUT[index + 1 : index + 16], base=2)
            index += 16
            end_index = index + size

            while True:
                value, index = parse_packet(index, index + size)
                values.append(value)

                if index == end_index:
                    break
        else:
            size = int(INPUT[index + 1 : index + 12], base=2)
            index += 12

            for _ in range(size):
                value, index = parse_packet(index, index + size)
                values.append(value)
        
        # Arthimetic operation
        match type_:
            case 0:
                value = sum(values)
            case 1:
                value = prod(values)
            case 2:
                value = min(values)
            case 3:
                value = max(values)
            case 5:
                value = int(values[0] > values[1])
            case 6:
                value = int(values[0] < values[1])
            case 7:
                value = int(values[0] == values[1])

    return value, index


print(parse_packet(0)[0])
