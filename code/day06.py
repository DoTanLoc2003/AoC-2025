def operate(a, b, s):
    if s == '+':
        return a + b
    elif s == '*':
        return a * b
    return 0

def part1(input_data):
    if isinstance(input_data, str):
        lines = input_data.strip().split('\n')
    else:
        lines = [line.rstrip('\n') if isinstance(line, str) else str(line) for line in input_data]
    
    operators = lines[-1].split()
    nums = [list(map(int, line.split())) for line in lines[:-1]]
    
    result = 0
    for j in range(len(nums[0])):
        r = nums[0][j]
        for i in range(1, len(nums)):
            r = operate(r, nums[i][j], operators[j])
        result += r
    
    return result

def part2(input_data):
    if isinstance(input_data, str):
        lines = input_data.split('\n')
    else:
        lines = [line if isinstance(line, str) else str(line) for line in input_data]
    
    lines = [line.rstrip('\n') for line in lines if line.rstrip('\n')]
    operators = lines[-1].split()
    data_lines = lines[:-1]
    
    max_len = max(len(line) for line in data_lines)
    
    separator_cols = [col for col in range(max_len) 
                      if all(col >= len(line) or line[col] == ' ' for line in data_lines)]
    
    col_ranges = []
    start = 0
    for sep in separator_cols:
        col_ranges.append((start, sep))
        start = sep + 1
    col_ranges.append((start, max_len))
    
    total = 0
    for j, (col_start, col_end) in enumerate(col_ranges):
        max_digits = max((len(line[col_start:min(col_end, len(line))].strip()) 
                         for line in data_lines), default=0)
        
        col_result = 0
        for digit_pos in range(max_digits):
            col_num = ''
            for line in data_lines:
                text = line[col_start:min(col_end, len(line))]
                idx = len(text) - 1 - digit_pos
                if idx >= 0 and text[idx] != ' ':
                    col_num += text[idx]
            
            if col_num:
                col_value = int(col_num)
                col_result = col_value if digit_pos == 0 else operate(col_result, col_value, operators[j])
        
        total += col_result
    
    return total

def solve(input_data):
    p1 = part1(input_data)
    p2 = part2(input_data)
    return f"{p1}\n{p2}"