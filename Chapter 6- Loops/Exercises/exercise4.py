## Exercise 4: Deli :ballot_box_with_check:

'''Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''

# Creating the sandwich lsit
sandwich_orders = [
    "Club Sandwich",
    "Grilled Cheese Sandwich",
    "Egg Sandwich",
    "Ham Sandwich",
    "Chicken Sandwich"
    ]
# empty finished sandwich list
finished_sandwiches = []

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



