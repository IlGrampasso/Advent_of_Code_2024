from pathlib import Path


# Function to read the input from the file
def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')

    patterns = lines[0].split(', ')
    designs = lines[2:]
    return patterns, designs


# Function to check if a design can be constructed using the available patterns
def can_construct(design, patterns):
    dp = [False] * (len(design) + 1)
    dp[0] = True

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and dp[i - len(pattern)] and design[i - len(pattern):i] == pattern:
                dp[i] = True
                break

    return dp[len(design)]


# Main function to solve the problem
def count_possible_designs(file_path):
    patterns, designs = read_input(file_path)
    count = 0

    for design in designs:
        if can_construct(design, patterns):
            count += 1

    return count


# Read the input and count possible designs
file_path = 'input1.txt'
possible_designs_count = count_possible_designs(file_path)
print("Number of possible designs:", possible_designs_count)
