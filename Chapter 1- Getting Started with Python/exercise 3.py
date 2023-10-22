## Exercise 3: Print date and Time
'''Write a Python program to display the current date and time.'''

# Import the datetime module
import datetime  

# Get the current date and time
now = datetime.datetime.now()

# Print a message indicating the output
print("Current date and time:")

# Print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))
