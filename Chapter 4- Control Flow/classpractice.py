# Class practice for exercise 4

grade = float(input("Enter Final Grade:"))
result = "You have failed."
if grade > 80:
    result = ("You have passed!")
else:
    result =  ("You have failed.")
print(f"\nFinal Grade: {grade},{result}")