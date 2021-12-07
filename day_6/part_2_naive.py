import time

with open("day_6/input.txt") as file:
    fishes = [int(state) for state in file.read().split(",")]

ITERATIONS = 256

for day in range(ITERATIONS):
    start_time = time.time_ns()

    new_fishes = 0

    for i, state in enumerate(fishes):
        if state == 0:
            fishes[i] = 6
            new_fishes += 1
        else:
            fishes[i] -= 1

    fishes.extend([8] * new_fishes)

    print(f"Computed day {day + 1} in {(time.time_ns() - start_time) * 10e-9:.4f}s")

print(len(fishes))
