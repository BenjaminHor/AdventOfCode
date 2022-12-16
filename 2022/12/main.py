from functools import reduce
from collections import defaultdict
import math


class Node:
    def __init__(self, value, row, col):
        self.value = value
        self.neighbors = []
        self.visited = False
        self.row = row
        self.col = col
        self.str = f"({self.row},{self.col}):{self.value}"

    def __repr__(self):
        return self.str

    def __str__(self):
        return self.str

    def __hash__(self):
        return hash(f"{self.row} {self.col}")

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.row == other.row and self.col == other.col


def parse_input(input_file):
    lines = open(input_file, "r").read().split("\n")
    lines = [line for line in lines if line != ""]

    nodes = []
    start_node = None
    end_node = None

    # For each character, create a Node
    for r, row in enumerate(lines):
        new_row = []
        for c, col in enumerate(row):
            node = Node(col, r, c)
            new_row.append(node)
            if col == "S":
                start_node = node
            elif col == "E":
                end_node = node
        nodes.append(new_row)

    # Determine neighbors for each node
    for r, row in enumerate(nodes):
        for c, curr_node in enumerate(row):
            neighbors = get_neighbors(nodes, r, c)
            if curr_node.value == "S":
                curr_node.neighbors = neighbors
            else:
                curr_node.neighbors = list(
                    filter(lambda x: can_traverse(curr_node, x), neighbors)
                )

    return (start_node, end_node, nodes)


def get_neighbors(nodes, row, col):
    neighbors = []

    num_rows = len(nodes)
    num_cols = len(nodes[0])

    # North neighbor
    if row - 1 >= 0:
        node = nodes[row - 1][col]
        neighbors.append(node)
    # South neighbor
    if row + 1 < num_rows:
        node = nodes[row + 1][col]
        neighbors.append(node)
    # East neighbor
    if col - 1 >= 0:
        node = nodes[row][col - 1]
        neighbors.append(node)
    # West neighbor
    if col + 1 < num_cols:
        node = nodes[row][col + 1]
        neighbors.append(node)

    return neighbors


def can_traverse(node_a, node_b):
    a_val = ord(node_a.value)
    b_val = ord(node_b.value)
    if node_a.value == "S":
        a_val = ord("a")
    if node_b.value == "S":
        b_val = ord("a")
    if node_a.value == "E":
        a_val = ord("z")
    if node_b.value == "E":
        b_val = ord("z")
    return b_val - a_val <= 1


def bfs(start_node):
    queue = [start_node]
    start_node.visited = True

    distances = defaultdict(lambda: 0)
    parents = defaultdict(lambda: 0)
    while queue:
        curr_node = queue.pop(0)

        # Append neighbors we haven't seen
        for neighbor in curr_node.neighbors:
            if not neighbor.visited:
                queue.append(neighbor)
                neighbor.visited = True
                distances[neighbor] = distances[curr_node] + 1
                parents[neighbor] = curr_node

    return parents, distances


def reset(nodes):
    for row in nodes:
        for n in row:
            n.visited = False


def part_1():
    start_node, end_node, nodes = parse_input("input.prod")

    # for row in nodes:
    #     for node in row:
    #         print(node, "->", node.neighbors)

    # Need to perform some sort of graph search
    parents, distances = bfs(start_node)
    return distances[end_node]


def part_2():
    start_node, end_node, nodes = parse_input("input.prod")

    # for row in nodes:
    #     for node in row:
    #         print(node, "->", node.neighbors)

    # Find all nodes of elevation a
    start_nodes = []
    for row in nodes:
        for n in row:
            if n.value == "S" or n.value == "a":
                start_nodes.append(n)

    def get_distance(node):
        parents, distances = bfs(node)
        reset(nodes)
        return distances[end_node]

    distances = list(filter(lambda x: x != 0, map(get_distance, start_nodes)))

    return min(distances)


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
