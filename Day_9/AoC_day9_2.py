import numpy as np


def read_input(filename):
    """
    Reads the input disk map from a file and returns it as an array of integers.

    Args:
        filename (str): The name of the input file.

    Returns:
        np.array: The disk map as an array of integers.
    """
    with open("input1.txt", 'r') as file:
        blocks = np.array([int(z) for z in file.read().strip()])
    return blocks


def initialize_memory(blocks):
    """
    Initializes memory and assigns file IDs and free space.

    Args:
        blocks (np.array): The array of integers representing the disk map.

    Returns:
        tuple: A tuple containing the memory array, file locations, and space locations.
    """
    locs = np.cumsum(blocks)  # Get the starting address of each block
    locs = np.insert(locs, 0, 0)

    # Addresses of spaces
    spaces = [np.arange(locs[i], locs[i + 1]) for i in range(1, len(locs) - 1, 2)]
    space_lens = blocks[1::2]  # Lengths of empty memory chunks

    # Addresses of files starting from the right
    files = [np.arange(locs[i], locs[i + 1]) for i in range(len(locs) - 2, 0, -2)]
    file_lens = [len(f) for f in files]  # File lengths

    # Initialize memory with file IDs and free space (-1)
    mem = np.zeros(np.sum(blocks), dtype=np.int16)
    for ind in range(0, len(locs), 2):
        val = ind // 2
        for l in range(locs[ind], locs[ind + 1]):
            mem[l] = val

    return mem, files, file_lens, spaces, space_lens


def move_files(mem, files, file_lens, spaces, space_lens):
    """
    Moves whole files to the leftmost span of free space blocks that could fit the file.

    Args:
        mem (np.array): The array representing the disk with file IDs and free spaces.
        files (list): The list of file locations.
        file_lens (list): The list of file lengths.
        spaces (list): The list of space locations.
        space_lens (list): The list of space lengths.

    Returns:
        np.array: The modified memory after moving the files.
    """
    file_num, space_num = len(files), len(spaces)

    for j in range(file_num):  # Loop through the files
        # Get the leftmost valid space that can fit the file
        valids = [i for i in range(space_num) if file_lens[j] <= space_lens[i] and spaces[i][-1] < files[j][0]]
        if len(valids) > 0:  # If such a space exists
            space = min(valids)  # Get the leftmost one
            # Only select the needed sub-portion of space
            spaces_put = spaces[space][:file_lens[j]]
            # Update free space left
            spaces[space] = spaces[space][file_lens[j]:]
            space_lens[space] -= file_lens[j]  # Update the length of this chunk of space
            mem[spaces_put] = mem[files[j]]  # Copy the file
            mem[files[j]] = -1  # Mark the old position as free space

    return mem


def calculate_checksum(mem):
    """
    Calculates the checksum of the modified memory.

    Args:
        mem (np.array): The modified memory.

    Returns:
        int: The checksum value.
    """
    checksum = np.sum(mem[mem != -1] * np.arange(len(mem))[mem != -1])
    return checksum


def main():
    # Read the input disk map from the file
    blocks = read_input('input1.txt')

    # Initialize memory and parse the disk map
    mem, files, file_lens, spaces, space_lens = initialize_memory(blocks)

    # Move whole files to the leftmost span of free space blocks
    mem = move_files(mem, files, file_lens, spaces, space_lens)

    # Calculate the checksum of the modified memory
    checksum = calculate_checksum(mem)

    # Print the final checksum result
    print(f'The resulting filesystem checksum is: {checksum}')


if __name__ == "__main__":
    main()
