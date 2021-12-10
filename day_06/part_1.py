with open("day_06/input.txt") as file:
    fishes = [int(state) for state in file.read().split(",")]

ITERATIONS = 80

for _ in range(ITERATIONS):
    new_fishes = 0

    for i, state in enumerate(fishes):
        if state == 0:
            fishes[i] = 6
            new_fishes += 1
        else:
            fishes[i] -= 1

    fishes.extend([8] * new_fishes)

print(len(fishes))
