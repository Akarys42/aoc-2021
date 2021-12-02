with open('day_2/input.txt') as file:
    INPUT = [line.split() for line in file.readlines()]

depth = 0
position = 0
aim = 0

for line in INPUT:
    instruction = line[0]
    step = int(line[1])

    match instruction:
        case "forward":
            position += step
            depth += step * aim
        case "up":
            aim -= step
        case "down":
            aim += step
        case unknown:
            raise ValueError(f"Unknown instruction {unknown}")

print(depth * position)