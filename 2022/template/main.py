from functools import reduce, cmp_to_key
from collections import defaultdict
import math
import json


def parse_input(input_file):
    lines = open(input_file, "r").read().split("\n")
    lines = [line for line in lines if line != ""]


def part_1():
    parse_input("input.prod")

    return 0


def part_2():
    parse_input("input.prod")

    return 0


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
