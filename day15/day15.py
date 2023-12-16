from itertools import takewhile


def get_chars_until(in_string, delims):
    return ''.join(takewhile(lambda char: char not in delims, in_string))


def hash_me(char, local_sum=0):
    local_sum += ord(char)
    local_sum *= 17
    local_sum %= 256
    return local_sum


def part1(input_file):
    values = [el for el in input_file.read().strip().split(',')]
    total_sum = 0
    for value in values:
        local_sum = 0
        for char in value:
            local_sum = hash_me(char, local_sum)
        total_sum += local_sum
    return total_sum


def part2(input_file):
    values = [el for el in input_file.read().strip().split(',')]
    ht = {}
    total_sum = 0
    for value in values:
        key = 0
        idx = get_chars_until(value, ['=', '-'])
        for char in idx:
            key = hash_me(char, key)
        value = value[len(idx):]

        if value[0] == '-':
            for key in ht:
                box_values = ht[key]
                for i in range(len(box_values)):
                    if idx == box_values[i][0]:
                        del box_values[i]
                        break

        else:
            if key not in ht:
                ht[key] = []
            for i in range(len(ht[key])):
                if idx == ht[key][i][0]:
                    ht[key][i][1] = int(value[1])
                    break
            else:
                ht[key].append([idx, int(value[1:])])

    for key in ht:
        for i in range(len(ht[key])):
            total_sum += (key + 1) * (i + 1) * ht[key][i][1]

    return total_sum


input_file = open("day15in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
