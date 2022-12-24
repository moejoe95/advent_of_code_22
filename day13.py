
def in_order(part1, part2, mixed=False):
    if type(part1) is str:
        part1 = eval(part1, {}, {})
        part2 = eval(part2, {}, {})
    if type(part1) is int and type(part2) is int:
        return part1 <= part2
    if type(part1) is list and type(part2) is int:
        return in_order(part1, [part2], mixed=True)
    if type(part2) is list and type(part1) is int:
        return in_order([part1], part2, mixed=True)
    if type(part1) is list and type(part2) is list:
        indices_in_order = [in_order(item1, item2)
                            for item1, item2 in zip(part1, part2)]
        list_in_order = all(indices_in_order)
        if not mixed:
            list_in_order = list_in_order and len(part1) <= len(part2)
        return list_in_order
    return part1 == part2


index = 1
index_sum = 0
with open('example13_b.txt', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        part1 = lines[i].strip()
        part2 = lines[i+1].strip()
        if in_order(part1, part2):
            print(index)
            index_sum += index
        index += 1

print(index_sum)
