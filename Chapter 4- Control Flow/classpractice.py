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
print(f"\nFinal Grade: {grade}\n{result}")'''


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
   print("VISA DISAPPROVED: Your earning is less than required.")



