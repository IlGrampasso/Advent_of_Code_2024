from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def move_cursor(map_matrix):
    # Define directions: North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_idx = 0  # Start facing North (initial direction)

    # Find initial cursor position
    rows, cols = len(map_matrix), len(map_matrix[0])
    cursor_pos = None
    for r in range(rows):
        for c in range(cols):
            if map_matrix[r][c] == '^':
                cursor_pos = (r, c)
                break
        if cursor_pos:
            break

    visited_count = 0

    # Mark the initial position as visited
    r, c = cursor_pos
    map_matrix[r][c] = 'X'
    visited_count += 1

    while True:
        dr, dc = directions[dir_idx]

        # Move to the next position
        next_r, next_c = r + dr, c + dc

        # Check if next position is out of bounds
        if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
            break

        # Check if next position is an obstacle
        if map_matrix[next_r][next_c] == '#':
            # Rotate 90 degrees clockwise
            dir_idx = (dir_idx + 1) % 4
        else:
            # Move cursor to the next position
            r, c = next_r, next_c
            # Mark the current position as visited
            if map_matrix[r][c] == '.':
                map_matrix[r][c] = 'X'
                visited_count += 1

    return visited_count

def read_map_from_file(filename):
    with open(filename, 'r') as file:
        map_lines = file.readlines()
    map_matrix = [list(line.strip()) for line in map_lines]
    return map_matrix

def print_colored_map(map_matrix):
    # Function to print the map with colors
    for row in map_matrix:
        colored_row = ""
        for cell in row:
            if cell == '#':
                colored_row += Fore.RED + cell
            elif cell == 'X':
                colored_row += Fore.GREEN + cell
            elif cell == '^':
                colored_row += Fore.BLUE + cell
            else:
                colored_row += cell
        print(colored_row)

# Name of the file containing the map
filename = "input1.txt"

# Read the map from the file
map_matrix = read_map_from_file(filename)

# Execute the cursor movement function on the map read from the file
result = move_cursor(map_matrix)

# Print the colored map after cursor movement
print_colored_map(map_matrix)
print(f"Number of marked areas: {result}")
