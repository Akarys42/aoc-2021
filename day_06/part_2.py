import time

with open("day_06/input.txt") as file:
    INPUT = [int(state) for state in file.read().split(",")]

ITERATIONS = 256

global_state = [0] * 10

for state in INPUT:
    global_state[state] += 1

for day in range(ITERATIONS):
    start_time = time.time_ns()

    new_fishes = global_state[0]

    for i in range(8):
        global_state[i] = global_state[i + 1]

    # New fishes staring at eight
    global_state[8] = new_fishes
    # Old fishes starting back to six
    global_state[6] += new_fishes

    print(f"Computed day {day + 1} in {(time.time_ns() - start_time) * 10e-9:.4f}s")

print(sum(global_state))
