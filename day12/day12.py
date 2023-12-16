score = 0


def hello(line, groups, i=0):
    if i == len(line):
        curr = 0
        seen = []
        for c in line:
            if c == '.':
                if curr > 0:
                    seen.append(curr)
                curr = 0
            elif c == '#':
                curr += 1

        if curr > 0:
            seen.append(curr)

        return 1 if seen == groups else 0

    elif line[i] == '?':
        return hello(line[:i] + '#' + line[i + 1:], groups, i + 1) + hello(line[:i] + '.' + line[i + 1:], groups, i + 1)
    else:
        return hello(line, groups, i + 1)


def part1(input_file):
    values = [[el for el in line.split()] for line in input_file.read().strip().split('\n')]
    total_sum = 0
    for line in values:
        foo = line[0]
        groups = [int(el) for el in line[1].split(',')]
        total_sum += hello(foo, groups)

    return total_sum


def part2(input_file):
    pass


input_file = open("day12in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
