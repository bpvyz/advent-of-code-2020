from collections import defaultdict

def solve(jolts):

    diffs = defaultdict(int)
    counts = defaultdict(int, {0: 1})

    for i, k in zip(jolts, jolts[1:]):
        diffs[k-i] += 1
        counts[k] = counts[k - 3] + counts[k - 2] + counts[k - 1]

    print('Solution to part 1 is:', diffs[1] * diffs[3])
    print('Solution to part 2 is:', counts[jolts[-1]])

with open('data.txt', 'r') as f:
    jolts = [0] + sorted(map(int, f.read().splitlines()))
    jolts.append(jolts[-1] + 3)
    solve(jolts)

