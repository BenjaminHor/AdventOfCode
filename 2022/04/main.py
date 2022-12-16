input_file = "input.prod"  # prod or test

file = open(input_file, "r")
lines = [line.replace("\n", "") for line in file.readlines()]


def part_1():
    sum = 0
    for line in lines:
        line = line.replace(",", "-").split("-")

        e1_low = int(line[0])
        e1_high = int(line[1])
        e2_low = int(line[2])
        e2_high = int(line[3])

        if (
            e1_low >= e2_low
            and e1_high <= e2_high
            or e2_low >= e1_low
            and e2_high <= e1_high
        ):
            sum += 1

    return str(sum)


def part_2():
    sum = 0
    for line in lines:
        line = line.replace(",", "-").split("-")

        e1_low = int(line[0])
        e1_high = int(line[1])
        e2_low = int(line[2])
        e2_high = int(line[3])

        if e2_high >= e1_low and e2_high <= e1_high:
            sum += 1
        elif e1_high >= e2_low and e1_high <= e2_high:
            sum += 1

    return str(sum)


print("Part 1 Answer: " + part_1())
print("Part 2 Answer: " + part_2())
