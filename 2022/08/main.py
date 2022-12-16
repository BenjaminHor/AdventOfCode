from functools import reduce

lines = open("input.prod", "r").read().split("\n")
lines = [line for line in lines if line != ""]


def is_visible(row, col, trees):
    tree = int(trees[row][col])

    n_visible = tree > max([int(trees[i][col]) for i in range(row - 1, -1, -1)])

    s_visible = tree > max([int(trees[i][col]) for i in range(row + 1, len(trees))])

    e_visible = tree > max([int(trees[row][i]) for i in range(col - 1, -1, -1)])

    w_visible = tree > max(
        [int(trees[row][i]) for i in range(col + 1, len(trees[row]))]
    )

    return n_visible or s_visible or e_visible or w_visible


def get_score(row, col, trees):
    tree = int(trees[row][col])

    north = [int(trees[i][col]) for i in range(row - 1, -1, -1)]
    n = 0
    for t in north:
        n += 1
        if t >= tree:
            break

    south = [int(trees[i][col]) for i in range(row + 1, len(trees))]
    s = 0
    for t in south:
        s += 1
        if t >= tree:
            break

    east = [int(trees[row][i]) for i in range(col - 1, -1, -1)]
    e = 0
    for t in east:
        e += 1
        if t >= tree:
            break

    west = [int(trees[row][i]) for i in range(col + 1, len(trees[row]))]
    w = 0
    for t in west:
        w += 1
        if t >= tree:
            break

    return n * s * e * w


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
