from typing import List, Tuple
from collections import defaultdict, deque

def parse_input(file_content: str) -> Tuple[List[str], List[str]]:
    # Split the file content into rules and updates sections using a blank line as the separator
    rules_section, updates_section = file_content.split('\n\n')
    # Split each section into individual lines
    rule_lines = rules_section.strip().split('\n')
    update_lines = updates_section.strip().split('\n')
    return rule_lines, update_lines

def parse_rules(rule_lines: List[str]) -> dict:
    rules = defaultdict(list)
    for line in rule_lines:
        x, y = map(int, line.split('|'))
        rules[x].append(y)
    return rules

def check_update(update: str, rules: dict) -> bool:
    pages = list(map(int, update.split(',')))
    page_indices = {page: i for i, page in enumerate(pages)}
    for x, following_pages in rules.items():
        if x in page_indices:
            for y in following_pages:
                if y in page_indices and page_indices[x] >= page_indices[y]:
                    return False
    return True

def find_middle_page(pages: List[int]) -> int:
    mid_index = len(pages) // 2
    return pages[mid_index]

def topological_sort(pages: List[int], rules: dict) -> List[int]:
    # Create a graph and an in-degree counter
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for page in pages:
        in_degree[page] = 0

    for x in pages:
        if x in rules:
            for y in rules[x]:
                if y in pages:
                    graph[x].append(y)
                    in_degree[y] += 1

    # Queue for pages with no incoming edges
    zero_in_degree = deque([page for page in pages if in_degree[page] == 0])
    sorted_pages = []

    while zero_in_degree:
        page = zero_in_degree.popleft()
        sorted_pages.append(page)
        for neighbor in graph[page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return sorted_pages

# Read input from file
with open("input1.txt", "r") as file:
    file_content = file.read()

# Parse rules and updates from file content
rule_lines, update_lines = parse_input(file_content)

# Parse the rules into a dictionary
rules = parse_rules(rule_lines)

# Check each update, reorder if necessary, and calculate the sum of middle pages
incorrect_updates = []
for update in update_lines:
    if not check_update(update, rules):
        pages = list(map(int, update.split(',')))
        sorted_pages = topological_sort(pages, rules)
        incorrect_updates.append(find_middle_page(sorted_pages))

total_sum = sum(incorrect_updates)
print(f"Sum of middle pages of corrected updates: {total_sum}")
