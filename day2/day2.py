import re
from functools import reduce
from operator import mul

def part1(input_file):
    possible = 0
    input_file = input_file.read().strip().split('\n')

    for line in input_file:
        line = re.split(' ', line)
        line = [line[1][:-1]] + [(line[i], line[i + 1]) for i in range(2, len(line), 2)]

        for tuple in line:

            if type(tuple) is str:
                continue
            count = int(tuple[0])
            color = tuple[1]

            if count > 14:
                break
            elif count > 12 and re.match(r'red*', color):
                break
            elif count > 13 and re.match(r'green*', color):
                break

        else:
            possible += int(line[0])

    return possible


def part2(input_file):
    total = 0
    input_file = input_file.read().strip().split('\n')

    for line in input_file:
        max_values = {}
        line = re.split(' ', line)
        line = [line[1][:-1]] + [(line[i], line[i + 1]) for i in range(2, len(line), 2)]

        for tuple in line:
            if type(tuple) is str:
                continue
            count = int(tuple[0])
            color = tuple[1].replace(",", "").replace(";", "")

            if color not in max_values or count > max_values[color]:
                max_values[color] = count

        local_max = reduce(mul, max_values.values(), 1)
        total += local_max

    return total


input_file = open("day2in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
