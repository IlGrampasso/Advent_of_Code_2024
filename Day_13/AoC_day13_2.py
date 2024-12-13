import re


def read_input(filename):
    """
    Reads the input claw machine configurations and prize locations from a file.

    Args:
        filename (str): The name of the input file.

    Returns:
        list: A list of strings, each representing a claw machine's configuration.
    """
    with open(filename, 'r') as file:
        input_data = file.read().split('\n\n')
    return input_data


def calculate_min_tokens(input_data):
    """
    Calculates the minimum number of tokens required to win all possible prizes.

    Args:
        input_data (list): A list of strings, each representing a claw machine's configuration.

    Returns:
        int: The total minimum number of tokens required to win all possible prizes.
    """
    total = 0

    for case in input_data:
        # Extract numbers from the configuration using regex
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", case))

        # Adjust the prize location by adding 10000000000000 to both X and Y coordinates
        px += 10000000000000
        py += 10000000000000

        # Solve for 'a' (nearest integer)
        a = round((py / by - px / bx) / (ay / by - ax / bx))

        # Back-solve for 'b' (nearest integer)
        b = round((px - a * ax) / bx)

        # Verify the result (ensuring the solution's validity)
        if (a * ax + b * bx == px and a * ay + b * by == py):
            total += 3 * a + b

    return total


def main():
    # Read the input claw machine configurations and prize locations from the file
    input_data = read_input('input1.txt')

    # Calculate the minimum tokens required to win all possible prizes
    total_tokens = calculate_min_tokens(input_data)

    # Print the total number of tokens used
    print(f'The total number of tokens used is: {total_tokens}')


if __name__ == "__main__":
    main()
