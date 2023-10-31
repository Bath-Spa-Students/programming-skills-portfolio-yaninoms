## Exercise 5: ## Exercise 5: No Pastrami 

'''Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.'''

# Creating the sandwich lsit
sandwich_orders = [
    "Club Sandwich",
    "Pastrami Sandwich",
    "Pastrami Sandwich",
    "Grilled Cheese Sandwich",
    "Egg Sandwich",
    "Pastrami Sandwich",
    "Chicken Sandwich"
    ]
# empty finished sandwich list
finished_sandwiches = []

print("Sorry, Dali has ran out of pastramis.")
while 'Pastrami Sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami Sandwich')

# While the sandwiches are running
while sandwich_orders:
    # it removes itself from sandwich_orders
    sandwich = sandwich_orders.pop()
    print(f"In progess:{sandwich}.")
    # and is transfered to finished_sandwich
    finished_sandwiches.append(sandwich)

# finally printing the final list 
print("\n")
for sandwich in finished_sandwiches:
    print(f"Finished: {sandwich}.")