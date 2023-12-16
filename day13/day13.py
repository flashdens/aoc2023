def part1(input_file):
    blocks = [block.split('\n') for block in input_file.read().strip().split('\n\n')]
    values = [[list(line) for line in block] for block in blocks]
    total_sum = 0

    for matrix in values:
        found = False
        for i in range(0, len(matrix) - 1):
            if found:
                break
            if matrix[i] == matrix[i + 1]:
                found_val = i
                for j in range(0, len(matrix)):
                    left = i - j
                    right = i + 1 + j

                    if left < 0 or right >= len(matrix):
                        total_sum += (found_val + 1) * 100
                        found = True
                        break

                    if matrix[left] != matrix[right]:
                        break

                else:
                    total_sum += (found_val + 1) * 100
                    found = True
                    break

        if found:
            continue

        matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]  # transposition

        for i in range(0, len(matrix) - 1):
            if found:
                break
            if matrix[i] == matrix[i + 1]:
                found_val = i
                for j in range(0, len(matrix)):
                    left = i - j
                    right = i + 1 + j

                    if left < 0 or right >= len(matrix):
                        total_sum += found_val + 1
                        found = True
                        break

                    if matrix[left] != matrix[right]:
                        break

                else:
                    total_sum += found_val + 1
                    break

    return total_sum


def part2(input_file):
    blocks = [block.split('\n') for block in input_file.read().strip().split('\n\n')]
    values = [[list(line) for line in block] for block in blocks]
    total_sum = 0

    for matrix in values:
        print(total_sum)
        found = False
        can_flip = True
        flipped = 0
        for i in range(0, len(matrix) - 1):
            if found:
                break

            diffs = [(index, item) for index, item in enumerate(matrix[i + 1]) if item != matrix[i][index]]

            if len(diffs) == 1:
                char = diffs[0][1]
                idx = diffs[0][0]
                flipped = i, idx, matrix[i][idx]
                matrix[i][idx] = char
                can_flip = False

            if matrix[i] == matrix[i + 1]:
                found_val = i
                for j in range(0, len(matrix)):
                    left = i - j
                    right = i + 1 + j

                    if left < 0 or right >= len(matrix):
                        if can_flip:
                            break
                        total_sum += (found_val + 1) * 100
                        found = True
                        break

                    diffs = [(index, item) for index, item in enumerate(matrix[right]) if item != matrix[left][index]]

                    if len(diffs) == 1 and can_flip:
                        char = diffs[0][1]
                        idx = diffs[0][0]
                        matrix[left][idx] = char
                        can_flip = False

                    if matrix[left] != matrix[right]:
                        # revert!
                        if flipped:
                            matrix[flipped[0]][flipped[1]] = flipped[2]
                        can_flip = True
                        break

                else:
                    if can_flip:
                        break
                    flipped = 0
                    total_sum += (found_val + 1) * 100
                    found = True
                    break

        if found:
            continue

        matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]  # transposition

        can_flip = True
        for i in range(0, len(matrix) - 1):

            if found:
                break

            diffs = [(index, item) for index, item in enumerate(matrix[i + 1]) if item != matrix[i][index]]

            if len(diffs) == 1:
                char = diffs[0][1]
                idx = diffs[0][0]
                flipped = i, idx, matrix[i][idx]
                matrix[i][idx] = char
                can_flip = False

            if matrix[i] == matrix[i + 1]:
                found_val = i
                for j in range(0, len(matrix)):
                    left = i - j
                    right = i + 1 + j

                    if left < 0 or right >= len(matrix):
                        if can_flip:
                            break
                        total_sum += found_val + 1
                        found = True
                        break

                    diffs = [(index, item) for index, item in enumerate(matrix[right]) if item != matrix[left][index]]

                    if len(diffs) == 1 and can_flip:
                        char = diffs[0][1]
                        idx = diffs[0][0]
                        flipped = left, idx, matrix[left][idx]
                        matrix[left][idx] = char
                        can_flip = False

                    if matrix[left] != matrix[right]:
                        if flipped:
                            matrix[flipped[0]][flipped[1]] = flipped[2]
                        can_flip = True
                        break

                else:
                    if can_flip:
                        continue
                    total_sum += found_val + 1
                    break
    print(total_sum)
    return total_sum


input_file = open("day13in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
