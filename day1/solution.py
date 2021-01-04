
# part 1

def part1(lines):
    for line1 in lines:
        for line2 in lines - {line1}:
            if line1 + line2 == 2020:
                print("Solution to part 1 is: ", line1*line2)
                break

def part2(lines):
    for line1 in lines:
        for line2 in lines:
            delta = 2020 - line1 - line2
            if delta in lines:
                print("Solution to part 2 is: ", delta*line1*line2)
                break
with open('data.txt', 'r') as f:
    lines = set([int(line) for line in f.read().split("\n")])
    part1(lines)
    part2(lines)
