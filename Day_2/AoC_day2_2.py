def check_conditions_with_removal(line):
    # Convert the line of numbers into a list of integers
    numbers = list(map(int, line.split()))

    # Funzione per verificare se una lista soddisfa le condizioni
    def satisfies_conditions(nums):
        is_ascending = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
        is_descending = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))
        correct_difference = all(1 <= abs(nums[i] - nums[i + 1]) <= 3 for i in range(len(nums) - 1))
        return (is_ascending or is_descending) and correct_difference

    # Verifica se la lista originale soddisfa le condizioni
    if satisfies_conditions(numbers):
        return True

    # Verifica se rimuovendo un numero la lista soddisfa le condizioni
    for i in range(len(numbers)):
        modified_numbers = numbers[:i] + numbers[i + 1:]
        if satisfies_conditions(modified_numbers):
            return True

    return False


# Open the file and read the lines
with open("input1.txt", "r") as file:
    lines = file.readlines()

safe_reports_count = 0
# Check each line
for i, line in enumerate(lines):
    if check_conditions_with_removal(line.strip()):
        safe_reports_count += 1
        print(f"Line {i + 1}: Conditions satisfied")
    else:
        print(f"Line {i + 1}: Conditions not satisfied")

print(f"Number of safe reports:", safe_reports_count)
