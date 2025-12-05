lines = []
rows = 0
columns = 0

def parse(input_data):
    global lines, rows, columns
    lines = []
    rows = 0
    columns = 0
    
    for line in input_data.strip().split('\n'):
        rows += 1
        columns = len(line)
        lines.append(list(line))
    
def count_around(i, j):
    count = 0

    if i == 0:
        if j == 0:
            neighbors = [(0, 1), (1, 0), (1, 1)]
        elif j == columns - 1:
            neighbors = [(0, j-1), (1, j-1), (1, j)]
        else:
            neighbors = [(0, j-1), (0, j+1), (1, j-1), (1, j), (1, j+1)]
    elif i == rows - 1:
        if j == 0:
            neighbors = [(i-1, 0), (i-1, 1), (i, 1)]
        elif j == columns - 1:
            neighbors = [(i-1, j-1), (i-1, j), (i, j-1)]
        else:
            neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1)]
    elif j == 0:
        neighbors = [(i-1, 0), (i-1, 1), (i, 1), (i+1, 0), (i+1, 1)]
    elif j == columns - 1:
        neighbors = [(i-1, j-1), (i-1, j), (i, j-1), (i+1, j-1), (i+1, j)]
    else:
        neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]

    for ni, nj in neighbors:
        if lines[ni][nj] == lines[i][j]:
            count += 1

    return count < 4

def part1():
    result = 0
    for i in range(rows):
        for j in range(columns):
            if lines[i][j] == '@' and count_around(i, j):
                result += 1
    return result

def part2():
    global lines
    result = 0

    while True:
        r = 0
        lines_after_remove = [row[:] for row in lines]
        for i in range(rows):
            for j in range(columns):
                if lines[i][j] == '@' and count_around(i, j):
                    r += 1
                    lines_after_remove[i][j] = '.'
        lines = lines_after_remove
        result += r

        if r == 0:
            break

    return result

def solve(input_data):
    parse(input_data)
    p1 = part1()
    parse(input_data)  # Parse lại để reset lines cho part2
    p2 = part2()
    return f"{p1}\n{p2}"