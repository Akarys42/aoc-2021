import re

with open("day_17/input.txt") as file:
    X_MIN, X_MAX, Y_MIN, Y_MAX = map(
        int,
        re.search(
            r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", file.read()
        ).groups(),
    )

# We just take a fucking guess
for v0y in range(200, 0, -1):
    for v0x in range(1, 200):
        vx = v0x
        vy = v0y
        x = 0
        y = 0
        peak = 0

        while True:
            # Update our velocity and position
            if vx > 0:
                x += vx
            y += vy
            vx -= 1
            vy -= 1

            # Update the peak
            if y > peak:
                peak = y

            if X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX:
                print(peak)
                exit()

            # We went over the target or were too short
            if x > X_MAX or y < Y_MIN:
                break
exit(1)  # Our guess was bad
