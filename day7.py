
from anytree import Node, PreOrderIter

available_space = 70000000
needed_space = 30000000

def get_recursive_size(parent):
    sum = 0
    for child in parent.children:
        if child.size == 0:
            sum += get_recursive_size(child)
        else:
            sum += child.size
    return sum

def calculate_sizes(parent):
    as_list = [node for node in PreOrderIter(parent)]
    filtered = [item for item in filter(lambda x: x.dir, as_list)]
    for child in filtered:
        if child.dir:
            child.size = get_recursive_size(child)

with open('input7.txt', 'r') as f:
    root = Node('/', size=0, dir=True)
    current_parent = root
    for line in f.readlines()[1:]:
        line = line.strip()
        if line.startswith('$ cd'):
            dir = line.split(' ')[2]
            if dir == '..':
                current_parent = current_parent.parent
            else: 
                new_parent = Node(dir, parent=current_parent, size=0, dir=True)
                current_parent = new_parent
        elif not line.startswith('$'):
            size, filename = line.split(' ')
            if size == 'dir':
                size = 0
            Node(filename, parent=current_parent, size=int(size), dir=False)

    calculate_sizes(root)
    as_list = [node for node in PreOrderIter(root)]
    dirs = [node for node in filter(lambda x: x.dir, as_list)]
    
    # step 1
    sum = sum([item.size for item in filter(lambda x: x.size < 100000, dirs)])
    print(sum)

    # step 2
    unused_space = available_space - root.size
    rm_candidates = [item.size for item in filter(lambda x: x.size + unused_space > needed_space, dirs)]
    print(min(rm_candidates))
