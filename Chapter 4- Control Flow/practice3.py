# Practice Question : Q3
'''. Write a python program with nested decision structures that perform the following:
 If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2'''

# assuming values
amount1 = 18
amount2 = 87

# the nested if statements
if amount1 > 10: # first if condition
    if amount2 < 100: # second nested condition
        greater_amnt = max(amount1, amount2)
        print(f"{greater_amnt} is greater.") 
        # display the greater
    else:
        print("amount2 is not less than 100.")
        # else statements
else: 
    print("amount1 is not greater than 10.")


    