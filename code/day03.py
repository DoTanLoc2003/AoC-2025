lines = []

def parse(input_data):
    global lines
    
    for line in input_data.strip().splitlines():
        l = line.strip()
        lines.append(l)

def part1():
    result = 0
    for line in lines:
        max1 = 0
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                num = line[i] + line[j]
                if int(num) > max1:
                    max1 = int(num)
        
        result += max1
    return result
    
def part2():
    result = 0
    for line in lines:
        n = len(line)
        num = []
        pop_num = n - 12
        for digit in line:
                while num and pop_num > 0 and num[-1] < digit:
                    num.pop()
                    pop_num -= 1
                num.append(digit)
        num = ''.join(num[:12])
        result += int(num)
    return result

def solve(input_data):
    parse(input_data)
    return f"{part1()}\n{part2()}"
