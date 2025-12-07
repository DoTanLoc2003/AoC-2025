diagram = []

def parse(input_data):
    global diagram
    for line in input_data.strip().splitlines():
        line = line.strip()
        diagram.append(list(line))
    
def part1():
    result = 0
    temp_diagram = [row[:] for row in diagram]
    rows = len(temp_diagram)
    cols = len(temp_diagram[0])
    p_s = cols // 2
    temp_diagram[1][p_s] = '|'
    
    for i in range(2, rows, 2):
        for j in range(cols):
            if i-1 >= 0 and temp_diagram[i-1][j] == '|':
                if temp_diagram[i][j] == '^':
                    result += 1
                    if j > 0:
                        temp_diagram[i][j-1] = '|'
                        if i+1 < rows:
                            temp_diagram[i+1][j-1] = '|'
                    
                    if j < cols - 1:
                        temp_diagram[i][j+1] = '|'
                        if i+1 < rows:
                            temp_diagram[i+1][j+1] = '|'
                else:
                    temp_diagram[i][j] = '|'
                    if i+1 < rows:
                        temp_diagram[i+1][j] = '|'
    
    return result

def part2():
    rows = len(diagram)
    cols = len(diagram[0])
    start_col = cols // 2
    
    nums = [[0] * cols for _ in range(rows + 1)]
    for col in range(cols):
        nums[rows][col] = 1
    
    for row in range(rows - 1, -1, -1):
        for col in range(cols):
            item = diagram[row][col]
            if item == 'S' or item == '|' or item == '.':
                if row + 1 < rows:
                    nums[row][col] += nums[row + 1][col]
                else:
                    nums[row][col] = 1
            elif item == '^':
                left = nums[row + 1][col - 1] if col - 1 >= 0 else 0
                right = nums[row + 1][col + 1] if col + 1 < cols else 0
                nums[row][col] = left + right
    
    return nums[0][start_col]

def solve(input_data):
    parse(input_data)
    p1 = part1()
    p2 = part2()
    return f"{p1}\n{p2}"

    