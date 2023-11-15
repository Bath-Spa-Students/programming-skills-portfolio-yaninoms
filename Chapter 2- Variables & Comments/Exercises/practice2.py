## Practice Questions: Q2
'''Write a python program that takes courses marks as input and then calculates average of all the courses. After calculating the average, calculate the percentage of a student using total marks. Assume the total of all the courses marks is 500 or take the total marks from the user as input. '''

# Assuming there are 3 courses that totals up to 300 marks all in all
num_courses = 3
marks_each =  300

# asking for users input
codelab = int(input("Enter your CODELAB mark (_/100):"))
computing = int(input("Enter your COMPUTING mark (_/100):"))
cybersecurity = int(input("Enter your CYBERSECURITY mark (_/100):"))

# Calculation of total, avg, and percentage
total_marks = codelab + computing + cybersecurity
avg = total_marks / 3
percentage = (total_marks / 300) * 100

# Printing the average and percentage
print(f"Average marks: {avg:.2f}") 
print(f"Percentage: {percentage:.2f}%")