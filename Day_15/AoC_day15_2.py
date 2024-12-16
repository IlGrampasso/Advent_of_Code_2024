import numpy as np

# Read the input file and split it into lines
with open('input1.txt') as f:
    lines = f.readlines()

# Find the index of the newline separating the map and instructions
newline_idx = lines.index('\n')

# Define a tile mapping for converting characters to grid elements
tilemap = {'.': ['.','.'], '@': ['@','.'], 'O': ['[',']'], '#': ['#','#']}

# Convert the input lines into a grid of tiles
tiles = [
    [char for pair in (tilemap[char] for char in line.strip()) for char in pair]
    for line in lines[:newline_idx]
]

# Read the movement instructions
instructions = ''.join(line.strip() for line in lines[newline_idx+1:])
grid = np.array(tiles)  # Convert the list of tiles to a numpy array

# Find the initial position of the robot
robot = np.argwhere(grid == '@')[0]

# Map movement instructions to grid movements
movemap = {'>': [1, 0], '<': [-1, 0], 'v': [0, 1], '^': [0, -1]}
moves = [movemap[instruction] for instruction in instructions]

def get_blocks_to_move(x, y, mx, my):
    """Determine which blocks need to move for the robot to move."""
    next_tile = grid[y+my, x+mx]
    if next_tile == '#':
        return (False, [])
    elif next_tile == '.':
        return (True, [])
    elif next_tile in tilemap['O']:
        if my == 0:  # Horizontal movement
            if mx > 0:
                blocks_to_move = [[y, x+mx]]
            else:
                blocks_to_move = [[y, x+mx-1]]
            x = x + mx*2
            (can_shift, next_blocks_to_move) = get_blocks_to_move(x, y, mx, my)
            blocks_to_move.extend(next_blocks_to_move)
            return (can_shift, blocks_to_move)
        # Vertical movement
        y = y + my
        if next_tile == ']':
            x = x - 1
        blocks_to_move = [[y, x]]
        (can_shift_1, next_blocks_to_move_1) = get_blocks_to_move(x, y, mx, my)
        blocks_to_move.extend(next_blocks_to_move_1)
        if can_shift_1:
            (can_shift_2, next_blocks_to_move_2) = get_blocks_to_move(x+1, y, mx, my)
            blocks_to_move.extend(next_blocks_to_move_2)
        return (can_shift_1 and can_shift_2, blocks_to_move)

# Execute the movement instructions
for mx, my in moves:
    (can_shift, blocks_to_move) = get_blocks_to_move(robot[1], robot[0], mx, my)
    if not can_shift:
        continue
    for by, bx in blocks_to_move:
        grid[by, bx] = '.'
        grid[by, bx+1] = '.'
    for by, bx in blocks_to_move:
        grid[by+my, bx+mx] = '['
        grid[by+my, bx+mx+1] = ']'
    grid[robot[0], robot[1]] = '.'
    robot = [robot[0]+my, robot[1]+mx]
    grid[robot[0], robot[1]] = '@'

# Find all boxes and calculate the total score
boxes = np.argwhere(grid == '[')
gps_sum = sum([100*y + x for y, x in boxes])

print("Sum of GPS coordinates of the boxes:", gps_sum)