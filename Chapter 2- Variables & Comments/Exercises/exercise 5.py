## Exercise 5: USB Shopper 

# The Constants
usb_price = 6
total_budget = 50

# Computing how many she can buy
usb_sticks_bought = total_budget // usb_price 

# Computing the change
change = total_budget % usb_price

print(f"She can buy {usb_sticks_bought} and have {change} pounds left.")
