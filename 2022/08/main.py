from functools import reduce

lines = open("input.prod", "r").read().split("\n")
lines = [line for line in lines if line != ""]


def is_visible(row, col, trees):
    tree = trees[row][col]

    # Need to search outward, north, south, east, west
    # North
    pointer = row - 1
    n_visible = True
    while pointer >= 0:
        adj = trees[pointer][col]
        if adj >= tree:
            n_visible = False
            break
        pointer -= 1

    # South
    pointer = row + 1
    s_visible = True
    while pointer < len(trees):
        adj = trees[pointer][col]
        if adj >= tree:
            s_visible = False
            break
        pointer += 1

    # East
    pointer = col - 1
    e_visible = True
    while pointer >= 0:
        adj = trees[row][pointer]
        if adj >= tree:
            e_visible = False
            break
        pointer -= 1

    # West
    pointer = col + 1
    w_visible = True
    while pointer < len(trees[0]):
        adj = trees[row][pointer]
        if adj >= tree:
            w_visible = False
            break
        pointer += 1

    return n_visible or s_visible or e_visible or w_visible


def get_score(row, col, trees):
    tree = trees[row][col]

    # Need to search outward, north, south, east, west
    # North
    pointer = row - 1
    n_score = 0
    while pointer >= 0:
        n_score += 1
        adj = trees[pointer][col]
        if adj >= tree:
            break
        pointer -= 1

    # South
    pointer = row + 1
    s_score = 0
    while pointer < len(trees):
        s_score += 1
        adj = trees[pointer][col]
        if adj >= tree:
            break
        pointer += 1

    # East
    pointer = col - 1
    e_score = 0
    while pointer >= 0:
        e_score += 1
        adj = trees[row][pointer]
        if adj >= tree:
            break
        pointer -= 1

    # West
    pointer = col + 1
    w_score = 0
    while pointer < len(trees[0]):
        w_score += 1
        adj = trees[row][pointer]
        if adj >= tree:
            break
        pointer += 1
    return n_score * s_score * e_score * w_score


def part_1():
    num_visible = (len(lines[0]) * 2) + ((len(lines) - 2) * 2)

    for r in range(1, len(lines) - 1):
        for c in range(1, len(lines[0]) - 1):
            if is_visible(r, c, lines):
                num_visible += 1

    return num_visible


def part_2():
    scenic_score = 0
    for r in range(1, len(lines) - 1):
        for c in range(1, len(lines[0]) - 1):
            scenic_score = max(scenic_score, get_score(r, c, lines))

    return scenic_score


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
