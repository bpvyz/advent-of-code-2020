from copy import deepcopy


def simulate_seats(layout):
    layout = deepcopy(layout)
    rounds = 0
    changes = None
    changes_old = None
    while changes != changes_old or changes is None:
        changes_old = changes
        layout, changes = new_state(layout)
        rounds += 1

    return layout, rounds


def check(layout, r, s):
    occupied = 0
    num_rows = len(layout)
    num_columns = len(layout[0])
    for offset_x in range(-1, 2):
        for offset_y in range(-1, 2):
            x = offset_x + r
            y = offset_y + s
            if offset_x == offset_y == 0 or x >= num_rows or x < 0 or y >= num_columns or y < 0:
                continue
            if layout[x][y] == '#':
                occupied += 1
    return occupied


def new_state(layout):
    new_layout = deepcopy(layout)
    changes = 0
    for r, row in enumerate(layout):
        for s, seat in enumerate(row):
            if seat == 'L' and check(layout, r, s) == 0:
                new_layout[r][s] = '#'
                changes += 1
            elif seat == '#' and check(layout, r, s) >= 4:
                new_layout[r][s] = 'L'
                changes += 1
    return new_layout, changes


def get_num_tiles(layout, tile):
    num = 0
    for row in layout:
        for seat in row:
            if seat == tile:
                num += 1
    return num


with open('data.txt', 'r') as f:
    layout = list(list(line) for line in f.read().splitlines())
    print(layout)
    new_layout, rounds = simulate_seats(layout)
    print(f"Part 1: Rounds: {rounds:<5} Num Occupied Seats: {get_num_tiles(new_layout, '#')}")
