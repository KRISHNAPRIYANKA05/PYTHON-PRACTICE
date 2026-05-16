""" in this program er are going to write
the code for  finging  whether the given nuber is prime number 
or not in both local and global variables."""

#global variable
# Global variable example
is_prime_global = False

def check_prime(number):
    # Local variables
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Usage
num = int(input("Enter a number: "))
is_prime_global = check_prime(num)  # Assign to global
print(f"Is {num} prime? {is_prime_global}")
