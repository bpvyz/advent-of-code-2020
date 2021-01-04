def solve(bootcode):
    done = []
    acc = 0
    i = 0

    while True:
        if i == len(bootcode):
            return (0, acc)
        if i in done:
            return (1, acc)

        instr, arg = bootcode[i]
        done.append(i)
        if instr == 'nop':
            i += 1
        elif instr == 'acc':
            acc += int(arg)
            i += 1
        else:
            i += int(arg)


def solve_second(bootcode):
    for i, (instr, arg) in enumerate(bootcode):
        if instr in {'jmp', 'nop'}:
            if instr == 'jmp':
                bootcode[i] = 'nop', arg
            elif instr == 'nop':
                bootcode[i] = 'jmp', arg
            retcode, retval = solve(bootcode)
            if retcode == 0:
                return retval
            else:
                bootcode[i] = instr, arg


def parse(bcode_line):
    instr, arg = bcode_line.split()
    return instr, int(arg)


with open('data.txt', 'r') as f:
    bootcode = list(map(parse, f.read().splitlines()))
    instr, part1 = solve(bootcode)
    print('Solution to part 1 is:', part1)
    print('Solution to part 2 is:', solve_second(bootcode))
