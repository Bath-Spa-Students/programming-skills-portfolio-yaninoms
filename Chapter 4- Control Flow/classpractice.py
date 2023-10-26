# Class practice for exercise 4

# Final Grade results

# enter grade
'''grade = float(input("Enter Final Grade:"))

# result conditions
result = "You have failed."
if grade > 80:
    result = ("You have passed!")
else:
    result =  ("You have failed.")
print(f"\nFinal Grade: {grade}\n{result}")


# Visa approval

# Enter requirements
earning = int(input("\nEnter your earning per year:"))
reason = str(input("Enter your reason of travel:"))

# conditions
if earning >= 40000: 
    if reason == "business" or reason == "pleasure":
        print("VISA APPROVED !")
    else:
       print("VISA DISAPPROVED: Sorry your reason of travel is not approved.")
else:
   print("VISA DISAPPROVED: Your earning is less than required.")'''


   
   
print("Simple arithmetic calculator")
print('''Addition : 1
         Subtraction: 2
         Multiplication: 3
         Division: 4''')

oper = input(print("Choose Operator:"))
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if oper == "1":
    result = num1 + num2
    operation = "addition"
elif oper == "2":
    result = num1 - num2
    operation = "subtraction"
elif oper == "3":
    result = num1*num2
    operation = "multiplication"
elif oper == "4":
    if num2 == 0:
        print("Invalid")
    else:
        result = num1 / num2
        operation = "division"
else:
    if oper != "4":
        print(f"The chosen operator is {oper} result: {result}.")
    else:
        print("Invalid")









