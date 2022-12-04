

def full_overlap(range1, range2):
    if range1[0] <= range2[0] and range2[1] <= range1[1]:  # range1 fully contains range2
        return 1
    if range2[0] <= range1[0] and range1[1] <= range2[1]:  # range2 fully contains range1
        return 1
    return 0


def overlap(range1, range2):
    range1 = range(range1[0], range1[1]+1)
    range2 = range(range2[0], range2[1]+1)
    intersection = set(range1).intersection(set(range2))
    return 1 if len(intersection) > 0 else 0


with open('input4.txt', 'r') as f:
    full_overlaps = 0
    overlaps = 0
    for line in f.readlines():
        range1, range2 = line.strip().split(',')
        range1 = [int(x) for x in range1.split('-')]
        range2 = [int(x) for x in range2.split('-')]

        full_overlaps += full_overlap(range1, range2)
        overlaps += overlap(range1, range2)

    print('step 1:', full_overlaps)
    print('step 2:', overlaps)
