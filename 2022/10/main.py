from functools import reduce
import math

lines = open("input.prod", "r").read().split("\n")
lines = [line for line in lines if line != ""]


def get_register_log():
    register = 1
    register_log = []

    pointer = 0
    instructions = []
    while pointer < len(lines):
        # Log the current register value
        register_log.append(register)

        # START OF CYCLE
        if not instructions:
            # Read a new instruction
            split = lines[pointer].split(" ")
            if split[0] == "addx":
                instructions.append([split[0], split[1], 2])
            else:
                instructions.append([split[0], "", 1])
            pointer += 1

        # Process the current instruction
        instructions[-1][2] -= 1

        # Check if current instruction has completed
        if instructions[-1][2] == 0:
            # Execute the instruction
            if instructions[-1][0] == "addx":
                register += int(instructions[-1][1])

            instructions.pop()
        # END OF CYCLE

    return register_log


def is_visible(pixel_pos, sprite_position):
    return pixel_pos in (sprite_position - 1, sprite_position, sprite_position + 1)


def part_1():
    signal_cycles = (20, 60, 100, 140, 180, 220)

    return reduce(
        lambda x, y: x + ((y[0] + 1) * y[1]),
        list(
            filter(
                lambda x: x[0] + 1 in signal_cycles, list(enumerate(get_register_log()))
            )
        ),
        0,
    )


def part_2():
    image = ""
    for cycle, pos in enumerate(get_register_log()):
        cycle = cycle % 40
        if is_visible(cycle, pos):
            image += "#"
        else:
            image += " "

        if cycle == 39:
            image += "\n"
    return image


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer:\n" + part_2())
