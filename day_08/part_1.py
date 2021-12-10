from collections import Counter
import re


with open("day_08/input.txt") as file:
    INPUT = re.sub(r".+ \|", "", file.read()).split()

# This one is quite free, since all the digits we want
# to count have a unique number of segments
digit_lengths = Counter(len(digit) for digit in INPUT)

# Mapping of unique length digits
# 2 -> 1
# 4 -> 4
# 3 -> 7
# 7 -> 8
print(digit_lengths[2] + digit_lengths[4] + digit_lengths[3] + digit_lengths[7])
