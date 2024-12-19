from pathlib import Path


# Function to read the input from the file
def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')

    patterns = lines[0].split(', ')
    designs = lines[2:]
    return patterns, designs


# Function to count all ways a design can be constructed using the available patterns
def count_ways_to_construct(design, patterns):
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # There's one way to construct an empty design

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[len(design)]


# Main function to solve the problem
def sum_of_all_ways(file_path):
    patterns, designs = read_input(file_path)
    total_ways = 0

    for design in designs:
        total_ways += count_ways_to_construct(design, patterns)

    return total_ways


# Read the input and sum all ways to construct each design
file_path = 'input1.txt'
total_ways = sum_of_all_ways(file_path)
print("Total number of ways to construct all designs:", total_ways)
