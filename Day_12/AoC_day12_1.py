def read_garden_from_file(filename):
    # Opens the file with the given filename and reads its content line by line.
    # Each line is stripped of leading/trailing whitespace and converted into a list of characters.
    # The resulting list of lists (garden) is returned.
    with open(filename, 'r') as file:
        garden = [list(line.strip()) for line in file.readlines()]
    return garden

def get_garden_details(garden):
    rows = len(garden)  # Number of rows in the garden
    cols = len(garden[0])  # Number of columns in the garden
    visited = [[False for _ in range(cols)] for _ in range(rows)]  # Matrix to keep track of visited cells

    def dfs(x, y):
        stack = [(x, y)]  # Stack for Depth-First Search (DFS)
        region_cells = []  # List to store cells belonging to the current region
        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True  # Mark the cell as visited
            region_cells.append((cx, cy))  # Add the cell to the region
            # Explore the neighboring cells (up, down, left, right)
            for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                if 0 <= nx < rows and 0 <= ny < cols and garden[nx][ny] == garden[cx][cy] and not visited[nx][ny]:
                    stack.append((nx, ny))
        return region_cells

    def calculate_area_perimeter(region_cells):
        area = len(region_cells)  # Area is the number of cells in the region
        perimeter = 0  # Initialize perimeter
        for x, y in region_cells:
            # Check each neighboring cell (up, down, left, right)
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or garden[nx][ny] != garden[x][y]:
                    perimeter += 1  # Increase perimeter if the neighboring cell is out of bounds or different
        return area, perimeter

    regions = []  # List to store details of all regions
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                region_cells = dfs(i, j)  # Find all cells in the current region
                area, perimeter = calculate_area_perimeter(region_cells)  # Calculate area and perimeter
                regions.append((garden[i][j], area, perimeter))  # Append region details to the list

    return regions

def calculate_fence_price(garden):
    regions = get_garden_details(garden)  # Get details of all regions
    total_price = 0
    for plant, area, perimeter in regions:
        total_price += area * perimeter  # Calculate the price for the region and add to total price
    return total_price

# Read the garden from the input file
garden = read_garden_from_file('input1.txt')

# Calculate and print the total price of the fence
print("Total fence price:", calculate_fence_price(garden))
