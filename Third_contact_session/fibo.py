# Function to generate a Fibonacci sequence up to a specified maximum value.
def generate_fibonacci(max_value):
    # Initialize an empty list to store the Fibonacci sequence.
    fib_sequence = []

    # Initialize variables for the first two Fibonacci numbers.
    a, b = 0, 1

    # Continue generating Fibonacci numbers while 'a' is less than or equal to the specified maximum value.
    while a <= max_value:
        # Append the current Fibonacci number 'a' to the sequence.
        fib_sequence.append(a)
        # 'n' variable keeps track of 'a'
        n = a
        # Update 'a' and 'b' to the next Fibonacci numbers in the sequence.
        a, b = b, a + b
    # Check if max value was found in the sequence
    if a != max_value:
        print(f"{max_value} is not in the sequence, {n} is the closest number to it")
    else:
        print("Found it!")
    # Convert the list of Fibonacci numbers to a comma-separated string and return it.
    return ', '.join(map(str, fib_sequence))

# Main function for user interaction.
def main():
    while True:
        try:
            # Prompt the user to input the maximum value for the Fibonacci sequence.
            max_value = int(input("Enter the maximum number: "))

            # Break the loop if the input is a valid integer.
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate and print the Fibonacci sequence up to the specified maximum value.
    print(generate_fibonacci(max_value))

# Execute the main function when the script is run.
if __name__ == "__main__":
    main()