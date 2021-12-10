with open('day_02/input.txt') as file:
    INPUT = [line.split() for line in file.readlines()]

depth = 0
position = 0

for line in INPUT:
    instruction = line[0]
    step = int(line[1])

    match instruction:
        case "forward":
            position += step
        case "up":
            depth -= step
        case "down":
            depth += step
        case unknown:
            raise ValueError(f"Unknown instruction {unknown}")

print(depth * position)