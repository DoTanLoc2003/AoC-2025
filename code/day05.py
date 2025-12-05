pairs = []
items = []

def parse(input_data):
    global pairs, items
    
    pairs = []
    items = []
    change = False
    
    for line in input_data.strip().split('\n'):
        line = line.strip()
        
        if not line:
            change = True
        else:
            if not change:
                item = line.split('-')
                pairs.append((int(item[0]), int(item[1])))
            else:
                items.append(int(line))

def merge_ranges():
    global pairs
    pairs.sort(key = lambda x:x[0])
    
    merge = [pairs[0]]
    
    for c in pairs[1:]:
        last = merge[-1]
        if c[0] <= last[1] +1:
            merge[-1]=(last[0], max(last[1], c[1]))
        else:
            merge.append(c)
    
    pairs = merge

def part1():
    count = 0
    
    for item in items:
        for pair in pairs:
            if pair[0] <= item <= pair[1]:
                count += 1
                break
    return count

def part2():
    total = 0
    for pair in pairs:
        total += pair[1] - pair[0] + 1
    return total

def solve(input_data):
    parse(input_data)
    merge_ranges()
    p1 = part1()
    p2 = part2()
    return f"{p1}\n{p2}"
    