## Exercise 5: Pets 

'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet'''

# listing the pets and their owners
pets = [
    {"kind":"Dog","owner": "Alekz"},
    {"kind":"Cat","owner": "Sam"},
    {"kind":"Cat","owner": "Yani"},
    {"kind":"Cat","owner": "Seif"},
    {"kind":"Hamster","owner": "Denise"},
]

# looping the dictionaries 
for pet in pets:
    # assigning variables: what kind of pet and its order
    kind = pet["kind"]
    owner = pet["owner"]
    # print
    print(f"The pet is a {kind} and the owner's name is {owner}.")

