from collections import deque


# Function to read the list of byte positions from input file
def read_byte_positions(filename):
    with open(filename, 'r') as f:
        positions = [tuple(map(int, line.split(','))) for line in f.read().strip().split('\n')]
    return positions


# Function to initialize the grid and mark the corrupted positions
def initialize_grid(byte_positions, grid_size):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in byte_positions:
        grid[y][x] = '#'
    return grid


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

# Simulate the first 1024 bytes falling onto the memory space
grid_size = 71
byte_positions = byte_positions[:1024]
grid = initialize_grid(byte_positions, grid_size)

# Print the grid after the first 1024 bytes have fallen
print("Grid after 1024 bytes:")
print_grid(grid)

# Find the shortest path from top left corner (0, 0) to bottom right corner (70, 70)
start = (0, 0)
goal = (70, 70)
min_steps = bfs_shortest_path(grid, start, goal)

print("Minimum number of steps needed to reach the exit:", min_steps)
