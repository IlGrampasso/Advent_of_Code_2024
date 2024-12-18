from collections import deque


# Function to read the list of byte positions from input file
def read_byte_positions(filename):
    with open(filename, 'r') as f:
        positions = [tuple(map(int, line.split(','))) for line in f.read().strip().split('\n')]
    return positions


# Function to initialize the grid and mark the corrupted positions
def initialize_grid(grid_size):
    return [['.' for _ in range(grid_size)] for _ in range(grid_size)]


# Function to print the grid (for visualization purposes)
def print_grid(grid):
    for row in grid:
        print(''.join(row))


# Function to find the shortest path using BFS
def bfs_shortest_path(grid, start, goal):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == goal:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[ny][nx] == '.' and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))

    return -1  # Return -1 if there is no path


# Read byte positions from input file
byte_positions = read_byte_positions('input1.txt')

# Initialize the grid
grid_size = 71
grid = initialize_grid(grid_size)

# Simulate the bytes falling one by one
start = (0, 0)
goal = (70, 70)

for i, (x, y) in enumerate(byte_positions):
    grid[y][x] = '#'

    # Check if there is still a path to the exit
    if bfs_shortest_path(grid, start, goal) == -1:
        print(f"{x},{y}")
        break
