from functools import reduce

lines = open("input.prod", "r").read().split("\n")
lines.pop()  # get rid of empty line

# [M] [H]         [N]
# [S] [W]         [F]     [W] [V]
# [J] [J]         [B]     [S] [B] [F]
# [L] [F] [G]     [C]     [L] [N] [N]
# [V] [Z] [D]     [P] [W] [G] [F] [Z]
# [F] [D] [C] [S] [W] [M] [N] [H] [H]
# [N] [N] [R] [B] [Z] [R] [T] [T] [M]
# [R] [P] [W] [N] [M] [P] [R] [Q] [L]
#  1   2   3   4   5   6   7   8   9


def part_1():
    stacks = [
        ["R", "N", "F", "V", "L", "J", "S", "M"],
        ["P", "N", "D", "Z", "F", "J", "W", "H"],
        ["W", "R", "C", "D", "G"],
        ["N", "B", "S"],
        ["M", "Z", "W", "P", "C", "B", "F", "N"],
        ["P", "R", "M", "W"],
        ["R", "T", "N", "G", "L", "S", "W"],
        ["Q", "T", "H", "F", "N", "B", "V"],
        ["L", "M", "H", "Z", "N", "F"],
    ]

    for line in lines:
        split = line.split(" ")
        quantity = int(split[1])
        from_s = stacks[int(split[3]) - 1]
        to_s = stacks[int(split[5]) - 1]
        while quantity > 0 and from_s:
            to_s.append(from_s.pop())
            quantity -= 1

    return reduce(lambda x, y: x + y[-1], stacks, "")


def part_2():
    stacks = [
        ["R", "N", "F", "V", "L", "J", "S", "M"],
        ["P", "N", "D", "Z", "F", "J", "W", "H"],
        ["W", "R", "C", "D", "G"],
        ["N", "B", "S"],
        ["M", "Z", "W", "P", "C", "B", "F", "N"],
        ["P", "R", "M", "W"],
        ["R", "T", "N", "G", "L", "S", "W"],
        ["Q", "T", "H", "F", "N", "B", "V"],
        ["L", "M", "H", "Z", "N", "F"],
    ]

    for line in lines:
        split = line.split(" ")
        quantity = int(split[1])
        from_s = stacks[int(split[3]) - 1]
        to_s = stacks[int(split[5]) - 1]
        temp_s = []

        while len(temp_s) < quantity and from_s:
            temp_s.append(from_s.pop())

        while temp_s:
            to_s.append(temp_s.pop())

    return reduce(lambda x, y: x + y[-1], stacks, "")


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
