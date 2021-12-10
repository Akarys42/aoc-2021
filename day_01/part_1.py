with open("day_01/input.txt") as file:
    INPUT = map(int, file.readlines())

previous = None
increases = 0

for current in INPUT:
    if previous and current > previous:
        increases += 1

    previous = current

print(increases)
