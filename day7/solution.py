import re

def solve(rules):

    bags = {}
    bag_count = 0

    for rule in rules:
        colour = re.match(r"(.+?) bags contain", rule)[1]
        bags[colour] = re.findall(r"(\d+?) (.+?) bags?", rule)

    def has_shiny_gold(colour):
        if colour == "shiny gold":
            return True
        else:
            return any(has_shiny_gold(c) for _, c in bags[colour])

    for bag in bags:
        if has_shiny_gold(bag):
            bag_count += 1

    print("Solution to part 1 is: " + str(bag_count - 1))

    #part2

    def count_bags(bag_type):
        return 1 + sum(int(number) * count_bags(colour) for number, colour in bags[bag_type])

    print("Solution to part 2 is: " + str(count_bags("shiny gold") - 1))


with open('data.txt', 'r') as f:
    rules = f.read().splitlines()
    solve(rules)
