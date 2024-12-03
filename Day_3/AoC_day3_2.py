import re


def process_line(line, dont_active):
    # Precompile the regex patterns
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    dont_pattern = re.compile(r"don\'t\(\)")
    do_pattern = re.compile(r'do\(\)')

    total = 0

    # Find all instances of mul(), don't(), and do()
    tokens = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", line)

    for token in tokens:
        if dont_pattern.match(token):
            dont_active = True
        elif do_pattern.match(token):
            dont_active = False
        elif pattern.match(token) and not dont_active:
            match = pattern.match(token)
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            total += num1 * num2
            print(token)

    return total, dont_active


# Open the file and read the lines
with open("input1.txt", "r") as file:
    lines = file.readlines()

total_sum = 0
dont_active = False

# Process each line and sum the results
for line in lines:
    line_total, dont_active = process_line(line.strip(), dont_active)
    total_sum += line_total

print("Total sum:", total_sum)
