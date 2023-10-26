# Exercise 2: Movie Tickets

'''A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket'''

# the prompts to enter age or 'quit'
prompt = "\nHow old are you ?"
prompt += "\nEnter 'quit' when you are finished: "

#condition
while True:
    age = input(prompt)
    # convert age as string to integer
    age = int(age)

    # condition and the printed price per age
    if age < 3:
        print("Your movie ticket is FREE.")
    elif 3 <= age <= 12:
        print("Ticket Cost: $10.00")
    else:
        if age > 12:
             print("Ticket Cost: $15.00")
    # break command       
    if age == 'quit':
        break

