from typing import Tuple, List
from math import sqrt

# Function to check if coordinates are within the matrix bounds
def is_valid(x, y, max_x, max_y):
    return 0 <= x <= max_x and 0 <= y <= max_y

# Function to search for the "MAS" or "SAM" pattern in an "X" shape
def search(loc: Tuple[int, int], grid: List[List[str]], x_max: int, y_max: int):
    y, x = loc

    # Define the corners for the "X" pattern
    corners = [(y-1, x-1), (y-1, x+1), (y+1, x-1), (y+1, x+1)]

    # Check if corners are not out of bounds
    if all([is_valid(x, y, x_max, y_max) for y, x in corners]):
        # Check if the diagonals form "MAS" or "SAM"
        return all([sorted([grid[n[0]][n[1]] for j, n in enumerate(corners) if i != j and sqrt((n[1]-c[1])**2 + (n[0]-c[0])**2) == 2]) == ["M", "S"] for i, c in enumerate(corners)])
    else:
        return False

# Open the file and read the grid
with open("input1.txt") as f:
    grid = [[char for char in line.strip()] for line in f]

# Count the occurrences of the "MAS" or "SAM" pattern in an "X" shape
ans = sum([search((i, j), grid, len(grid[0])-1, len(grid)-1) for i, row in enumerate(grid) for j, col in enumerate(row) if col == "A"])

print(ans)
