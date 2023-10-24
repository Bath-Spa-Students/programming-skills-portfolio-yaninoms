## Exercise 5: USB Shopper 
'''A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.'''

# The Constants
usb_price = 6
total_budget = 50

# Computing how many she can buy
usb_sticks_bought = total_budget // usb_price 

# Computing the change
change = total_budget % usb_price

print(f"She can buy {usb_sticks_bought} and have {change} pounds left.")
