with open('day_3/input.txt') as file:
    INPUT = file.readlines()

life_support = INPUT.copy()
co2_scrubber = INPUT.copy()

INPUT_LENGTH = len(INPUT)
LINE_LENGTH = len(INPUT[0].strip())

def list_iteration(list_: list[str], by_most_common: bool, i: int) -> list[str]:
    if len(list_) == 1:
        return list_

    count_0 = 0

    for line in list_:
        if line[i] == "0":
            count_0 += 1
    
    if count_0 > len(list_) / 2:
        most_common = "0"
        least_common = "1"
    elif count_0 < len(list_) / 2:
        most_common = "1"
        least_common = "0"
    else:
        if by_most_common:
            most_common = "1"
            least_common = "0"
        else:
            most_common = "1"
            least_common = "0"
    
    common = most_common if by_most_common else least_common

    new_list = []

    for line in list_:
        if line[i] == common:
            new_list.append(line)
    
    return new_list



for i in range(LINE_LENGTH):
    life_support = list_iteration(life_support, True, i)
    co2_scrubber = list_iteration(co2_scrubber, False, i)

assert len(life_support) == 1
assert len(co2_scrubber) == 1

print(int(life_support[0], 2) * int(co2_scrubber[0], base=2))