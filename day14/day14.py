dirs = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}


def part1(input_file):
    values = [list(line) for line in input_file.read().strip().split('\n')]
    total_sum = 0

    for i in range(len(values) - 1, -1, -1):
        for j in range(i + 1, len(values)):
            for k in range(len(values[i])):
                if values[j][k] == 'O':
                    if values[j - 1][k] == '.':
                        values[j][k], values[j - 1][k] = values[j - 1][k], values[j][k]

    for i in range(len(values)):
        total_sum += values[i].count('O') * (len(values) - i)

    return total_sum


# todo
def part2(input_file):
    values = [list(line) for line in input_file.read().strip().split('\n')]
    total_sum = 0

    for i in range(4):
        print(i)
        for j in range(len(values)):
            for k in range(len(values[0])):
                if values[j][k] == 'O':
                    check_dir = dirs[i % 3]
                    x = j + check_dir[0]
                    y = k + check_dir[1]
                    if not x < 0 and not y < 0 and not x >= len(values) and not y >= len(values[0]) and values[x][
                        y] == '.':
                        values[j][k], values[x][y] = values[x][y], values[j][k]

    for i in range(len(values)):
        total_sum += values[i].count('O') * (len(values) - i)

    return total_sum


input_file = open("day14in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
