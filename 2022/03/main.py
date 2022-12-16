input_file = "input.prod"  # prod or test

file = open(input_file, "r")
lines = file.readlines()


def part_1():
    priorities = {}
    for i in range(97, 122 + 1):
        priorities[chr(i)] = i - 97 + 1
    for i in range(65, 90 + 1):
        priorities[chr(i)] = i - 65 + 1 + 26

    sum = 0
    # Determine common priority in each line
    for line in lines:
        # Split line in half
        h1 = set(line[0 : len(line) // 2])
        h2 = set(line[len(line) // 2 :])
        # Find intersection, aka common priority
        common = h1.intersection(h2)
        sum += priorities[common.pop()]

    return str(sum)


def part_2():
    priorities = {}
    for i in range(97, 122 + 1):
        priorities[chr(i)] = i - 97 + 1
    for i in range(65, 90 + 1):
        priorities[chr(i)] = i - 65 + 1 + 26

    sum = 0
    # Divide lines into groups of three lines
    # Determine intersection between all three
    for group in [lines[i : i + 3] for i in range(0, len(lines), 3)]:
        g1 = set(group[0].replace("\n", ""))
        g2 = set(group[1].replace("\n", ""))
        g3 = set(group[2].replace("\n", ""))
        common = g1.intersection(g2, g3)
        sum += priorities[common.pop()]

    return str(sum)


print("Part 1 Answer: " + part_1())
print("Part 2 Answer: " + part_2())
