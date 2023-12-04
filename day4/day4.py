import re
from math import pow


def part1(input_file):
    total_sum = 0
    input_file = [
        re.sub(r'^.*?:', '', record).split('|') + [0]
        for record in input_file.read().strip().split('\n')
    ]

    for line in input_file:
        winning_numbers = line[0].strip().split()
        my_numbers = line[1].strip().split()

        total_sum += int(
            pow(2,
                len([num1 for num1 in winning_numbers if num1 in my_numbers]) - 1))

    return total_sum


def part2(input_file):
    total_sum = 0
    input_file = [
        re.sub(r'^.*?:', '', record).split('|') + [0]
        for record in input_file.read().strip().split('\n')
    ]

    for i in range(0, len(input_file)):
        line = input_file[i]
        winning_numbers = line[0].strip().split()
        my_numbers = line[1].strip().split()

        won = len([num1 for num1 in winning_numbers if num1 in my_numbers])

        while line[2] >= 0:
            line[2] -= 1
            total_sum += 1
            for j in range(i + 1, i + won + 1):
                input_file[j][2] += 1

    return total_sum


input_file = open("day4in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
input_file.close()
