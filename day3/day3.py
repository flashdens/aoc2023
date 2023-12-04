from operator import add

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def part1(input_file):
    total_sum = 0
    values = []
    special_chars_coords = []
    input_file = input_file.read().split()

    for i in range(0, len(input_file)):

        current_line = []
        for j in range(0, len(input_file[i])):
            coord = input_file[i][j]
            current_line.append(coord)
            if coord in ['*', '$', '&', '@', '%', '/', '=', '+', '-', '#']:
                special_chars_coords.append((i + 1, j + 1))

        values.append(['.'] + current_line + ['.'])

    extra_row = ['.' for _ in range(0, len(input_file[0]) + 2)]
    values = [extra_row] + values + [extra_row]

    for coord in special_chars_coords:
        for dir in dirs:
            checked = tuple(map(add, coord, dir))
            x = checked[0]
            y = checked[1]

            if values[x][y].isnumeric():

                build_me = ""
                char_ptr = y

                while values[x][char_ptr].isnumeric():
                    curr_x = values[x][char_ptr]
                    build_me = curr_x + build_me
                    values[x][char_ptr] = '.'
                    char_ptr = char_ptr - 1

                char_ptr = y + 1

                while values[x][char_ptr].isnumeric():
                    curr_x = values[x][char_ptr]
                    build_me = build_me + curr_x
                    values[x][char_ptr] = '.'
                    char_ptr = char_ptr + 1

                total_sum += int(build_me)

    return total_sum


def part2(input_file):
    total_sum = 0
    values = []
    special_chars_coords = []
    input_file = input_file.read().split()

    for i in range(0, len(input_file)):

        current_line = []
        for j in range(0, len(input_file[i])):
            coord = input_file[i][j]
            current_line.append(coord)
            if coord in ['*', '$', '&', '@', '%', '/', '=', '+', '-', '#']:
                special_chars_coords.append((i + 1, j + 1))

        values.append(['.'] + current_line + ['.'])

    extra_row = ['.' for i in range(0, len(input_file[0]) + 2)]
    values = [extra_row] + values + [extra_row]

    for coord in special_chars_coords:
        found = []
        for dir in dirs:
            checked = tuple(map(add, coord, dir))
            x = checked[0]
            y = checked[1]

            if values[x][y].isnumeric():

                build_me = ""
                char_ptr = y

                while values[x][char_ptr].isnumeric():
                    curr_x = values[x][char_ptr]
                    build_me = curr_x + build_me
                    values[x][char_ptr] = '.'
                    char_ptr = char_ptr - 1

                char_ptr = y + 1

                while values[x][char_ptr].isnumeric():
                    curr_x = values[x][char_ptr]
                    build_me = build_me + curr_x
                    values[x][char_ptr] = '.'
                    char_ptr = char_ptr + 1

                found.append(int(build_me))
                if len(found) > 2:
                    break

        if len(found) == 2:
            total_sum += found[0] * found[1]

    return total_sum


input_file = open("day3in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
input_file.close()
