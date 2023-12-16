next_v = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

slash_dirs = {
    'R': 'U',
    'U': 'R',
    'L': 'D',
    'D': 'L',
}

backslash_dirs = {
    'L': 'U',
    'U': 'L',
    'R': 'D',
    'D': 'R'
}


def start_gen(values):
    for i in range(len(values)):
        yield (i, 0), 'R', []
    for i in range(len(values)):
        yield (0, i), 'D', []
    for i in range(len(values)):
        yield (len(values) - 1, i), 'U', []
    for i in range(len(values)):
        yield (i, len(values) - 1), 'L', []


def part1(input_file):
    values = input_file.read().strip().split('\n')

    q = [((0, 0), 'R', [])]
    visited = []

    while len(q) > 0:
        curr_v = q.pop(0)
        v_coords = curr_v[0]
        a = v_coords[0]
        b = v_coords[1]

        v_dir = curr_v[1]
        v_visited_mirrors = curr_v[2]

        if a >= len(values) or a < 0 or b >= len(values[0]) or b < 0:
            continue

        if v_coords not in visited:
            visited.append(v_coords)

        if values[a][b] == '-' and (v_dir == 'U' or v_dir == 'D'):
            q.append(((a, b - 1), 'L', v_visited_mirrors))
            q.append(((a, b + 1), 'R', v_visited_mirrors))

        elif values[a][b] == '|' and (v_dir == 'L' or v_dir == 'R'):
            q.append(((a - 1, b), 'U', v_visited_mirrors))
            q.append(((a + 1, b), 'D', v_visited_mirrors))

        else:
            if values[a][b] == "\\":
                if [(a, b) for t in v_visited_mirrors if (a, b) == t[0] and v_dir == t[1]]:
                    continue
                else:
                    v_visited_mirrors.append(((a, b), v_dir))
                    v_dir = backslash_dirs[v_dir]

            elif values[a][b] == '/':
                if [(a, b) for t in v_visited_mirrors if (a, b) == t[0] and v_dir == t[1]]:
                    continue
                else:
                    v_visited_mirrors.append(((a, b), v_dir))
                    v_dir = slash_dirs[v_dir]

            x, y = tuple(a + b for a, b in zip(next_v[v_dir], (v_coords[0], v_coords[1])))

            if x > len(values) or x < 0 or y > len(values[0]) or y < 0:
                continue

            q.append(((x, y), v_dir, v_visited_mirrors))

    return len(visited)


def part2(input_file):
    values = input_file.read().strip().split('\n')
    best_score = 0
    gen = start_gen(values)

    while True:
        try:
            q = [next(gen)]
        except StopIteration:
            break

        visited = []

        while len(q) > 0:
            curr_v = q.pop(0)
            v_coords = curr_v[0]
            a = v_coords[0]
            b = v_coords[1]

            v_dir = curr_v[1]
            v_visited_mirrors = curr_v[2]

            if a >= len(values) or a < 0 or b >= len(values[0]) or b < 0:
                continue

            if v_coords not in visited:
                visited.append(v_coords)

            if values[a][b] == '-' and (v_dir == 'U' or v_dir == 'D'):
                q.append(((a, b - 1), 'L', v_visited_mirrors))
                q.append(((a, b + 1), 'R', v_visited_mirrors))

            elif values[a][b] == '|' and (v_dir == 'L' or v_dir == 'R'):
                q.append(((a - 1, b), 'U', v_visited_mirrors))
                q.append(((a + 1, b), 'D', v_visited_mirrors))

            else:
                if values[a][b] == "\\":
                    if [(a, b) for t in v_visited_mirrors if (a, b) == t[0] and v_dir == t[1]]:
                        continue
                    else:
                        v_visited_mirrors.append(((a, b), v_dir))
                        v_dir = backslash_dirs[v_dir]

                elif values[a][b] == '/':
                    if [(a, b) for t in v_visited_mirrors if (a, b) == t[0] and v_dir == t[1]]:
                        continue
                    else:
                        v_visited_mirrors.append(((a, b), v_dir))
                        v_dir = slash_dirs[v_dir]

                x, y = tuple(a + b for a, b in zip(next_v[v_dir], (v_coords[0], v_coords[1])))

                if x > len(values) or x < 0 or y > len(values[0]) or y < 0:
                    continue

                q.append(((x, y), v_dir, v_visited_mirrors))

        if len(visited) > best_score:
            best_score = len(visited)

    return best_score


input_file = open("day16in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
