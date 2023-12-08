import collections

order = [
    'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'
]


# todo fix this sorting function
def sort_by_card_order(item):
    return [order.index(char) for char in item[0]]


class Hands:

    def __init__(self):
        self.highs = []
        self.pairs = []
        self.two_pairs = []
        self.threes = []
        self.fulls = []
        self.fours = []
        self.fives = []


def part1(input_file):
    total_value = 0

    values = [line.split(' ') for line in input_file.read().strip().split('\n')]
    hands = Hands()

    for line in values:
        hand = line[0]
        bet = int(line[1])

        char_occurrences = dict(collections.Counter(hand).items())
        char_occurrences = dict(sorted(char_occurrences.items(), key=lambda x: x[1], reverse=True))

        first_el = list(char_occurrences.keys())[0]

        if char_occurrences[first_el] != 5:
            sec_el = list(char_occurrences.keys())[1]

        match char_occurrences[first_el]:

            case 5:
                hands.fives.append((hand, bet))

            case 4:
                hands.fours.append((hand, bet))

            case 3:
                if char_occurrences[sec_el] == 2:
                    hands.fulls.append((hand, bet))
                else:
                    hands.threes.append((hand, bet))

            case 2:
                if char_occurrences[sec_el] == 2:
                    hands.two_pairs.append((hand, bet))
                else:
                    hands.pairs.append((hand, bet))

            case _:
                hands.highs.append((hand, bet))

    rank = 1
    for field in vars(hands).values():
        if field == []:
            continue

        field = sorted(field, key=sort_by_card_order, reverse=True)

        for foo in field:
            total_value += rank * foo[1]
            rank += 1

    return total_value


def part2(input_file):
    total_value = 0

    values = [line.split(' ') for line in input_file.read().strip().split('\n')]
    hands = Hands()

    for i, line in enumerate(values):
        hand = line[0]
        bet = int(line[1])

        char_occurrences = dict(collections.Counter(hand).items())
        char_occurrences = dict(
            sorted(char_occurrences.items(), key=lambda x: (-x[1], sort_by_card_order(x[0]))))

        first_el = list(char_occurrences.keys())[0]

        if 'J' in char_occurrences:
            if char_occurrences['J'] == 5:
                first_el = 'A'
                char_occurrences['A'] = 0

            if first_el == 'J':
                first_el = list(char_occurrences.keys())[1]

            char_occurrences[first_el] += char_occurrences['J']
            del char_occurrences['J']

        first_el = list(char_occurrences.keys())[0]

        if char_occurrences[first_el] != 5:
            sec_el = list(char_occurrences.keys())[1]

        match char_occurrences[first_el]:

            case 5:
                hands.fives.append((hand, bet))

            case 4:
                hands.fours.append((hand, bet))

            case 3:
                if char_occurrences[sec_el] == 2:
                    hands.fulls.append((hand, bet))
                else:
                    hands.threes.append((hand, bet))

            case 2:
                if char_occurrences[sec_el] == 2:
                    hands.two_pairs.append((hand, bet))
                else:
                    hands.pairs.append((hand, bet))

            case _:
                hands.highs.append((hand, bet))

    rank = 1
    for field in vars(hands).values():
        if field == []:
            continue

        field = sorted(field, key=sort_by_card_order)

        for foo in field:
            total_value += rank * foo[1]
            rank += 1

    return total_value


input_file = open("day7in.txt", "r")
print("Part 1:", part1(input_file))
input_file.seek(0)
print("Part 2:", part2(input_file))
