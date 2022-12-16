from functools import reduce
import math
import sys

sys.set_int_max_str_digits(1000000000)

lines = open("input.prod", "r").read().split("\n")
lines = [line for line in lines if line != ""]


class Monkey:
    def __init__(self, index):
        self.index = index
        self.items = []
        self.operation = None
        self.divisor = 1
        self.true_monkey: Monkey = None
        self.false_monkey: Monkey = None
        self.num_inspections = 0

    def process(self, monkeys, mod=None):
        self.num_inspections += len(self.items)
        for item in self.items:
            # Inspect
            item = self.inspect_item(item)
            # Decrease
            if mod == None:
                item = item // 3
            else:
                item = item % mod
            # Throw
            self.throw_item(item, monkeys)

        self.items.clear()
        return self.num_inspections

    def throw_item(self, item, monkeys):
        if item % self.divisor == 0:
            monkeys[self.true_monkey].items.append(item)
        else:
            monkeys[self.false_monkey].items.append(item)

    def inspect_item(self, old):
        x = self.operation[0]
        operator = self.operation[1]
        y = self.operation[2]

        if x == "old":
            x = old
        if y == "old":
            y = old

        if operator == "+":
            return int(x) + int(y)
        elif operator == "*":
            return int(x) * int(y)

    def __repr__(self):
        return f"Monkey {self.index}: {self.items}\n"


def parse_input(lines):
    monkeys = []

    index = 0
    while index < len(lines):
        line = lines[index]
        # Start creating a new monkey
        if line.startswith("Monkey"):
            monkey = Monkey(len(monkeys))

            # Parse the monkey's items
            index += 1
            monkey.items = list(
                map(
                    lambda x: int(x),
                    lines[index].split("  Starting items: ")[1].split(", "),
                )
            )

            # Parse the operation
            index += 1
            monkey.operation = lines[index].split("  Operation: new = ")[1].split(" ")

            # Parse the test
            index += 1
            monkey.divisor = int(lines[index].split("  Test: divisible by ")[1])

            # Parse the true and false
            index += 1
            monkey.true_monkey = int(
                lines[index].split("    If true: throw to monkey ")[1]
            )
            index += 1
            monkey.false_monkey = int(
                lines[index].split("    If false: throw to monkey ")[1]
            )
            monkeys.append(monkey)
        index += 1

    return monkeys


def part_1():
    monkeys = parse_input(lines)

    for i in range(20):
        for j, m in enumerate(monkeys):
            m.process(monkeys)

    counts = sorted(list(map(lambda x: x.num_inspections, monkeys)))

    return counts[-1] * counts[-2]


def part_2():
    monkeys = parse_input(lines)

    # Determine super modulo
    mod = reduce(lambda x, y: x * y.divisor, monkeys, 1)

    for i in range(10000):
        for j, m in enumerate(monkeys):
            m.process(monkeys, mod)

    counts = sorted(list(map(lambda x: x.num_inspections, monkeys)))

    return counts[-1] * counts[-2]


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
