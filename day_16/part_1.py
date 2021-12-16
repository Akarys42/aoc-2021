from typing import Optional

with open("day_16/input.txt") as file:
    INPUT = "".join(bin(int(n, base=16))[2:].zfill(4) for n in file.read().strip())


def parse_packet(start: int, end: Optional[int] = None) -> tuple[int, int]:
    version = int(INPUT[start : start + 3], base=2)
    type_ = int(INPUT[start + 3 : start + 6], base=2)

    index = start + 6

    # Literal type
    if type_ == 4:
        while True:
            if INPUT[index] == "0":
                index += 5
                break
            index += 5
    else:
        # Sized packet
        if INPUT[index] == "0":
            size = int(INPUT[index + 1 : index + 16], base=2)
            index += 16
            end_index = index + size

            while True:
                new_version, index = parse_packet(index, index + size)
                version += new_version

                if index == end_index:
                    break
        else:
            size = int(INPUT[index + 1 : index + 12], base=2)
            index += 12

            for _ in range(size):
                new_version, index = parse_packet(index, index + size)
                version += new_version

    return version, index


print(parse_packet(0)[0])
