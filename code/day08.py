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

def part2():
    n = len(coor)
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(coor[i], coor[j])
            edges.append((dist, i, j))
    
    edges.sort()
    
    parent = list(range(n))
    size = [1] * n
    components = n
    
    last_connection = None
    
    for dist, i, j in edges:
        if union(parent, size, i, j):
            components -= 1
            last_connection = (i, j)
            
            if components == 1:
                break
    
    if last_connection:
        i, j = last_connection
        x1 = coor[i][0]
        x2 = coor[j][0]
        result = x1 * x2
        return result
    
    return 0
    
def solve(input_data):
    parse(input_data)
    p1 = part1()
    p2 = part2()
    return f"{p1}\n{p2}"