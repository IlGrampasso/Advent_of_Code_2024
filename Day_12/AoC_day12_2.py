from collections import defaultdict
import os, sys

def main():
    # Open and read the input file
    with open(os.path.join(sys.path[0], "input1.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [list(line) for line in lines]
    width = len(grid[0])
    height = len(grid)

    # Holds all visited points
    visited_points = set()
    total = 0

    # Iterate through all points in the grid
    for y in range(height):
        for x in range(width):
            # If the point is already visited, skip it
            if (x, y) in visited_points:
                continue
            # Get the side count and size of the region
            side_count, size = expand_region(grid, x, y, visited_points)
            total += side_count * size

    # Print the total price
    print(total)


def expand_region(grid, x, y, visited_points):
    # Initialize the stack with the starting point for BFS
    stack = [(x, y)]
    # Set to store cells in the current region
    region = set([(x, y)])
    # Identifying the flower type for the region
    region_flower = grid[y][x]
    # Mark the starting point as visited
    visited_points.add((x, y))

    # Perform BFS
    while stack:
        x, y = stack.pop()
        # Check all 4 neighboring cells
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            # Skip if the neighbor is out of bounds
            if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
                continue
            # Skip if the neighbor is not the same flower type
            if grid[new_y][new_x] != region_flower:
                continue
            # Skip if the neighbor is already visited
            if (new_x, new_y) in visited_points:
                continue
            # Add the neighbor to the stack and mark it as visited
            stack.append((new_x, new_y))
            visited_points.add((new_x, new_y))
            region.add((new_x, new_y))

    # Return the size of the region and the number of sides
    return len(region), find_sides(region)


def find_sides(region):
    # Dictionary to store sides of the region
    sides = defaultdict(set)

    # Iterate through all points in the region
    for x, y in region:
        # Check all 4 neighboring cells
        vertical_left = (x - 1, y)
        vertical_right = (x + 1, y)
        horizontal_up = (x, y - 1)
        horizontal_down = (x, y + 1)

        # If a neighbor is out of the region, add the side
        if vertical_left not in region:
            sides[(x, 0)].add((x, y))
        if vertical_right not in region:
            sides[(x, 1)].add((x, y))
        if horizontal_up not in region:
            sides[(y, 2)].add((x, y))
        if horizontal_down not in region:
            sides[(y, 3)].add((x, y))

    # Count the number of sides
    side_count = 0

    # For each section of sides, perform BFS to count unique sides
    for section in sides.values():
        visited = set()
        for x, y in section:
            if (x, y) not in visited:
                grow_section(x, y, section, visited)
                side_count += 1

    return side_count


def grow_section(x, y, section, visited):
    # Initialize the stack for BFS
    stack = [(x, y)]

    # Perform BFS
    while stack:
        x, y = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            # Skip if the neighbor is out of bounds of the section
            if (new_x, new_y) not in section:
                continue
            # Skip if the neighbor is already visited
            if (new_x, new_y) in visited:
                continue
            # Add the neighbor to the stack and mark it as visited
            stack.append((new_x, new_y))
            visited.add((new_x, new_y))


if __name__ == "__main__":
    main()
