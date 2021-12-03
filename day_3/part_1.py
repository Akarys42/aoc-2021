with open('day_3/input.txt') as file:
    INPUT = file.readlines()

gamma = 0
epsilon = 0

INPUT_LENGTH = len(INPUT)
LINE_LENGTH = len(INPUT[0].strip())

for i in range(LINE_LENGTH):
    count_0 = 0

    for line in INPUT:
        if line[LINE_LENGTH - (i + 1)] == "0":
            count_0 += 1
    
    if count_0 > INPUT_LENGTH / 2:
        gamma += 1 << i
    else:
        epsilon += 1 << i

print(gamma * epsilon)