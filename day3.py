
def calculate_prio(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27


f = open("input3.txt", "r")
sum_priorities = 0
for line in f.readlines():
    line = line.strip()
    part1 = line[:(len(line)//2)]
    part2 = line[len(line)//2:]
    for char in part1:
        if char in part2:
            prio = calculate_prio(char)
            sum_priorities += prio
            break

print(sum_priorities)
