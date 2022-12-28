
rocks = []

with open('input14.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        edges = line.split(' -> ')
        rock = []
        for edge in edges:
            x, y = edge.split(',')
            rock.append((int(x), int(y)))
        rocks.append(rock)

x_coords = [x[0] for rock in rocks for x in rock]
y_coords = [x[1] for rock in rocks for x in rock]

max_x, min_x = max(x_coords)+1, min(x_coords)
max_y, min_y = max(y_coords)+1, min(y_coords)

grid_world = [['.'] * (max_x-min_x) for _ in range(max_y)]

# draw rocks
for rock_edges in rocks:
    for i, edge in enumerate(rock_edges):
        x, y = edge[0] - min_x, edge[1]
        grid_world[y][x] = '#'
        if i + 1 < len(rock_edges):
            until = rock_edges[i+1][0] - min_x
            r = range(x, until) if x < until else range(until, x)
            for j in r:
                grid_world[y][j] = '#'
        if i + 1 < len(rock_edges):
            until = rock_edges[i+1][1]
            r = range(y, until) if y < until else range(until, y)
            for j in r:
                grid_world[j][x] = '#'
grid_world[0][500-min_x] = '+'


def simulate_sand_corn(grid_world, sand_pos):
    if sand_pos[0]+1 >= len(grid_world) or sand_pos[1]+1 >= len(grid_world[0]) or sand_pos[1]-1 < 0:
        return False
    new_sand_pos = sand_pos[0] + 1, sand_pos[1]
    if grid_world[new_sand_pos[0]][new_sand_pos[1]] != '.':
        if grid_world[new_sand_pos[0]][new_sand_pos[1]-1] == '.':
            new_sand_pos = sand_pos[0]+1, sand_pos[1]-1
        elif grid_world[new_sand_pos[0]][new_sand_pos[1]+1] == '.':
            new_sand_pos = sand_pos[0]+1, sand_pos[1]+1
        else:
            grid_world[sand_pos[0]][sand_pos[1]] = 'o'
            return True
    return simulate_sand_corn(grid_world, new_sand_pos)


# simulate sand
sand_count = 0
sand_pos = 0, 500-min_x
is_in_rest = True
while is_in_rest:
    sand_pos = 0, 500-min_x
    is_in_rest = simulate_sand_corn(grid_world, sand_pos)
    sand_count = sand_count + 1 if is_in_rest else sand_count


# print
for row in grid_world:
    print(row)
print()
print('units of sand:', sand_count)
