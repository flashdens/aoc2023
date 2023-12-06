import re


def part1(input_file):
    values = [[int(el) for el in re.sub(r'^.*?:', '', line).strip().split() if any(el)] for line in
              input_file.read().split('\n')]
    values = list((zip(values[0], values[1])))

    total_sum = 1
    # i guess binary search would be the fastest, but this one is good enough i think
    for pair in values:

        for i in range(1, pair[0], 1):
            if (pair[0] - i) * i > pair[1]:
                total_sum *= pair[0] - i - i + 1
                break

    return total_sum


def part2(input_file):
    values = [int(re.sub(r'^.*?:', '', line).strip().replace(" ", "")) for line in
              input_file.read().split('\n') if line.strip()]

    total_sum = 1
    # i guess binary search would be the fastest, but this one is good enough i think
    # not good enough for this solution but i'm brain-damaged by day 5 honestly

    for i in range(1, values[0], 1):
        if (values[0] - i) * i > values[1]:
            total_sum *= values[0] - i - i + 1
            break

    return total_sum


input_file = open("day6in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
