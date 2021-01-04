
def part1(a):
    answers = [answer.replace("\n", "") for answer in a]
    value = 0
    for answer in answers:
        value += len(set(answer))
    print("Solution to part 1 is: ", value)


def part2(a):
    value = 0
    answers = [answer.split("\n") for answer in a]
    for answer_group in answers:
        s = set(answer_group[0])
        for answer in answer_group:
            x = s.intersection(set(answer))
            s = x
        value += len(x)
    print("Solution to part 2 is: ", value)


with open('data.txt', 'r') as f:
    answers = f.read().split('\n\n')
    part1(answers)
    part2(answers)
