from functools import reduce, cmp_to_key
from collections import defaultdict
import math
import json


def parse_input(input_file):
    lines = open(input_file, "r").read().split("\n")
    lines = [line for line in lines if line != ""]

    # Need to parse line into a list of lists and integers
    def parse_packet(line):
        # stack = []
        # packet = None
        # for c in line:
        #     if c == "[":
        #         stack.append([])
        #     elif c == "]":
        #         s = stack.pop()
        #         packet = s
        #         if stack:
        #             stack[-1].append(s)
        #     elif c != ",":
        #         if stack:
        #             stack[-1].append(int(c))
        # return packet
        return json.loads(line)

    packets = []
    for line in lines:
        packets.append(parse_packet(line))

    pairs = []
    for i in range(0, len(packets), 2):
        pairs.append([packets[i], packets[i + 1]])

    return packets, pairs


def in_order(packet_1, packet_2):
    max_len = max(len(packet_1), len(packet_2))

    for index in range(max_len):
        if index >= len(packet_1):
            return True
        if index >= len(packet_2):
            return False

        left = packet_1[index]
        right = packet_2[index]

        # If both are integers
        if type(left) == int and type(right) == int:
            if left > right:
                return False
            elif left < right:
                return True
        # If both are lists
        elif type(left) == list and type(right) == list:
            result = in_order(left, right)
            if result is not None:
                return result
        # If is an integer, convert other to list
        elif type(left) == int:
            result = in_order([left], right)
            if result is not None:
                return result
        elif type(right) == int:
            result = in_order(left, [right])
            if result is not None:
                return result

    return None


def part_1():
    packets, pairs = parse_input("input.prod")
    sum = 0
    for index, pair in enumerate(pairs):
        sum += index + 1 if in_order(pair[0], pair[1]) else 0

    return sum


def part_2():
    packets, pairs = parse_input("input.prod")

    # Add the divider packets
    packets.append([[2]])
    packets.append([[6]])

    def compare(packet_1, packet_2):
        result = in_order(packet_1, packet_2)
        if result:
            return -1
        elif not result:
            return 1

        return 0

    # Sort the packets
    packets = sorted(packets, key=cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
