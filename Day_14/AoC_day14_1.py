import numpy as np


def read_input(filename):
    """
    Reads the input positions and velocities of robots from a file and returns them as lists of tuples.

    Args:
        filename (str): The name of the input file.

    Returns:
        list: A list of tuples representing the initial positions of robots.
        list: A list of tuples representing the velocities of robots.
    """
    positions = []
    velocities = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            p_part, v_part = line.split(' v=')
            x, y = map(int, p_part[2:].split(','))
            vx, vy = map(int, v_part.split(','))
            positions.append((x, y))
            velocities.append((vx, vy))
    return positions, velocities


def update_positions(positions, velocities, seconds, width, height):
    """
    Updates the positions of robots based on their velocities after a given number of seconds.

    Args:
        positions (list): A list of tuples representing the initial positions of robots.
        velocities (list): A list of tuples representing the velocities of robots.
        seconds (int): The number of seconds to simulate.
        width (int): The width of the space.
        height (int): The height of the space.

    Returns:
        list: A list of tuples representing the new positions of robots.
    """
    new_positions = []
    for (x, y), (vx, vy) in zip(positions, velocities):
        new_x = (x + vx * seconds) % width
        new_y = (y + vy * seconds) % height
        new_positions.append((new_x, new_y))
    return new_positions


def count_robots_in_quadrants(positions, width, height):
    """
    Counts the number of robots in each quadrant of the space.

    Args:
        positions (list): A list of tuples representing the positions of robots.
        width (int): The width of the space.
        height (int): The height of the space.

    Returns:
        tuple: The counts of robots in the four quadrants.
    """
    mid_x = width // 2
    mid_y = height // 2

    q1 = q2 = q3 = q4 = 0

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x > mid_x and y < mid_y:
            q1 += 1
        elif x < mid_x and y < mid_y:
            q2 += 1
        elif x < mid_x and y > mid_y:
            q3 += 1
        elif x > mid_x and y > mid_y:
            q4 += 1

    return q1, q2, q3, q4


def calculate_safety_factor(quadrant_counts):
    """
    Calculates the safety factor by multiplying the counts of robots in each quadrant.

    Args:
        quadrant_counts (tuple): The counts of robots in the four quadrants.

    Returns:
        int: The safety factor.
    """
    q1, q2, q3, q4 = quadrant_counts
    return q1 * q2 * q3 * q4


def main():
    # Parameters
    width = 101
    height = 103
    seconds = 100

    # Read the input positions and velocities of robots from the file
    positions, velocities = read_input('input1.txt')

    # Update the positions of robots after the given number of seconds
    new_positions = update_positions(positions, velocities, seconds, width, height)

    # Count the number of robots in each quadrant
    quadrant_counts = count_robots_in_quadrants(new_positions, width, height)

    # Calculate the safety factor
    safety_factor = calculate_safety_factor(quadrant_counts)

    # Print the safety factor
    print(f'The safety factor after {seconds} seconds is: {safety_factor}')


if __name__ == "__main__":
    main()
