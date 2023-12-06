import re


def interval_intersection(interval1, interval2):
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # Check if there is a valid intersection
    if start <= end:
        return start, end
    else:
        return None


def _is_overlapping(x1, x2, y1, y2):
    return max(x1, y1) <= min(x2, y2)


def _fully_overlaps(seed, interval):
    return interval[0] <= seed[0] and interval[1] >= seed[1]


def _is_in_interval(val, interval):
    lower = interval[0]
    upper = interval[1]
    return lower <= val <= upper


def _merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        prev_start, prev_end = merged[-1]

        if current_start <= prev_end + 1:
            merged[-1] = [prev_start, max(prev_end, current_end)]
        else:
            merged.append([current_start, current_end])

    return merged


def part1(input_file):
    values = [
        [int(el) for el in re.sub(r'^.*?:', '', line).strip().split() if any(el)]
        for line in input_file.read().split('\n')
    ]

    seeds = values.pop(0)
    values = values[2:]
    wait = False

    local_maps = []

    for line in values:
        if line != []:
            local_maps.append(line)
        elif wait:
            wait = False
            continue
        else:
            intervals = sorted([(_map[1], _map[1] + _map[2] - 1, _map[1] - _map[0]) for _map in local_maps])
            new_vals = []
            for seed in seeds:
                for interval in intervals:
                    if _is_in_interval(seed, interval):
                        foo = seed - interval[2]
                        new_vals.append(foo)
                        break
                else:
                    new_vals.append(seed)

                seeds = new_vals

            local_maps = []
            wait = True

    return min(seeds)


def part2(input_file):
    values = [
        [int(el) for el in re.sub(r'^.*?:', '', line).strip().split() if any(el)]
        for line in input_file.read().split('\n')
    ]
    seeds = values.pop(0)
    seeds = sorted([[seeds[i], seeds[i] + seeds[i + 1] - 1] for i in range(0, len(seeds) - 1, 2)])
    values = values[2:]
    wait = False

    local_maps = []

    for line in values:
        if line != []:
            local_maps.append(line)
        elif wait:
            wait = False
            continue
        else:
            intervals = sorted([(_map[1], _map[1] + _map[2] - 1, _map[1] - _map[0]) for _map in local_maps])
            new_vals = []
            for interval in intervals:
                int_seeds = [seed for seed in seeds if
                             _is_overlapping(seed[0], seed[1], interval[0], interval[1])]
                seeds = [seed for seed in seeds if seed not in int_seeds]

                for seed in int_seeds:
                    intersection = interval_intersection(seed, interval)

                    if intersection:
                        new_vals.append(
                            [intersection[0] - interval[2], intersection[1] - interval[2]])
                        if _fully_overlaps(seed, interval):
                            continue
                        if seed[0] < intersection[0]:  # left
                            seeds.append([seed[0], intersection[0] - 1])
                        if seed[1] > intersection[1]:  # right
                            seeds.append(([intersection[1] + 1, seed[1]]))

                    else:
                        seeds.append(seed)

            seeds = _merge_intervals(seeds + new_vals)
            local_maps = []
            wait = True

    return min(seeds)[0]


input_file = open("day5in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
