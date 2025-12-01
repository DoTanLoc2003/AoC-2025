dials = []

def parse(input_data):
    global dials
    dials = []

    for line in input_data.strip().splitlines():
        s = line.strip()
        LR = -1 if s[0] == 'L' else 1
        rotation = int(s[1:])
        dials.append(LR * rotation)


def part1():
    point = 50
    result = 0
    for dial in dials:
        point = (point + dial) % 100
        if point % 100 == 0:
            result += 1
            point = 0
    return result


def part2():
    point = 50
    result = 0
    for dial in dials:
        new_point = point + dial
        if dial < 0:
            result += (point - 1) // 100 - (new_point - 1) // 100
        else:
            result += new_point // 100 - point // 100
        point = new_point % 100
    return result


def solve(input_data):
    parse(input_data)
    return f"{part1()}\n{part2()}"
