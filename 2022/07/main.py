from functools import reduce
from collections import defaultdict

lines = open("input.prod", "r").read().split("\n")
lines = [line for line in lines if line != ""]


class Node:
    def __init__(self, parent, type, name, size, children={}):
        self.parent = parent
        self.children = children
        self.type = type
        self.name = name
        self.size = size

    def __str__(self):
        return "" + self.type + ":" + self.name + ":" + str(self.size)


class FileSystem:
    def __init__(self, lines):
        self.root = Node(None, "dir", "/", 0)
        self.curr_node = self.root
        self.lines = lines
        self.build_tree()

    def change_dir(self, target_dir):
        if target_dir == "..":  # Move up one level from the current directory
            self.curr_node = self.curr_node.parent
        elif target_dir == "/":  # Move to the root directory
            self.curr_node = self.root
        else:  # Move to a deeper directory in the current directory
            self.curr_node = self.curr_node.children[target_dir]

    def list_files(self):
        while self.lines:
            split = self.lines[0].split(" ")
            # Decode the split
            if split[0] == "$":
                return "skip"
            elif split[0] == "dir":  # Add a new dir (node) to the curr_node children
                dir_name = split[1]
                self.curr_node.children[dir_name] = Node(
                    self.curr_node, "dir", dir_name, 0
                )
            else:  # Add a new file (node) to the curr_node children
                file_name = split[1]
                file_size = int(split[0])
                self.curr_node.children[file_name] = Node(
                    self.curr_node, "file", file_name, file_size
                )
            # We've evaluated the line, so we can discard it
            self.lines.pop(0)

        return ""

    def decode(self, line):
        split = line.split(" ")
        # Determine what kind of line this is
        if split[0] == "$":
            # This is a command line, determine what kind of command
            command = split[1]
            if command == "cd":
                self.change_dir(split[2])
                self.lines.pop(0)
            elif command == "ls":
                self.lines.pop(0)
                result = self.list_files()
                if result != "skip" and self.lines:
                    self.lines.pop(0)

    def build_tree(self):
        while self.lines:
            line = self.lines[0]
            self.decode(line)

    def print_tree_dfs(self):
        visited = set()
        stack = [self.root]

        while stack:
            node = stack.pop(0)
            visited.add(node.name)
            print(node)

            for key, value in node.children.items():
                if value.name not in visited:
                    stack.append(value)

    def print_tree_bfs(self):
        visited = [self.root]
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node)

            for key, value in node.children.items():
                if key not in visited:
                    visited.append(key)
                    queue.append(value)


def change_dir(dir, dir_stack, dir_size):
    if dir == "..":
        dir = dir_stack.pop()
        dir_size[dir_stack[-1]] += dir_size[dir]
    else:
        parent_dir = dir_stack[-1]
        dir_name = parent_dir + ">" + dir
        dir_stack.append(dir_name)


def list_files(pointer, lines, dir_stack, dir_size):
    pointer += 1
    while pointer < len(lines):
        split = lines[pointer].split(" ")
        if split[0] == "$":
            pointer -= 1
            break

        if split[0] != "dir":
            curr_dir = dir_stack[-1]
            dir_size[curr_dir] += int(split[0])
        pointer += 1

    return pointer


def part_1():
    dir_stack = ["/"]
    dir_size = defaultdict(int)
    dir_size["/"] = 0
    pointer = 1
    while pointer < len(lines):
        split = lines[pointer].split(" ")
        # Determine what kind of line this is
        if split[0] == "$":
            # This is a command line, determine what kind of command
            command = split[1]
            if command == "cd":
                change_dir(split[2], dir_stack, dir_size)
            elif command == "ls":
                pointer = list_files(pointer, lines, dir_stack, dir_size)
        pointer += 1

    while dir_stack:
        dir = dir_stack.pop()
        if dir_stack:
            dir_size[dir_stack[-1]] += dir_size[dir]

    sizes = filter(lambda x: x <= 100000, dir_size.values())
    return reduce(lambda x, y: x + y, list(sizes), 0)


def part_2():
    dir_stack = ["/"]
    dir_size = defaultdict(int)
    dir_size["/"] = 0
    pointer = 1
    while pointer < len(lines):
        split = lines[pointer].split(" ")
        # Determine what kind of line this is
        if split[0] == "$":
            # This is a command line, determine what kind of command
            command = split[1]
            if command == "cd":
                change_dir(split[2], dir_stack, dir_size)
            elif command == "ls":
                pointer = list_files(pointer, lines, dir_stack, dir_size)
        pointer += 1

    while dir_stack:
        dir = dir_stack.pop()
        if dir_stack:
            dir_size[dir_stack[-1]] += dir_size[dir]

    sizes = sorted(dir_size.values())
    unused_size = 70000000 - sizes[-1]
    return next(filter(lambda x: unused_size + x >= 30000000, sizes))


print("Part 1 Answer: " + str(part_1()))
print("Part 2 Answer: " + str(part_2()))
