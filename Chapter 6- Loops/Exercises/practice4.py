# Practice Question : Q4
'''Write a Python program that uses the break statement to exit a for loop when a specific condition is met.'''

print("The code will break when it reaches 5.")

# for loop 
for num in range(1, 11): # set range from 1 to 10
    print(num) # print
    if num == 5:
         print("The condition is met. break.")
         break
        

