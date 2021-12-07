from statistics import median

with open("day_7/input.txt") as file:
    INPUT = [int(n) for n in file.read().split(",")]

# The most optimal end position is the median of all starting positions
# rounded to the nearest integer
end = round(median(INPUT))

print(sum(abs(start - end) for start in INPUT))
