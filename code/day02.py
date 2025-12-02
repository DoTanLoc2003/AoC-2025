pairs = []

def parse(input_data):
    global pairs
    pairs = []
    
    for pair in input_data.split(','):
        pair = pair.strip()
        
        item = pair.split('-')
        pairs.append((int(item[0]), int(item[1])))
    
def is_sequential_2(num):
    length = len(num)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first = num[:mid]
    last = num[mid:]
    
    return first == last

def is_sequential(num):
    length = len(num)
    
    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0: # divide the str into parts equally
           pattern = num[:pattern_length]
           times = length // pattern_length
           
           if times >= 2 and pattern*times == num:
               return True
    return False

def part1():
    result = 0
    for pair in pairs:
        for i in range(pair[0], pair[1] + 1):
            if is_sequential_2(str(i)):
                result += i
    return result

def part2():
    result = 0
    for pair in pairs:
        for i in range(pair[0], pair[1] + 1):
            if is_sequential(str(i)):
                result += i
    return result

def solve(input_data):
    parse(input_data)
    return f"{part1()}\n{part2()}"
    # return f"{pairs}"