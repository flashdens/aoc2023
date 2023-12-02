import regex as re


def part1(input):
    input = input.read().strip().split('\n')
    sum = 0

    for line in input:
        temp = ""
        temp += re.search(r'\d', line).group()
        temp += re.search(r'\d', line[::-1]).group()
        sum += int(temp)

    return sum


def part2(input):
    num_dict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }

    input = input.read().strip().split('\n')
    sum = 0

    for line in input:

        if line[0].isnumeric() and line[len(line) - 1].isnumeric():
            sum += int(line[0] + line[len(line) - 1])

        else:
            pattern = r'one|two|three|four|five|six|seven|eight|nine|\d'
            temp = ""
            found = re.findall(pattern, line, overlapped=True)
            items = [found[0], found[len(found) - 1]]

            for item in items:
                if item.isnumeric():
                    temp += item
                else:
                    temp += num_dict[item]

            sum += int(temp)

    return sum


input = open("day1in.txt")
#print("Part 1:", part1(input))
input.seek(0)
print("Part 2:", part2(input))
input.close()
