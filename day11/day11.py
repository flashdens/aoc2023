def part1(input_file):
    total_sum = 0
    values = [[el for el in line] for line in input_file.read().strip().split('\n')]
    hashes = []
    ex_rows = []
    ex_cols = []

    for i in range(len(values)):
        if not any(c not in '.' for c in values[i]):
            ex_rows.append(i)

    values = [[row[i] for row in values] for i in range(len(values[0]))]  # transposition

    for i in range(len(values)):
        if not any(c not in '.' for c in values[i]):
            ex_cols.append(i)

    values = [[row[i] for row in values] for i in range(len(values[0]))]  # transposition
    for i in range(len(values)):
        for j in range(len(values[0])):
            if values[i][j] == '#':
                hashes.append((i + 1 * len([x for x in ex_rows if i > x])
                               , j + 1 * len([y for y in ex_cols if j > y])))

    for i in range(len(hashes)):
        for j in range(i, len(hashes)):
            total_sum += max(hashes[i][0], hashes[j][0]) - min(hashes[i][0], hashes[j][0]) + max(hashes[i][1],
                                                                                                 hashes[j][1]) - min(
                hashes[i][1], hashes[j][1])

    return total_sum


def part2(input_file):
    total_sum = 0
    values = [[el for el in line] for line in input_file.read().strip().split('\n')]
    hashes = []
    ex_rows = []
    ex_cols = []

    for i in range(len(values)):
        if not any(c not in '.' for c in values[i]):
            ex_rows.append(i)

    values = [[row[i] for row in values] for i in range(len(values[0]))]  # transposition

    for i in range(len(values)):
        if not any(c not in '.' for c in values[i]):
            ex_cols.append(i)

    values = [[row[i] for row in values] for i in range(len(values[0]))]  # transposition
    for i in range(len(values)):
        for j in range(len(values[0])):
            if values[i][j] == '#':
                hashes.append((i + 999999 * len([x for x in ex_rows if i > x])
                               , j + 999999 * len([y for y in ex_cols if j > y])))

    for i in range(len(hashes)):
        for j in range(i, len(hashes)):
            total_sum += max(hashes[i][0], hashes[j][0]) - min(hashes[i][0], hashes[j][0]) + max(hashes[i][1],
                                                                                                 hashes[j][1]) - min(
                hashes[i][1], hashes[j][1])

    return total_sum


input_file = open("day11in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
