def part1(timestamp, ids):
    new_timestamp = timestamp
    for id in ids:
        if new_timestamp % id == 0:
            print(id*new_timestamp-timestamp)
            return 0
        else:
            new_timestamp += 1
            print(new_timestamp)
with open('sample.txt', 'r') as f:
    f = f.read().splitlines()
    timestamp, ids = int(f[0]), list(int(i) for i in f[1].replace('x,', '').split(','))
    part1(timestamp, ids)