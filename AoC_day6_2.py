from typing import List, Tuple
from collections import defaultdict

def read_map_from_file(filename: str) -> List[List[str]]:
    with open(filename, 'r') as file:
        map_lines = [list(line.strip()) for line in file.readlines()]
    return map_lines

def simulate_guard(grid: List[List[str]], start_pos: Tuple[int, int], directions: List[Tuple[int, int]]) -> bool:
    h, w = len(grid), len(grid[0])
    steps = set()  # Set to track the steps and detect loops
    dir_idx = 0  # Start facing North
    prev = start_pos  # Initialize the starting position

    while True:
        dy, dx = directions[dir_idx]
        next_pos = (prev[0] + dy, prev[1] + dx)

        # Check if next position is out of bounds
        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] >= h or next_pos[1] >= w:
            break

        val = grid[next_pos[0]][next_pos[1]]

        if val == '#':  # If an obstacle is encountered, rotate 90 degrees clockwise
            dir_idx = (dir_idx + 1) % len(directions)
        elif prev + next_pos in steps:  # If the position has been visited before, a loop is detected
            return True
        else:
            steps.add(prev + next_pos)  # Add the current step to the set
            prev = next_pos  # Move to the next position

    return False  # Return False if no loop is detected

def count_loop_obstructions(grid: List[List[str]]) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Define movement directions: North, East, South, West
    start_pos = next(
        (i, j) for i, row in enumerate(grid)
        for j, element in enumerate(row) if element == '^'
    )

    loop_count = 0

    # Iterate through each position on the grid
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                continue

            original_val = grid[y][x]  # Save the original value
            grid[y][x] = '#'  # Place an obstruction

            if simulate_guard(grid, start_pos, directions):  # Check if the obstruction causes a loop
                loop_count += 1

            grid[y][x] = original_val  # Restore the original value

    return loop_count

# Read the map from the file
filename = "input1.txt"
grid = read_map_from_file(filename)

# Run the function
result = count_loop_obstructions(grid)
print(f"Number of positions for new obstructions to cause loops: {result}")
