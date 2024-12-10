import numpy as np


def read_input(filename):
    """
    Reads the input topographic map from a file and returns it as a NumPy matrix.

    Args:
        filename (str): The name of the input file.

    Returns:
        np.array: The topographic map as a NumPy matrix.
    """
    with open(filename, 'r') as file:
        lines = np.array([list(map(int, list(line.strip()))) for line in file.readlines()])
    return lines


def walk_the_trail2(location, curr_height, matrix, peaks):
    """
    Walks the hiking trail recursively and appends the locations with height 9 to peaks.

    Args:
        location (tuple): The current position on the map.
        curr_height (int): The current height on the map.
        matrix (np.array): The topographic map as a NumPy matrix.
        peaks (list): The list of locations with height 9.
    """
    if curr_height == 9:
        peaks.append(location)
        return

    # Check 4 directions (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = location[0] + di, location[1] + dj
        if 0 <= ni < matrix.shape[0] and 0 <= nj < matrix.shape[1] and matrix[ni, nj] == curr_height + 1:
            walk_the_trail2((ni, nj), matrix[ni, nj], matrix, peaks)


def calculate_total_score(filename):
    """
    Calculates the total score of all trailheads on the topographic map.

    Args:
        filename (str): The name of the input file.

    Returns:
        int: The total score of all trailheads.
    """
    matrix = read_input(filename)
    trailheads = np.argwhere(matrix == 0)

    total_score = 0
    for trailhead in trailheads:
        peaks = []
        walk_the_trail2(tuple(trailhead), 0, matrix, peaks)
        total_score += len(peaks)

    return total_score


def main():
    total_score = calculate_total_score('input1.txt')
    print(f'The sum of the scores of all trailheads is: {total_score}')


if __name__ == "__main__":
    main()
