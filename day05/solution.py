def part1(passes):
    ids = []
    for bpass in passes:

        rows = {'floor': 0, 'ceil': 127}
        columns = {'floor': 0, 'ceil': 7}

        for letter in bpass:

            if letter == 'F':
                rows['ceil'] -= (rows['ceil'] - rows['floor']) // 2 + 1

            elif letter == 'B':
                rows['floor'] += -(-(rows['ceil'] - rows['floor']) // 2)

            if letter == 'R':
                columns['floor'] += -(-(columns['ceil'] - columns['floor']) // 2)

            elif letter == 'L':
                columns['ceil'] -= (columns['ceil'] - columns['floor']) // 2 + 1
        row = rows['floor']
        column = columns['floor']
        ids.append(row * 8 + column)
    print('Solution to part 1 is: ', max(ids))
    return ids


def part2(passes):
    ids = part1(passes)
    for id in ids:
        if (id + 2) in ids and (id + 1) not in ids:
            seat = id + 1
            print('Solution to part 2 is: ', seat)


with open('data.txt', 'r') as f:
    passes = f.read().splitlines()
    part2(passes)
