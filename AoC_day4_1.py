def is_valid(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

def search_in_direction(matrix, word, start_x, start_y, delta_x, delta_y):
    max_x, max_y = len(matrix), len(matrix[0])
    for i in range(len(word)):
        x, y = start_x + i * delta_x, start_y + i * delta_y
        if not is_valid(x, y, max_x, max_y) or matrix[x][y] != word[i]:
            return False
    return True

def count_occurrences(matrix, word):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for delta_x, delta_y in directions:
                if search_in_direction(matrix, word, x, y, delta_x, delta_y):
                    count += 1
    return count

# Apri il file e leggi la matrice
with open("input1.txt", "r") as file:
    lines = file.readlines()

matrix = [line.strip() for line in lines]

word = "XMAS"
result = count_occurrences(matrix, word)
print(f"Total occurrences of '{word}':", result)
