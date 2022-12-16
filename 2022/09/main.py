from functools import reduce
import math

lines = open("input.prod", "r").read().split("\n")
lines = [line for line in lines if line != ""]


class Vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + ":" + str(self.y)


def update_all_positions(direction, units, knots, head, tail, history):
    dir_map = {"R": Vec(1, 0), "L": Vec(-1, 0), "U": Vec(0, 1), "D": Vec(0, -1)}
    dir = dir_map[direction]
    for i in range(units):
        # reset_grid()
        # Need to update each knot in knots
        # Start with head
        head.x += dir.x
        head.y += dir.y

        pointer = 1
        while pointer < len(knots):
            # Check if knot at pointer needs to be updated
            prev_knot = knots[pointer - 1]
            knot = knots[pointer]

            x = (prev_knot.x - knot.x) ** 2
            y = (prev_knot.y - knot.y) ** 2
            if round(math.sqrt(x + y)) >= 2:
                # Knot's new position is the normalized offset
                # x, y must be within range [-1, 1] (normalized)
                offset_x = prev_knot.x - knot.x
                offset_y = prev_knot.y - knot.y
                if offset_x >= 0:
                    offset_x = min(offset_x, 1)
                elif offset_x < 0:
                    offset_x = max(offset_x, -1)
                if offset_y >= 0:
                    offset_y = min(offset_y, 1)
                elif offset_y < 0:
                    offset_y = max(offset_y, -1)
                knot.x += offset_x
                knot.y += offset_y

            pointer += 1

        # reset_grid()
        # for i in range(len(knots) - 1, -1, -1):
        #     knot = knots[i]
        #     grid[knot.y % len(grid)][knot.x % len(grid[0])] = str(i)
        # print("--------------------------------")
        # print_grid()
        # input("")

        history.add((tail.x, tail.y))


grid = []


def print_grid():
    global grid
    for row in range(len(grid) - 1, -1, -1):
        line = ""
        for col in grid[row]:
            line += col + " "
        print(line)


def reset_grid():
    global grid
    grid = [["." for i in range(30)] for i in range(20)]


def part_1():
    # Positions start at 0,0
    knots = [Vec() for i in range(2)]
    head = knots[0]
    tail = knots[-1]
    history = set()
    history.add((0, 0))
    # reset_grid()
    # grid[head.y][head.x] = "0"
    # print_grid()

    for line in lines:
        command = line.split(" ")
        dir = command[0]
        units = int(command[1])
        update_all_positions(dir, units, knots, head, tail, history)

    return len(history)


def part_2():
    global grid
    # Positions start at 0,0
    knots = [Vec() for i in range(10)]
    head = knots[0]
    tail = knots[-1]
    history = set()
    history.add((0, 0))
    # reset_grid()
    # grid[head.y][head.x] = "0"
    # print_grid()

    for line in lines:
        command = line.split(" ")
        dir = command[0]
        units = int(command[1])
        update_all_positions(dir, units, knots, head, tail, history)

    return len(history)


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
