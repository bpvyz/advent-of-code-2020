import re

keys = ['byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid']


def part1(passports):
    count = 0
    for item in passports:
        passport = dict(re.findall(r'(?=\S|^)(.+?):(\S+)', item.rstrip()))
        if all(key in passport for key in keys):
            count += 1
    print('Solution to part 1 is: ', count)


def part2(passports):
    count = 0
    def is_valid(passport):
        if ((1920 <= int(passport['byr']) <= 2002) and
                (2010 <= int(passport['iyr']) <= 2020) and
                (2020 <= int(passport['eyr']) <= 2030) and
                (((passport['hgt'][-2:] == 'cm') and (150 <= int(passport['hgt'][:-2]) <= 193)) or
                 ((passport['hgt'][-2:] == 'in') and (59 <= int(passport['hgt'][:-2]) <= 76))) and
                (passport['hcl'][0] == '#' and all([x.isalnum() for x in passport['hcl'][1:]])) and
                (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
                (len(passport['pid']) == 9 and all([x.isdigit() for x in passport['pid']]))):
            return True

    for item in passports:
        passport = dict(re.findall(r'(?=\S|^)(.+?):(\S+)', item.rstrip()))
        if all(key in passport for key in keys):
            if is_valid(passport):
                count+=1
    print('Solution to part 2 is: ', count)


with open('data.txt', 'r') as f:
    passports = f.read().split('\n\n')
    part1(passports)
    part2(passports)
