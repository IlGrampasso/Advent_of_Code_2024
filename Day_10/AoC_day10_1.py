import numpy as np

def read_input(filename):
    """
    Reads the input topographic map from a file and returns it as a NumPy matrix.

    Args:
        filename (str): The name of the input file.

    Returns:
        np.array: The topographic map as a NumPy matrix.
    """
    with open("input1.txt", 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    matrix = np.array([list(map(int, line)) for line in lines])
    return matrix

def find_trailheads(matrix):
    """
    Finds all positions with height 0 in the matrix.

    Args:
        matrix (np.array): The topographic map as a NumPy matrix.

    Returns:
        list: A list of positions (tuples) with height 0.
    """
    trailheads = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_position(matrix, position):
    """
    Checks if a position is valid (within bounds) and not impassable.

    Args:
        matrix (np.array): The topographic map as a NumPy matrix.
        position (tuple): The position to check.

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    i, j = position
    return 0 <= i < matrix.shape[0] and 0 <= j < matrix.shape[1] and matrix[i, j] != -1

def find_hiking_trails(matrix, trailhead):
    """
    Finds all valid hiking trails starting from a given trailhead.

    Args:
        matrix (np.array): The topographic map as a NumPy matrix.
        trailhead (tuple): The starting position of the hiking trail.

    Returns:
        int: The score of the trailhead (number of reachable positions with height 9).
    """
    score = 0
    stack = [(trailhead, 0)]  # (position, current height)
    visited = set()

    while stack:
        (i, j), height = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if matrix[i, j] == 9:
            score += 1
            continue

        # Check all four possible moves (up, down, left, right)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if is_valid_position(matrix, (ni, nj)) and matrix[ni, nj] == height + 1:
                stack.append(((ni, nj), height + 1))

    return score

def calculate_total_score(filename):
    """
    Calculates the total score of all trailheads on the topographic map.

    Args:
        filename (str): The name of the input file.

    Returns:
        int: The total score of all trailheads.
    """
    matrix = read_input(filename)
    trailheads = find_trailheads(matrix)
    total_score = sum(find_hiking_trails(matrix, trailhead) for trailhead in trailheads)
    return total_score

def main():
    total_score = calculate_total_score('input1.txt')
    print(f'The sum of the scores of all trailheads is: {total_score}')

if __name__ == "__main__":
    main()
