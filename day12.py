import networkx as nx
import matplotlib.pyplot as plt

def get_height(grid, i, j):
    if i < 0 or j < 0 or i+1 > len(grid) or j+1 > len(grid[0]):
        return ord('z') + 3
    if grid[i][j] == 'E':
        return ord('z') + 1
    if grid[i][j] == 'S':
        return ord('a')
    return ord(grid[i][j])

def draw_graph(graph, shortest_path):
    pos = {(x,y):(y,-x) for x,y in graph.nodes()}
    for node in graph.nodes:
        if node in shortest_path:
            nx.draw_networkx_nodes(graph, pos=pos, nodelist=[node], node_color='red')
        else:
            nx.draw_networkx_nodes(graph, pos=pos, nodelist=[node], node_color='black')
    nx.draw_networkx_edges(graph, pos=pos)
    nx.draw_networkx_labels(graph, pos=pos)
    plt.show()


grid = []
with open('input12.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        points = [c for c in line]
        grid.append(points)

graph = nx.DiGraph()
source, target = '0,0', '0,0'
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        graph.add_node((i, j))
        if grid[i][j] == 'S':
            source = (i, j)
        if grid[i][j] == 'E':
            target = (i, j)

        height = get_height(grid, i, j)

        if height+1 >= get_height(grid, i+1, j):
            graph.add_edge((i, j), (i+1, j))
        if height+1 >= get_height(grid, i-1, j):
            graph.add_edge((i, j), (i-1, j))
        if height+1 >= get_height(grid, i, j+1):
            graph.add_edge((i, j), (i,j+1))
        if height+1 >= get_height(grid, i, j-1):
            graph.add_edge((i, j), (i,j-1))

# solution to part a is 339

# part 2
start_candidate_path_lens = []
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if grid[i][j] == 'a' or grid[i][j] == 'S':
            try:
                shortest_path_len = nx.shortest_path_length(graph, (i, j), target, method='dijkstra')
                print('shortest path from', (i, j), '->', target, "is of lenght", shortest_path_len)
                start_candidate_path_lens.append(shortest_path_len)
            except:
                print('no path from', (i, j), 'to', target)

print(min(start_candidate_path_lens))

# solution to part b is 332

# somewhere there is a off-by-x error!
