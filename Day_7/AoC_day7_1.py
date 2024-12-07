from itertools import product

def evaluate_expression(nums, ops):
    """
    Evaluates the expression formed by combining the numbers in `nums` with the operators in `ops`.

    Args:
        nums (list of int): List of numbers.
        ops (list of str): List of operators, where each operator is either '+' or '*'.

    Returns:
        int: The result of evaluating the expression.
    """
    result = nums[0]
    for i in range(1, len(nums)):
        if ops[i - 1] == '+':
            result += nums[i]
        elif ops[i - 1] == '*':
            result *= nums[i]
    return result

def check_equation(test_value, numbers):
    """
    Checks if there is any combination of '+' and '*' operators that can combine `numbers` to equal `test_value`.

    Args:
        test_value (int): The value to be checked against.
        numbers (list of int): List of numbers to be combined.

    Returns:
        bool: True if a combination of operators can produce `test_value`, otherwise False.
    """
    operators = ['+', '*']
    for ops in product(operators, repeat=len(numbers) - 1):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

def read_input(filename):
    """
    Reads the input from a file and returns a list of equations.

    Args:
        filename (str): The name of the file containing the input.

    Returns:
        list of str: List of equations as strings.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def main():
    """
    Main function that reads the input, checks which equations can be solved,
    and calculates the total calibration result.
    """
    equations = read_input('input1.txt')
    total_calibration_result = 0

    for equation in equations:
        test_value, numbers = equation.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.split()))

        if check_equation(test_value, numbers):
            total_calibration_result += test_value

    print(f'Total calibration result: {total_calibration_result}')

if __name__ == "__main__":
    main()