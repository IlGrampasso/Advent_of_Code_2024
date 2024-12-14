import sys
import time
import os

# Dimensions of the grid
width = 101
height = 103
print_interval = 10

# Read input data from file
with open(sys.argv[1] if len(sys.argv) > 1 else 'input1.txt') as f:
    robots = [tuple(tuple(int(n) for n in coord[2:].split(',')) for coord in robot.split()) for robot in
              f.read().splitlines()]

# List to store safety factors for each time t
safety_factors = []

# Simulate the movement of robots for each time t
for current_time in range(max(width, height)):
    quadrants = [0, 0, 0, 0]  # Quadrant counts
    locations = set()
    for ((pos_x, pos_y), (vel_x, vel_y)) in robots:
        x = (pos_x + vel_x * current_time) % width
        y = (pos_y + vel_y * current_time) % height
        locations.add((x, y))
        if x != width // 2 and y != height // 2:
            x = x // (width // 2 + 1)
            y = y // (height // 2 + 1)
            quadrants[y * 2 + x] += 1
    safety_factor = 1
    for quadrant in quadrants:
        safety_factor *= quadrant
    safety_factors.append((safety_factor, current_time, quadrants))

    # Print the output every print_interval iterations
    if current_time % print_interval == 0:
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the current configuration
        for y in range(height):
            line = ''.join('#' if (x, y) in locations else ' ' for x in range(width))
            print(line)

        # Introduce a short delay to visualize the progression
        time.sleep(0.75)

# Determine the best time tx and ty
for _, current_time, quadrants in sorted(safety_factors)[:2]:
    if quadrants[0] > len(robots) // 4 < quadrants[2] or quadrants[1] > len(robots) // 4 < quadrants[3]:
        best_time_x = current_time
    else:
        best_time_y = current_time

# Calculate synchronized_time using the Chinese Remainder Theorem
synchronized_time = best_time_x + (pow(width, -1, height) * (best_time_y - best_time_x) % height) * width

# Find the final positions of robots at synchronized_time
locations = set()
for ((pos_x, pos_y), (vel_x, vel_y)) in robots:
    x = (pos_x + vel_x * synchronized_time) % width
    y = (pos_y + vel_y * synchronized_time) % height
    locations.add((x, y))

# Print the final configuration
print('\n'.join(''.join('#' if (x, y) in locations else ' ' for x in range(width)) for y in range(height)))

# Print the safety factor at 100 seconds and the calculated synchronized_time
print("Number of seconds to display the Easter egg:", synchronized_time)
