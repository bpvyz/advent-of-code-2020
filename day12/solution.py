def move(instruction, value, x, y):
    if instruction == 'E' or instruction == 0:
        x += value
    elif instruction == 'W' or instruction == 180:
        x -= value
    elif instruction == 'N' or instruction == 270:
        y += value
    elif instruction == 'S' or instruction == 90:
        y -= value
    return x, y


def transform(old_direction, direction, wp_x, wp_y):
    change = (direction - old_direction) % 360
    if change == 90:
        wp_x, wp_y = wp_y, -wp_x
    elif change == 180:
        wp_x, wp_y = -wp_x, -wp_y
    elif change == 270:
        wp_x, wp_y = -wp_y, wp_x

    return wp_x, wp_y


def rotate(instruction, direction, value, wp_x=None, wp_y=None):
    if instruction == 'L':
        direction -= value
        direction %= 360
        if wp_x and wp_y:
            wp_x, wp_y = transform(direction + value, direction, wp_x, wp_y)
            return direction, wp_x, wp_y
    elif instruction == 'R':
        direction += value
        direction %= 360
        if wp_x is not None and wp_y is not None:
            wp_x, wp_y = transform(direction - value, direction, wp_x, wp_y)
            return direction, wp_x, wp_y
    return direction


def get_manhattan(s_x, s_y):
    return abs(s_y) + abs(s_x)


directions = ['N', 'W', 'S', 'E']
rotations = ['L', 'R']


def part1(instructions):
    direction = 0
    s_y = 0
    s_x = 0
    for line in instructions:
        instruction, value = line[0], int(line[1:])

        if instruction in directions:
            s_x, s_y = move(instruction, value, s_x, s_y)

        elif instruction in rotations:
            direction = rotate(instruction, direction, value)

        else:
            s_x, s_y = move(direction, value, s_x, s_y)

    print('Solution to part 1 is:', get_manhattan(s_x, s_y))


def part2(instructions):
    direction = 0
    s_y = 0
    s_x = 0
    wp_y = 1
    wp_x = 10

    for line in instructions:
        instruction, value = line[0], int(line[1:])

        if instruction in directions:
            wp_x, wp_y = move(instruction, value, wp_x, wp_y)

        elif instruction in rotations:
            direction, wp_x, wp_y = rotate(instruction, direction, value, wp_x, wp_y)

        else:
            s_x += value * wp_x
            s_y += value * wp_y
    print('Solution to part 2 is:', get_manhattan(s_x, s_y))


with open('data.txt', 'r') as f:
    lines = f.read().splitlines()
    part1(lines)
    part2(lines)
