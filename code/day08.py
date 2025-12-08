import math

coor = []

def parse(input_data):
    global coor
    coor = []
    for line in input_data.splitlines():
        line = line.strip().split(',')
        coor.append(list(map(int, line)))

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def find(parent, x):

    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, x, y):

    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x == root_y:
        return False
    
    if size[root_x] < size[root_y]:
        root_x, root_y = root_y, root_x
    
    parent[root_y] = root_x
    size[root_x] += size[root_y]
    return True

def part1():
    n = len(coor)
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(coor[i], coor[j])
            edges.append((dist, i, j))
    
    edges.sort()
    
    parent = list(range(n))
    size = [1] * n
    
    for connection_num in range(1000): # if tests input -> 28
        dist, i, j = edges[connection_num]
        union(parent, size, i, j)
    
    component_sizes = {}
    for i in range(n):
        root = find(parent, i)
        component_sizes[root] = component_sizes.get(root, 0) + 1
    
    sizes = sorted(component_sizes.values(), reverse=True)
    
    result = sizes[0] * sizes[1] * sizes[2]
    
    return result

def solve(input_data):
    parse(input_data)
    p1 = part1()
    return f"{p1}"