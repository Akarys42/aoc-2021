# Advent of Code 2021

My solution to the [Advent of Code 2021](https://adventofcode.com/2021) programming challenges. You can find the solution of each part in each daily folder, along with some visualisations and their rendered output in the images folder. 

You will need Python 3.10 to run those solutions. The code is linted using [Black](https://github.com/psf/black).

# Index

Here is a short description of each puzzle:
- 1: Scanning the ocean depth
- 2: Piloting the submarine
- 3: Reading the diagnosis
- 4: Playing bingo against the octopus
- 5: Avoiding the hydrothermal vents
- 6: Counting lanternfishes
- 7: Digging a hole with the crabs
- 8: Decoding the seven segments display
- 9: Finding basins in the cave
- 10: Syntax checking
- 11: Counting octopus flashes
- 12: Counting paths in the cave system
- 13: Activating the infrared camera
- 14: Creating the polymer for the submarine
- 15: Pathfinding through the chitons
- 16: Decode BITS packages
- 17: Calculating the trajectory of torpedo probes
- 18: Snailfish mathematics
- 19: Mapping out scanners
- 20: Enhancing the trench map
- 21: Playing dirac dice
- 22: Rebooting the reactor
- 23: Sending amphipods to their room
- 24: Validating the submarine model number
- 25: Measuring the movement of sea cucumbers

# Timing

Below is a table taking by the full resolution of each puzzle, taking the interpreter startup and shutdown time into account.

The higher the timing is, the more accurate it should be. Hence, anything under 100ms has been replaced with a dash.

Each part is run a few times -depending on the overall time taken- and the best time is reported in the table.

Day|Part 1|Part 2
---|------|------
1|-|-
2|-|-
3|-|-
4|-|-
5|124ms|175ms
6|578ms|-
7|-|340ms
8|-|1.55s
9|-|107ms
10|-|-
11|-|-
12|-|266ms
13|414ms|596ms
14|-|-
15|155ms|4.69s
16|-|-
17|324ms|1.69s
18|261ms|3.30s
19|2.73s|2.73s
20|188ms|12.81s
21|-|293ms
22|732ms|297ms
23|124s¹|17.62s
24|213ms|23.69s
25|2.53s|Victory!

¹ not a typo, I will have to investigate that one at some point and perhaps backport part 2