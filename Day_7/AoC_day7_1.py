from itertools import product


def evaluate_expression(nums, ops):
    result = nums[0]
    for i in range(1, len(nums)):
        if ops[i - 1] == '+':
            result += nums[i]
        elif ops[i - 1] == '*':
            result *= nums[i]
    return result


def check_equation(test_value, numbers):
    operators = ['+', '*']
    for ops in product(operators, repeat=len(numbers) - 1):
        if evaluate_expression(numbers, ops) == test_value:
            return True
    return False


def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def main():
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
