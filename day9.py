import operator


coord_head = [0, 0]
coord_tail = [0, 0]
coord_inter = [[0, 0] for _ in range(0, 10)]
tail_visited = set()


def move_head(index, dir):
    coord_head[index] += dir


def follow(index, dir, to_follow, follower):
    op = operator.gt if dir > 0 else operator.lt
    if op(to_follow[index], follower[index] + dir):
        if to_follow[index ^ 1] != follower[index ^ 1]:
            follower[index ^ 1] = to_follow[index ^ 1]
        follower[index] += dir
    if op(to_follow[index], follower[index]) and abs(to_follow[index ^ 1] - follower[index ^ 1]) > 1:
        if follower[index ^ 1] > to_follow[index ^ 1]:
            follower[index ^ 1] -= 1
        if follower[index ^ 1] < to_follow[index ^ 1]:
            follower[index ^ 1] += 1
        follower[index] += dir


def make_step(dir, steps):
    for _ in range(0, steps):
        current_to_follow = coord_head
        if dir == 'R':
            move_head(0, 1)
            for coord in coord_inter:
                follow(0, 1, current_to_follow, coord)
                current_to_follow = coord
            follow(0, 1, current_to_follow, coord_tail)
        if dir == 'L':
            move_head(0, -1)
            for coord in coord_inter:
                follow(0, -1, current_to_follow, coord)
                current_to_follow = coord
            follow(0, -1, current_to_follow, coord_tail)
        if dir == 'U':
            move_head(1, 1)
            for coord in coord_inter:
                follow(1, 1, current_to_follow, coord)
                current_to_follow = coord
            follow(1, 1, current_to_follow, coord_tail)
        if dir == 'D':
            move_head(1, -1)
            for coord in coord_inter:
                follow(1, -1, current_to_follow, coord)
                current_to_follow = coord
            follow(1, -1, current_to_follow, coord_tail)
        # mark coordinate as visited
        tail_visited.add(str(coord_tail))


# main
movements = []
with open('example9_2.txt', 'r') as f:
    for line in f.readlines():
        dir, steps = line.strip().split(' ')
        movements.append([dir, int(steps)])

for dir, steps in movements:
    make_step(dir, steps)

print(len(tail_visited))
