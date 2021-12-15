from collections import defaultdict
from typing import Counter


with open("day_14/input.txt") as file:
    START_MOLECULE = file.readline().strip()
    file.readline()  # Blank line
    RULES = dict(line.strip().split(" -> ") for line in file.readlines())

STEPS = 40

total_elements = defaultdict(lambda: 0)
for element in START_MOLECULE:
    total_elements[element] += 1

patterns = defaultdict(lambda: 0)

for i in range(len(START_MOLECULE) - 1):
    key = START_MOLECULE[i] + START_MOLECULE[i + 1]
    patterns[key] += 1

for _ in range(STEPS):
    new_patterns = defaultdict(lambda: 0)

    for pattern, extra in RULES.items():
        count = patterns[pattern]

        total_elements[extra] += count
        new_patterns[pattern[0] + extra] += count
        new_patterns[extra + pattern[1]] += count

    patterns = new_patterns

counter = Counter(total_elements).most_common()
print(counter[0][1] - counter[-1][1])
