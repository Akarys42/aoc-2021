from itertools import product

with open("day_20/input.txt") as file:
    ALGORITHM = [c == "#" for c in file.readline().strip()]
    file.readline()  # Empty line
    image = [[c == "#" for c in line.strip()] for line in file.readlines()]

STEPS = 2
BORDER = 2


for step in range(STEPS):
    # While the image is infinite, there is no way any pixel outside of BORDER strips
    # around the current image that can be lighten
    new_image = [
        [None for _ in range(len(image[0]) + BORDER * 2)]
        for _ in range(len(image) + BORDER * 2)
    ]

    # If the value for 0 is true, we may have a different value for the OOB zone
    oob_value = ALGORITHM[0] and (step - 1) % 2 == 0

    for i, line in enumerate(new_image):
        for j in range(len(line)):
            total = 0

            for delta, index in zip(product((1, 0, -1), (1, 0, -1)), range(9)):
                dx, dy = delta
                x = i - BORDER + dx
                y = j - BORDER + dy

                # Bound check
                if not (0 <= x < len(image[0]) and 0 <= y < len(image)):
                    if oob_value:
                        total += 1 << index
                    continue

                if image[x][y]:
                    total += 1 << index

            line[j] = ALGORITHM[total]

    image = new_image

print(sum(sum(line[2:-2]) for line in image[2:-2]))
