import re

def process_line(line):
    # Define the regex pattern to match mul(<number1>,<number2>)
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Find all matches in the line
    matches = re.findall(pattern, line)
    
    # Calculate the sum of the products
    total = 0
    for match in matches:
        print(match)
        num1 = int(match[0])
        num2 = int(match[1])
        total += num1 * num2
    
    return total

# Open the file and read the lines
with open("input1.txt", "r") as file:
    lines = file.readlines()

# Process each line and sum the results
total_sum = 0
for line in lines:
    total_sum += process_line(line.strip())

print("Total sum:", total_sum)
