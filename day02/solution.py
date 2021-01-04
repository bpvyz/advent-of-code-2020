def part1(entries):
    count = 0
    for entry in entries:
        splitted = entry.split()
        ranges, char, passw = [int(x) for x in splitted[0].split('-')], splitted[1][0], splitted[2]
        if passw.count(char) in range(ranges[0], ranges[1]+1):
            count += 1
    print("Solution to part 1 is: ", count)

def part2(entries):
    count = 0
    for entry in entries:
        splitted = entry.split()
        pos, char, passw = [int(x)-1 for x in splitted[0].split('-')], splitted[1][0], splitted[2]
        try:
            if passw[pos[0]] == char and passw[pos[1]] != char or passw[pos[1]] == char and passw[pos[0]] != char:
                print(passw, char, pos)
                count += 1
        except IndexError:
            pass
    print("Solution to part 2 is: ", count)

with open('data.txt', 'r') as f:
    passwords = f.read().splitlines()
    part1(passwords)
    part2(passwords)
