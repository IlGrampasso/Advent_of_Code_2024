from collections import defaultdict

def process_input(filename):
    """
    Reads the input numbers engraved on stones from a file and returns them as a defaultdict of integer counts.

    Args:
        filename (str): The name of the input file.

    Returns:
        defaultdict: A dictionary with the numbers engraved on the stones as keys and their counts as values.
    """
    with open(filename) as file:
        input_data = file.read().splitlines()

    stones = defaultdict(int)
    for stone in input_data[0].split():
        stone = int(stone)
        stones[stone] += 1

    return stones

def blink_times(blinks):
    """
    Simulates the transformation of stones for the given number of blinks.

    Args:
        blinks (int): The number of blinks to simulate.
    """
    for i in range(blinks):
        blink()
        print(i, len(stones))
    return

def blink():
    """
    Transforms the stones according to the specified rules.
    """
    stonework = dict(stones)
    for stone, count in stonework.items():
        if count == 0:
            continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            stone_1 = int(stone_str[:mid])
            stone_2 = int(stone_str[mid:])
            stones[stone_1] += count
            stones[stone_2] += count
            stones[stone] -= count
        else:
            stones[stone * 2024] += count
            stones[stone] -= count
    return

def main():
    """
    Main function to read input, simulate blinks, and print the final number of stones.
    """
    filename = 'input1.txt'

    global stones
    stones = process_input(filename)

    # Simulate the transformations for the specified number of blinks
    blink_times(75)

    # Print the number of stones after the specified number of blinks
    print()
    print('Stones =', sum(stones.values()))

if __name__ == "__main__":
    main()
