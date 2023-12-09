def part1(input_file):
    values = [[int(el) for el in line.split()] for line in input_file.read().strip().split('\n')]
    total_sum = 0
    for line in values:
        local_values = [line]
        diffs = []
        while diffs == [] or not all(el == 0 for el in diffs):
            diffs = [int(line[i + 1]) - int(line[i]) for i in range(0, len(line) - 1)]
            local_values.append(diffs)
            line = diffs

        for i in range(len(local_values) - 1, 0, -1):
            local_values[i - 1].append(local_values[i][-1] + local_values[i - 1][-1])

        total_sum += local_values[0][-1]

    return total_sum


def part2(input_file):
    values = [[int(el) for el in line.split()] for line in input_file.read().strip().split('\n')]
    total_sum = 0
    for line in values:
        local_values = [line]
        diffs = []
        while diffs == [] or not all(el == 0 for el in diffs):
            diffs = [int(line[i + 1]) - int(line[i]) for i in range(0, len(line) - 1)]
            local_values.append(diffs)
            line = diffs

        for i in range(len(local_values) - 1, 0, -1):
            local_values[i - 1].insert(0, local_values[i - 1][0] - local_values[i][0])

        total_sum += local_values[0][0]

    return total_sum


input_file = open("day9in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
