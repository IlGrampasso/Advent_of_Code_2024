from time import time

keys = []
locks = []

def parse_input(raw: str) -> int:
    items = keys if raw[0] == "." else locks
    item = []
    lines = raw.split("\n")
    for i in range(len(lines[0])):
        item.append(sum(1 if line[i] == "#" else 0 for line in lines) - 1)
    items.append(item)
    return len(lines) - 2

def count_matching_pairs():
    matching = 0
    for key in keys:
        for lock in locks:
            for k, l in zip(key, lock):
                if k + l > available_space:
                    break
            else:
                matching += 1
    return matching

# Start timing
t = time()

# Load input file
file_path = 'input1.txt'
with open(file_path) as file:
    data = file.read().split("\n\n")

# Parse input data
for raw in data:
    available_space = parse_input(raw.strip())

# Count matching pairs
matching_pairs = count_matching_pairs()
print("Number of matching pairs:", matching_pairs)

# Print elapsed time
print("Elapsed time:", time() - t)
