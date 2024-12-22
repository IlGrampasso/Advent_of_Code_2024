# Read the input from the file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]


# Function to mix a value into the secret number
def mix(secret, value):
    return secret ^ value


# Function to prune the secret number
def prune(secret):
    return secret % 16777216


# Function to generate the next secret number
def generate_next_secret(secret):
    # Step 1: Multiply by 64, mix, and prune
    secret = prune(mix(secret, secret * 64))

    # Step 2: Divide by 32, mix, and prune
    secret = prune(mix(secret, secret // 32))

    # Step 3: Multiply by 2048, mix, and prune
    secret = prune(mix(secret, secret * 2048))

    return secret


# Function to simulate 2000 iterations and get the 2000th secret number
def simulate_secret_numbers(initial_secret, iterations=2000):
    secret = initial_secret
    for _ in range(iterations):
        secret = generate_next_secret(secret)
    return secret


# Main function to calculate the sum of the 2000th secret number for each buyer
def calculate_sum_of_secrets(file_path):
    initial_secrets = read_input(file_path)
    total_sum = 0

    for initial_secret in initial_secrets:
        secret_2000th = simulate_secret_numbers(initial_secret)
        total_sum += secret_2000th

    return total_sum


# Calculate and print the sum of the 2000th secret number for each buyer
file_path = 'input1.txt'
total_sum = calculate_sum_of_secrets(file_path)
print("Sum of the 2000th secret numbers:", total_sum)
