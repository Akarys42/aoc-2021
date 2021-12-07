with open("day_1/input.txt") as file:
    INPUT = list(map(int, file.readlines()))

previous = None
increases = 0

for i in range(3, len(INPUT) + 1):
    current = sum(INPUT[i - 3 : i])

    if previous and previous < current:
        increases += 1

    previous = current

print(increases)
