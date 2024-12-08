from collections import defaultdict
from itertools import combinations, count


def read_input(filename):
    """
    Reads the input map from a file and returns a list of strings.
    """
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def get_antennas_positions(map):
    """
    Identifies and returns the positions and frequencies of all antennas in the map.
    """
    antennas = defaultdict(list)
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char != '.':
                antennas[char].append((x, y))
    return antennas


def calculate_antinode_positions(pos1, pos2, bounds, is_part1):
    """
    Calculate the possible antinode positions for a given pair of antennas.
    """
    x1, y1 = pos1
    x2, y2 = pos2

    dx = x1 - x2
    dy = y1 - y2

    antinodes = set()

    for i in count(1):
        nx, ny = x1 + i * dx, y1 + i * dy
        mx, my = x2 - i * dx, y2 - i * dy

        added = False
        if 0 <= nx < bounds and 0 <= ny < bounds:
            antinodes.add((nx, ny))
            added = True
        if 0 <= mx < bounds and 0 <= my < bounds:
            antinodes.add((mx, my))
            added = True

        if is_part1 or not added:
            break

    return antinodes


def count_unique_antinodes(map):
    """
    Counts the number of unique positions within the map that contain an antinode.
    """
    antennas = get_antennas_positions(map)
    all_locations = set.union(*[set(x) for x in antennas.values()])
    bounds = len(map)

    # Iterate for both parts of the problem
    results = []
    for is_part1 in [True, False]:
        antinodes = set()
        for locations in antennas.values():
            for (xa, ya), (xb, yb) in combinations(locations, 2):
                antinodes.update(calculate_antinode_positions((xa, ya), (xb, yb), bounds, is_part1))

        if is_part1:
            results.append(len(antinodes))
        else:
            results.append(len(antinodes | all_locations))

    return results


def main():
    map = read_input('input1.txt')
    part1_result, part2_result = count_unique_antinodes(map)
    print(f'Number of unique locations containing an antinode (Part 1): {part1_result}')
    print(f'Number of unique locations containing an antinode (Part 2): {part2_result}')


if __name__ == "__main__":
    main()
