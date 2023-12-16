dirs = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'F': [(0, 1), (1, 0)],
    'S': [(0, -1), (1, 0)],  # yes, i hard coded it based on my input.
    '7': [(0, -1), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    '.': []
}

traversal_dirs = [
    (-1, 0), (0, 1), (1, 0), (0, -1)
]


def part1(input_file):
    values = input_file.readlines()

    start_node = None

    for i in range(len(values)):
        j = values[i].find('S')
        if j != -1:
            start_node = (i, j)
            break

    visited = []
    max_depth = 0
    q = [(start_node, 0)]

    while len(q) > 0:
        curr_v = q.pop(0)
        node = curr_v[0]
        depth = curr_v[1]
        directions = dirs[values[node[0]][node[1]]]
        if curr_v[0] not in visited:
            visited.append(curr_v[0])

        for direction in directions:
            x, y = tuple(a + b for a, b in zip(direction, (node[0], node[1])))

            if x > len(values) or x < 0 or y > len(values[0]) or y < 0:
                continue

            neighbour = (x, y)
            if neighbour not in visited:
                q.append(((x, y), depth + 1))
                if depth + 1 > max_depth:
                    max_depth = depth

    return max_depth + 1


def part2(input_file):
    values = input_file.readlines()

    start_node = None

    for i in range(len(values)):
        j = values[i].find('S')
        if j != -1:
            start_node = (i, j)
            break

    visited = []
    q = [(start_node, [])]

    while len(q) > 0:
        curr_v = q.pop(0)
        node = curr_v[0]
        local_visited = curr_v[1]
        directions = dirs[values[node[0]][node[1]]]
        if curr_v[0] not in visited:
            visited.append(curr_v[0])
            local_visited.append(curr_v[0])
        for direction in directions:
            x, y = tuple(a + b for a, b in zip(direction, (node[0], node[1])))

            if x > len(values) or x < 0 or y > len(values[0]) or y < 0:
                continue

            neighbour = (x, y)
            if neighbour not in visited:
                q.append(((x, y), local_visited))

    q = [(0, 0)]

    while len(q) > 0:
        curr_v = q.pop(0)
        if curr_v not in visited:
            print(curr_v)
            visited.append(curr_v)
        for dir in traversal_dirs:

            x, y = tuple(a + b for a, b in zip(dir, (curr_v[0], curr_v[1])))

            if x >= len(values) or x < 0 or y >= len(values[0]) or y < 0:
                continue

            neighbour = (x, y)
            if neighbour not in visited:
                q.append(neighbour)

    return len(values) * len(values[0]) - len(visited)


input_file = open("day10in.txt", "r")
# print("Part 1:", part1(input_file))
# input_file.seek(0)
print("Part 2:", part2(input_file))
