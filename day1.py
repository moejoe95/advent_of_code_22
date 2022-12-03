inventories = []
f = open("input1.txt", "r")
current = 0
for line in f.readlines():
    snack = line.strip()
    if len(snack) == 0:
        inventories.append(current)
        current = 0
    else:
        current += int(snack)

sorted_desc = sorted(inventories, reverse=True)
top = sorted_desc[:1][0]
# step 1
print(top)

# step 2
top_three = sorted_desc[:3]
print(sum(top_three))
