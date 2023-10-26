## Exercise 1: Pizza Toppings 

'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.'''

# The propmts for inputing 
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

# condition
while True:
    topping = input(prompt)
    # if topping is not quit this statement will print
    if topping != 'quit':
        print (f"I'll add {topping} to your pizza.")
        # or else it will stop
    else:
        break

