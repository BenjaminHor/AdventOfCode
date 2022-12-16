from functools import reduce

lines = open("input.prod", "r").read().split("\n")
lines = [line for line in lines if line != ""]


def part_1():
    data = lines[0]

    for i in range(len(data) - 4):
        if (len(set(data[i : i + 4]))) == 4:
            return i + 4
    return ""


def part_2():
    data = lines[0]

    for i in range(len(data) - 14):
        if (len(set(data[i : i + 14]))) == 14:
            return i + 14
    return ""


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
