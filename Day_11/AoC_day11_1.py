def read_input(filename):
    """
    Reads the input numbers engraved on stones from a file and returns them as a list of integers.

    Args:
        filename (str): The name of the input file.

    Returns:
        list of int: The numbers engraved on the stones.
    """
    with open(filename, 'r') as file:
        numbers = list(map(int, file.read().strip().split()))
    return numbers


def transform_stones(stones):
    """
    Transforms the stones according to the specified rules.

    Args:
        stones (list of int): The current arrangement of stones.

    Returns:
        list of int: The new arrangement of stones after transformation.
    """
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            # Split the stone into two new stones
            str_stone = str(stone)
            mid = len(str_stone) // 2
            left = int(str_stone[:mid])
            right = int(str_stone[mid:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            # Multiply the stone by 2024
            new_stones.append(stone * 2024)
    return new_stones


def main():
    # Read the input numbers from the file
    stones = read_input('input1.txt')

    # Simulate the transformations for 25 times
    for _ in range(25):
        stones = transform_stones(stones)

    # Print the number of stones after 25 transformations
    print(f'The number of stones after 25 blinks is: {len(stones)}')
    print(stones)

if __name__ == "__main__":
    main()
