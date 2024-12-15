import numpy as np


def read_input(filename):
    """
    Reads the initial map and the sequence of movements from a file.

    Args:
        filename (str): The name of the input file.

    Returns:
        np.array: A numpy array representing the initial map.
        str: A string representing the sequence of movements.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Find the index of the newline separating the map and the instructions
    newline_idx = lines.index('\n')

    # Parse the map into a 2D list and convert to numpy array
    tiles = [[char for char in line.strip()] for line in lines[:newline_idx]]
    grid = np.array(tiles)

    # Parse the instructions and concatenate them into a single string
    instructions = ''.join(line.strip() for line in lines[newline_idx + 1:])

    return grid, instructions


def in_grid(x, y, grid):
    """
    Checks if the given coordinates are within the grid bounds.

    Args:
        x (int): The x coordinate.
        y (int): The y coordinate.
        grid (np.array): The grid representing the map.

    Returns:
        bool: True if the coordinates are within bounds, False otherwise.
    """
    return 0 <= x < grid.shape[1] and 0 <= y < grid.shape[0]


def simulate_robot(grid, instructions):
    """
    Simulates the movement of the robot and boxes based on the sequence of movements.

    Args:
        grid (np.array): A numpy array representing the initial map.
        instructions (str): A string representing the sequence of movements.

    Returns:
        np.array: A numpy array representing the final map.
    """
    robot = np.argwhere(grid == '@')[0]
    movemap = {'>': [1, 0], '<': [-1, 0], 'v': [0, 1], '^': [0, -1]}
    moves = [movemap[instruction] for instruction in instructions]

    for mx, my in moves:
        can_shift = True
        shift_len = 1
        while can_shift and in_grid(robot[1] + mx * shift_len, robot[0] + my * shift_len, grid):
            next_tile = grid[robot[0] + my * shift_len, robot[1] + mx * shift_len]
            if next_tile == '#':
                can_shift = False
            elif next_tile == 'O':
                shift_len += 1
            elif next_tile == '.':
                break
        if can_shift:
            previous_tile = '.'
            for i in range(shift_len + 1):
                this_tile = grid[robot[0] + my * i, robot[1] + mx * i]
                grid[robot[0] + my * i, robot[1] + mx * i] = previous_tile
                previous_tile = this_tile
            robot = [robot[0] + my, robot[1] + mx]

    return grid


def calculate_gps_sum(grid):
    """
    Calculates the sum of the GPS coordinates of the boxes.

    Args:
        grid (np.array): A numpy array representing the map.

    Returns:
        int: The sum of the GPS coordinates of the boxes.
    """
    boxes = np.argwhere(grid == 'O')
    total = sum([100 * y + x for y, x in boxes])
    return total


def main():
    # Read the input map and the sequence of movements from the file
    grid, instructions = read_input('input1.txt')

    # Simulate the movements of the robot and boxes
    final_grid = simulate_robot(grid, instructions)

    # Calculate the sum of the GPS coordinates of the boxes
    gps_sum = calculate_gps_sum(final_grid)

    # Print the final map
    for row in final_grid:
        print(''.join(row))

    # Print the sum of the GPS coordinates
    print("Sum of GPS coordinates of the boxes:", gps_sum)


if __name__ == "__main__":
    main()
