import itertools


def in_order(part1, part2):
    if type(part1) is str:
        part1 = eval(part1, {}, {})
        part2 = eval(part2, {}, {})
    if part1 is None:
        return True
    if part2 is None:
        return False
    if type(part1) is int and type(part2) is int:
        if part1 == part2:
            return None
        return part1 < part2
    if type(part1) is list and type(part2) is int:
        return in_order(part1, [part2])
    if type(part2) is list and type(part1) is int:
        return in_order([part1], part2)
    if type(part1) is list and type(part2) is list:
        indices_in_order = [in_order(item1, item2)
                            for item1, item2 in itertools.zip_longest(part1, part2)]
        for index in indices_in_order:
            if index == True:
                return True
            if index == False:
                return False
        return None


index = 1
index_sum = 0
with open('input13.txt', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        part1 = lines[i].strip()
        part2 = lines[i+1].strip()
        if in_order(part1, part2):
            index_sum += index
        index += 1

print(index_sum)
