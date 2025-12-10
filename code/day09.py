import math
coor = []

def parse(input_data):
    global coor
    coor = []
    for line in input_data.splitlines():
        line = line.strip().split(',')
        coor.append(list(map(int, line)))

def area(a, b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1]) + 1)    

def part1():
    coor.sort()
    result = 0
    n = len(coor)
    for i in range(n):
        for j in range(i + 1, n):
            result = max(area(coor[i], coor[j]), result)
    return result

def part2():
    result = 0
    n = len(coor)
    temp = coor[0][0]
    coor.sort(key=lambda x: x[0])
        
    return result
     
def solve(input_data):
    parse(input_data)
    p1 = part1()
    p2 = part2()
    return f"{p1}\n{p2}"