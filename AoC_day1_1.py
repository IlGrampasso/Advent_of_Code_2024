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

total_difference = 0
for i in range(len(array1)):
    difference = abs(array1[i] - array2[i])  # Calculate the absolute difference
    total_difference += difference  # Sum the differences
    print(f"Difference for element {i+1}:", difference)  # Print the difference for each element

print("\nTotal difference:", total_difference)  # Print the total difference
