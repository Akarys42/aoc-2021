from typing import Counter


with open("day_14/input.txt") as file:
    molecule = list(file.readline().strip())
    file.readline()  # Blank line
    RULES = dict(line.strip().split(" -> ") for line in file.readlines())

STEPS = 10

for _ in range(STEPS):
    new_molecule = []
    prev_element = "-"

    for element in molecule:
        if extra_element := RULES.get(prev_element + element, None):
            new_molecule.append(extra_element)

        new_molecule.append(element)
        prev_element = element

    molecule = new_molecule

counter = Counter(molecule).most_common()
print(counter[0][1] - counter[-1][1])
