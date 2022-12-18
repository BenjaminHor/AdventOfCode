from functools import reduce, cmp_to_key
from collections import defaultdict
import math
import json


def parse_input(input_file):
    lines = open(input_file, "r").read().split("\n")
    lines = [line for line in lines if line != ""]
    # Determine bounds of grid?
    left_bound = math.inf
    right_bound = 0
    lower_bound = 0
    for line in lines:
        split = line.split(" -> ")
        for s in split:
            left_bound = min(left_bound, int(s.split(",")[0]))
            right_bound = max(right_bound, int(s.split(",")[0]))
            lower_bound = max(lower_bound, int(s.split(",")[1]))
    map_grid = defaultdict(lambda: " ")
    grid = [
        [" " for i in range((right_bound - left_bound) + 1)]
        for j in range(lower_bound + 1)
    ]

    # Insert sand source
    grid[0][500 - left_bound] = "+"
    map_grid[(0, 500)] = " "

    # Populate the rock paths
    def populate_path(from_p, to_p, grid, map_grid):
        from_x, from_y = from_p
        to_x, to_y = to_p

        grid[from_y][from_x - left_bound] = "#"
        grid[to_y][to_x - left_bound] = "#"

        map_grid[(from_y, from_x)] = "#"
        map_grid[(to_y, to_x)] = "#"

        # Determine if the x or y coord differs
        if from_x != to_x:
            min_x = min(from_x, to_x)
            max_x = max(from_x, to_x)

            for i in range(min_x, max_x + 1):
                grid[from_y][i - left_bound] = "#"
                map_grid[(from_y, i)] = "#"
        elif from_y != to_y:
            min_y = min(from_y, to_y)
            max_y = max(from_y, to_y)

            for i in range(min_y, max_y + 1):
                grid[i][from_x - left_bound] = "#"
                map_grid[(i, from_x)] = "#"

    for line in lines:
        split = line.split(" -> ")
        for i in range(len(split) - 1):
            from_p = split[i].split(",")
            to_p = split[i + 1].split(",")
            populate_path(
                (int(from_p[0]), int(from_p[1])),
                (int(to_p[0]), int(to_p[1])),
                grid,
                map_grid,
            )

    return grid, map_grid, (left_bound, right_bound, lower_bound)


def print_grid(grid):
    for index, row in enumerate(grid):
        line = f"{index}".rjust(3, " ")
        for col in row:
            line += f" {col}"
        print(line)


def print_map_grid(map_grid, bounds):
    left_b, right_b, lower_b = bounds
    print(bounds)
    index = 0
    for row in range(0, lower_b + 1):
        line = f"{index}".rjust(3, " ")
        for col in range(left_b, right_b + 1):
            line += f" {map_grid[(row, col)]}"
        print(line)
        index += 1


def simulate(grid, bounds):
    left_b, right_b, lower_b = bounds

    x = 500 - left_b
    y = 0

    # Check to see if sand can move to a new position
    while True:
        try:
            if grid[y + 1][x] == " ":
                y += 1
            elif grid[y + 1][x - 1] == " ":
                x -= 1
                y += 1
            elif grid[y + 1][x + 1] == " ":
                x += 1
                y += 1
            else:
                grid[y][x] = "o"
                return True
        except:
            return False


def simulate_map(grid, bounds):
    x = 500
    y = 0

    # Check to see if sand can move to a new position
    while True:
        if grid[0, 500] == "o":
            return False

        if grid[y + 1, x] == " ":
            y += 1
        elif grid[y + 1, x - 1] == " ":
            x -= 1
            y += 1
        elif grid[y + 1, x + 1] == " ":
            x += 1
            y += 1
        else:
            grid[y, x] = "o"
            return True

        if y == bounds[2]:
            grid[y - 1, x] = "o"
            grid[y, x] = "#"
            return True


def part_1():
    grid, map_grid, bounds = parse_input("input.prod")
    count = 0
    while simulate(grid, bounds):
        count += 1
        # print_grid(grid)
        # result = input("")
        # if result == "q":
        #     break

    return count


def part_2():
    grid, map_grid, bounds = parse_input("input.prod")
    count = 0
    bounds = (bounds[0] - 5, bounds[1] + 5, bounds[2] + 2)
    while simulate_map(map_grid, bounds):
        count += 1
        # print_map_grid(map_grid, bounds)
        # result = input("")
        # if result == "q":
        #     break

    return count


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
