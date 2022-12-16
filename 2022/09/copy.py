from functools import reduce
import math

lines = open("input.test", "r").read().split("\n")
lines = [line for line in lines if line != ""]


class Vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def update_positions(direction, units, head, tail, history):
    dir_map = {"R": Vec(1, 0), "L": Vec(-1, 0), "U": Vec(0, 1), "D": Vec(0, -1)}
    dir = dir_map[direction]
    for i in range(units):
        # Update position of head
        prev_head = Vec(head.x, head.y)
        head.x += dir.x
        head.y += dir.y
        x = (head.x - tail.x) ** 2
        y = (head.y - tail.y) ** 2
        distance = round(math.sqrt(x + y))

        # Figure out if tail's position needs to be updated
        if distance >= 2:
            # Determine tail's new position
            tail.x = prev_head.x
            tail.y = prev_head.y
            history.add((tail.x, tail.y))


def update_all_positions(direction, units, knots, head, tail, history):
    dir_map = {"R": Vec(1, 0), "L": Vec(-1, 0), "U": Vec(0, 1), "D": Vec(0, -1)}
    dir = dir_map[direction]
    for i in range(units):
        # Need to update each knot in knots
        # Start with head
        head.x += dir.x
        head.y += dir.y

        pointer = 1
        while pointer < 10:
            # Check if knot at pointer needs to be updated
            prev_knot = knots[pointer - 1]
            knot = knots[pointer]

            x = (prev_knot.x - knot.x) ** 2
            y = (prev_knot.y - knot.y) ** 2
            if round(math.sqrt(x + y)) >= 2:

                pass
            pointer += 1

        history.add((tail.x, tail.y))


def part_1():
    # Positions start at 0,0
    head = Vec()
    tail = Vec()
    history = set()
    history.add((0, 0))

    for line in lines:
        command = line.split(" ")
        dir = command[0]
        units = int(command[1])
        update_positions(dir, units, head, tail, history)

    return len(history)


def part_2():
    # Positions start at 0,0
    knots = [Vec() for i in range(10)]
    head = knots[0]
    tail = knots[-1]
    history = set()
    history.add((0, 0))

    for line in lines:
        command = line.split(" ")
        dir = command[0]
        units = int(command[1])
        update_all_positions(dir, units, knots, head, tail, history)

    return len(history)


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
