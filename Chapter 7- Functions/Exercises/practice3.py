# Practice Question : Q3
'''Write a Python program that uses a function to check if a given number is prime or not.'''

# defining a function
def is_prime(number):
    if number <= 1: # if number is less than or equal to 1, then false
        return False
    for i in range(2, int(number**0.5)+1): # check for divisors from 2 up to the square root of num
        if number % i == 0: # if divisible by any of these then not a prime
            return False
        # else it is prime
    return True

# assuming the number
number = 7
# calling the function in an if else statement
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


