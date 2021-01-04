import itertools


def solve(numbers):
    for index, i in enumerate(numbers[25:]):
        summable = False
        for j in range(index - 25, len(numbers) - 1):
            for k in range(j, len(numbers)):
                if numbers[j] + numbers[k] == i:
                    summable = True
                    break
        if not summable:
            return numbers[:index + 25], i


def solve_second(numbers, i, invalid_number):
    s = 0
    num_set = []
    for num in range(i, len(numbers)):
        s += numbers[num]
        num_set.append(numbers[num])

        if s > invalid_number:
            return solve_second(numbers, i + 1, invalid_number)
        elif s == invalid_number:
            return max(num_set) + min(num_set)


with open('data.txt', 'r') as f:
    numbers = list(int(line) for line in f.read().splitlines())
    nums, invalid_number = solve(numbers)
    print('Solution to part 1 is:', invalid_number)
    print('Solution to part 2 is:', solve_second(nums, 0, invalid_number))
