from collections import deque
from functools import cache
from itertools import pairwise

# Function to parse input from 'input1.txt'
def parse_input():
    with open("input1.txt", "r") as file:
        data = file.read()
    return data.splitlines()

# Load the codes to be typed
CODES = parse_input()

# Define the numeric keypad mapping
N_PAD = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}

# Define the directional keypad mapping
D_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}

# List of keypads used
PADS = [N_PAD, D_PAD]

# Function to perform BFS on the keypad graph
def bfs(u, v, g):
    q = deque([(u, [])])
    seen = {u}
    shortest = None
    res = []
    while q:
        cur, path = q.popleft()
        if cur == v:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
        for nei, d in g[cur]:
            seen.add(nei)
            q.append((nei, path + [d]))
    return res

# Function to perform DFS with memoization
@cache
def dfs(seq, level, i=0):
    g = PADS[i]
    res = 0
    seq = "A" + seq
    for u, v in pairwise(seq):
        paths = bfs(u, v, g)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(dfs(path, level - 1, 1) for path in paths)
    return res

# Function to solve part one
def part_one():
    return sum(dfs(code, 2) * int(code[:3]) for code in CODES)

# Function to solve part two
def part_two():
    return sum(dfs(code, 25) * int(code[:3]) for code in CODES)

# Execute and print the results for both parts
print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
