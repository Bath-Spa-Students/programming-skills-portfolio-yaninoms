# Practice Question : Q2
'''Write a Python function that calculates the factorial of a given positive integer using recursion.'''

# defining tutorial 
def factorial(n):
    # if number is 1 or 0, the factorial is 1
    if n == 0 or n == 1: 
        return 1
    else:
     # For other numbers, we calculate the factorial using recursion.
        # The factorial of n is n times the factorial of (n-1).
        return n * factorial(n-1)
# assuming the number is 5  
number = 5
result = factorial(number) # calling the function

print(f"The factorial of {number} is: {result}")








