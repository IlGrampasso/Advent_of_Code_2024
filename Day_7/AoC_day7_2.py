from itertools import product

<<<<<<< HEAD
def evaluate_expression(nums, ops):
    """
    Evaluates the expression formed by combining the numbers in `nums` with the operators in `ops`.

    Args:
        nums (list of int): List of numbers.
        ops (list of str): List of operators, where each operator is either '+', '*' or '||'.

    Returns:
        int: The result of evaluating the expression.
    """
    result = str(nums[0])  # Initialize result as a string to handle concatenation
    for i in range(1, len(nums)):
        if ops[i - 1] == '+':
            result = str(int(result) + nums[i])  # Addition operation
        elif ops[i - 1] == '*':
            result = str(int(result) * nums[i])  # Multiplication operation
        elif ops[i - 1] == '||':
            result = result + str(nums[i])  # Concatenation operation
    return int(result)  # Convert the result back to an integer

def check_equation(test_value, numbers):
    """
    Checks if there is any combination of '+', '*' and '||' operators that can combine `numbers` to equal `test_value`.

    Args:
        test_value (int): The value to be checked against.
        numbers (list of int): List of numbers to be combined.

    Returns:
        bool: True if a combination of operators can produce `test_value`, otherwise False.
    """
=======

def evaluate_expression(nums, ops):
    result = str(nums[0])
    for i in range(1, len(nums)):
        if ops[i - 1] == '+':
            result = str(int(result) + nums[i])
        elif ops[i - 1] == '*':
            result = str(int(result) * nums[i])
        elif ops[i - 1] == '||':
            result = result + str(nums[i])
    return int(result)


def check_equation(test_value, numbers):
>>>>>>> 98ff617fcb5df7ffd0791289febfeefed6593b03
    operators = ['+', '*', '||']
    for ops in product(operators, repeat=len(numbers) - 1):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False

<<<<<<< HEAD
def read_input(filename):
    """
    Reads the input from a file and returns a list of equations.

    Args:
        filename (str): The name of the file containing the input.

    Returns:
        list of str: List of equations as strings.
    """
=======

def read_input(filename):
>>>>>>> 98ff617fcb5df7ffd0791289febfeefed6593b03
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

<<<<<<< HEAD
def main():
    """
    Main function that reads the input, checks which equations can be solved,
    and calculates the total calibration result.
    """
=======

def main():
>>>>>>> 98ff617fcb5df7ffd0791289febfeefed6593b03
    equations = read_input('input1.txt')
    total_calibration_result = 0

    for equation in equations:
        test_value, numbers = equation.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.split()))

        if check_equation(test_value, numbers):
            total_calibration_result += test_value

    print(f'Total calibration result: {total_calibration_result}')

<<<<<<< HEAD
=======

>>>>>>> 98ff617fcb5df7ffd0791289febfeefed6593b03
if __name__ == "__main__":
    main()
