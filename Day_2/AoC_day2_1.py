def check_conditions(line):
    # Convert the line of numbers into a list of integers
    numbers = list(map(int, line.split()))

    # Check if the list is entirely ascending or entirely descending
    is_ascending = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    is_descending = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    # Check the difference condition
    correct_difference = all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

    # Return True if either ascending or descending and the difference condition is satisfied
    return (is_ascending or is_descending) and correct_difference

# Open the file and read the lines
with open("input1.txt", "r") as file:
    lines = file.readlines()

safe_reports_count = 0
# Check each line
for i, line in enumerate(lines):
    if check_conditions(line.strip()):
        safe_reports_count += 1
        print(f"Line {i + 1}: Conditions satisfied")
    else:
        print(f"Line {i + 1}: Conditions not satisfied")

print(f"Number of safe reports:",   safe_reports_count)