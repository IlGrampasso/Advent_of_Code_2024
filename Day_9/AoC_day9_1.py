import numpy as np

# Read the input file and create an array of integers representing the blocks.
blocks = np.array([int(z) for z in open('input1.txt').read()])

# Calculate the cumulative sum to determine the positions (locations) in memory.
locs = np.cumsum(blocks)
# Insert a zero at the beginning to handle the starting position.
locs = np.insert(locs, 0, 0)

# Initialize the memory with -1 to indicate free spaces.
mem = np.array([-1] * np.sum(blocks))

# Assign file IDs to the memory based on the parsed blocks.
for ind in range(0, len(locs), 2):
    val = ind // 2
    for l in range(locs[ind], locs[ind + 1]):
        mem[l] = val

# Find the positions of the free spaces (indicated by -1).
spaces = np.nonzero(mem == -1)[0]
# Find the file IDs to be moved into the free spaces, starting from the end of the memory.
vals = np.flip(np.nonzero(mem != -1)[0][-len(spaces):])
# Move the file IDs into the free spaces.
mem[spaces] = mem[vals]

# Calculate and print the checksum by summing the product of the positions and file IDs.
print(np.sum(mem[:-len(spaces)] * np.arange(0, len(mem) - len(spaces))))
