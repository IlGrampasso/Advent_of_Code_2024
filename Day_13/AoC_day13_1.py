import numpy as np
from itertools import product
from math import isclose


def read_input(filename):
    """
    Reads the input claw machine configurations and prize locations from a file.

    Args:
        filename (str): The name of the input file.

    Returns:
        list: A list of dictionaries containing the configurations and prize locations.
    """
    machines = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    for i in range(0, len(lines), 4):
        machine = {
            'A': (int(lines[i].split()[2][2:].replace(',', '')), int(lines[i].split()[3][2:].replace(',', ''))),
            'B': (int(lines[i + 1].split()[2][2:].replace(',', '')), int(lines[i + 1].split()[3][2:].replace(',', ''))),
            'prize': (
            int(lines[i + 2].split()[1][2:].replace(',', '')), int(lines[i + 2].split()[2][2:].replace(',', '')))
        }
        machines.append(machine)
    return machines


def min_tokens_to_win(machine, max_presses=100):
    """
    Calculates the minimum number of tokens required to win a prize for a single machine.

    Args:
        machine (dict): The configuration and prize location for the machine.
        max_presses (int): The maximum number of button presses to consider.

    Returns:
        int: The minimum number of tokens required to win the prize, or None if not possible.
    """
    A, B = machine['A'], machine['B']
    prize = machine['prize']

    for a_presses in range(max_presses + 1):
        for b_presses in range(max_presses + 1):
            x = a_presses * A[0] + b_presses * B[0]
            y = a_presses * A[1] + b_presses * B[1]
            if x == prize[0] and y == prize[1]:
                return a_presses * 3 + b_presses
    return None


def main():
    """
    Main function to read input, simulate blinks, and print the final number of stones.
    """
    # Read the input claw machine configurations and prize locations from the file
    machines = read_input('input1.txt')

    total_tokens = 0
    prizes_won = 0

    # Calculate the minimum tokens required for each machine
    for machine in machines:
        tokens = min_tokens_to_win(machine)
        if tokens is not None:
            total_tokens += tokens
            prizes_won += 1

    # Print the number of prizes won and the total number of tokens used
    print(f'The number of prizes won is: {prizes_won}')
    print(f'The total number of tokens used is: {total_tokens}')


if __name__ == "__main__":
    main()
