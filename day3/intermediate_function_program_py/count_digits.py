"""
This program finds the number of digits in a given positive integer.
It uses a simple loop to count the digits.
"""

# Get input from user
number = int(input("Enter a positive integer: "))

# Function to count digits
def count_digits(number):
    if number == 0:
        return 0  # 0 has 1 digit
    count = 0
    while number > 0:
        number = number // 10  # Remove last digit
        count += 1
    return count

# Print the result
print("The number of digits is:", count_digits(number))