
def visible_left(i, j, grid, score_grid):
    current = grid[i][j]
    distance = 1
    for m in reversed(range(0, j)):
        running = grid[i][m]
        if running >= current:
            score_grid[i][j] *= distance
            return False
        distance += 1
    score_grid[i][j] *= distance-1
    return True


def visible_right(i, j, grid, score_grid):
    current = grid[i][j]
    distance = 1
    for m in range(j+1, len(grid[0])):
        running = grid[i][m]
        if running >= current:
            score_grid[i][j] *= distance
            return False
        distance += 1
    score_grid[i][j] *= distance-1
    return True


def visible_top(i, j, grid, score_grid):
    current = grid[i][j]
    distance = 1
    for m in reversed(range(0, i)):
        running = grid[m][j]
        if running >= current:
            score_grid[i][j] *= distance
            return False
        distance += 1
    score_grid[i][j] *= distance-1
    return True


def visible_bottom(i, j, grid, score_grid):
    distance = 1
    current = grid[i][j]
    for m in range(i+1, len(grid)):
        running = grid[m][j]
        if running >= current:
            score_grid[i][j] *= distance
            return False
        distance += 1
    score_grid[i][j] *= distance-1
    return True


def is_visible(i, j, grid, score_grid):
    if i == 0 or j == 0 or i == len(grid[0]) - 1 or len(grid) - 1 == j:
        return True

    left = visible_left(i, j, grid, score_grid)
    right = visible_right(i, j, grid, score_grid)
    top = visible_top(i, j, grid, score_grid)
    bottom = visible_bottom(i, j, grid, score_grid)

    return left or right or top or bottom


def get_visibility_grid(grid):
    vis_grid = [row.copy() for row in grid]
    score_grid = [[1 for _ in row] for row in grid]
    for i, row in enumerate(vis_grid):
        for j, col in enumerate(row):
            if is_visible(i, j, grid, score_grid):
                vis_grid[i][j] = 'v'
    return vis_grid, score_grid


with open('input8.txt', 'r') as f:
    grid = []
    for line in f.readlines():
        line = line.strip()
        grid.append([int(t) for t in line])

    vis_grid, score_grid = get_visibility_grid(grid)

    # step 1
    count_vis = len([tree for row in vis_grid for tree in row if tree == 'v'])
    print(count_vis)

    # step 2
    count_score = max([tree for row in score_grid for tree in row])
    print(count_score)
