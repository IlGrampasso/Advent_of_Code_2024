# Open the file and read the lines
with open("input1.txt", "r") as file:
    rows = file.readlines()

# Initialize arrays for the columns
array1 = []
array2 = []

# Populate the arrays with the values from the rows
for row in rows:
    numbers = row.split()  # Split the numbers by space
    array1.append(int(numbers[0]))  # Add the first number to the first array
    array2.append(int(numbers[1]))  # Add the second number to the second array

# Sort the arrays
array1.sort()
array2.sort()

# Print the arrays to verify
print("Array 1:", array1)
print("Array 2:", array2)

# Initialize a dictionary to count occurrences of array2 elements
occurrences = {}

for num in array2:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

# Calculate the similarity sum
similarity_sum = 0

for num in array1:
    if num in occurrences:
        similarity_sum += num * occurrences[num]

print("\nTotal sum:", similarity_sum)  # Print the total sum 
