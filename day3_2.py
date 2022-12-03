
def calculate_prio(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27


f = open("input3.txt", "r")
sum_priorities = 0
group = []
for line in f.readlines():
    line = line.strip()
    group.append(line)
    if len(group) == 3:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                prio = calculate_prio(char)
                sum_priorities += prio
                break
        group = []

print(sum_priorities)
