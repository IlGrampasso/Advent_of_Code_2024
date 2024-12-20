import networkx as nx

# Read the input from the file
grid = open('input1.txt').read().splitlines()

# Minimum time saved required to be considered a cheat
min_saved = 100

# Parse the board and find start (S) and end (E) positions
board = {(r, c): ch for r, row in enumerate(grid) for c, ch in enumerate(row) if ch != '#'}
S = [x for x in board if board[x] == 'S'][0]
E = [x for x in board if board[x] == 'E'][0]
board = set(board)

# Function to get the Manhattan neighbors within a given distance
def neighbors(A, k):
    def _manhattan_neighbors(x, y, k):
        points = set()
        for dx in range(-k, k + 1):
            dy = k - abs(dx)
            points.add((x + dx, y + dy))
            points.add((x + dx, y - dy))
        return points
    return _manhattan_neighbors(A[0], A[1], k) & board

# Create a graph of the board
G = nx.Graph()
for x in board:
    for n in neighbors(x, 1):
        G.add_edge(x, n)

# Find the shortest path from start (S) to end (E) using Dijkstra's algorithm
dS, path = nx.single_source_dijkstra(G, source=S)
path = set(path[E])

# Function to calculate the Manhattan distance between two points
def dist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

# Part 1: Find the number of cheats that save at least `min_saved` picoseconds
t = 0
for x in path:
    for y in neighbors(x, 2):
        if (dS[y] - dS[x]) - dist(x, y) >= min_saved:
            t += 1
print("Part 1:", t)

# Part 2: Find the number of cheats that save at least `min_saved` picoseconds considering up to 20 picoseconds of cheating
t = 0
for x in path:
    for k in range(20 + 1):
        for y in neighbors(x, k):
            if (dS[y] - dS[x]) - dist(x, y) >= min_saved:
                t += 1
print("Part 2:", t)
