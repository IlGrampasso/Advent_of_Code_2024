def parse_input(file_content):
    # Split the file content into rules and updates sections using a blank line as the separator
    rules_section, updates_section = file_content.split('\n\n')
    # Split each section into individual lines
    rule_lines = rules_section.strip().split('\n')
    update_lines = updates_section.strip().split('\n')
    return rule_lines, update_lines

def parse_rules(rule_lines):
    rules = {}
    for line in rule_lines:
        # Split each rule line into two integers X and Y
        x, y = map(int, line.split('|'))
        # Add the rule to the dictionary, where X is the key and Y is added to its list of values
        if x not in rules:
            rules[x] = []
        rules[x].append(y)
    return rules

def check_update(update, rules):
    # Convert the update string into a list of integers
    pages = list(map(int, update.split(',')))
    # Create a dictionary to store the index of each page in the list
    page_indices = {page: i for i, page in enumerate(pages)}
    for x, following_pages in rules.items():
        if x in page_indices:
            # Check each rule for page X, ensuring X comes before Y if both are in the update
            for y in following_pages:
                if y in page_indices and page_indices[x] >= page_indices[y]:
                    return False
    return True

def find_middle_page(pages):
    # Find the middle index of the pages list
    mid_index = len(pages) // 2
    return pages[mid_index]

# Read input from file
with open("input1.txt", "r") as file:
    file_content = file.read()

# Parse rules and updates from file content
rule_lines, update_lines = parse_input(file_content)

# Parse the rules into a dictionary
rules = parse_rules(rule_lines)

# Check each update and calculate the sum of middle pages
correct_updates = []
for update in update_lines:
    if check_update(update, rules):
        # Convert the update string into a list of integers
        pages = list(map(int, update.split(',')))
        # Add the middle page of the correctly-ordered update to the list
        correct_updates.append(find_middle_page(pages))

# Calculate the total sum of the middle pages
total_sum = sum(correct_updates)
print(f"Sum of middle pages of correct updates: {total_sum}")