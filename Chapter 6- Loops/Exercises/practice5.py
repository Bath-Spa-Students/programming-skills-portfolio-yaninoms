# Practice Question : Q5
'''Write a Python program that uses a while loop to find the largest number among a series of user-input values until they enter '0' to exit the loop.'''

largest_num = float('-inf')

while True:
    user_input = float(input("Enter a number (enter 0 to end):"))

    if user_input == 0:
        break

    largest_num = max(largest_num, user_input)

print(f"The largest number is: {largest_num}")

