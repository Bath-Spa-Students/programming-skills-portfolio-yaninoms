## Exercise 6: Shrinkin

# Guest Names
guests = ['mc', 'river', 'jhunnie']

# Inviting the Guests Over
name = guests[0].title()
print(f"Hey {name}!, let's have a dinner at 8 PM.")

name = guests[1].title()
print(f"Hey {name}!, let's have a dinner at 8 PM.")

name = guests[2].title()
print(f"Hey {name}!, let's have a dinner at 8 PM.")

name = guests[0].title()
print(f"\n{name} Replied: Sorry, I can't. I have to finish something.")

# Mc turned down the invitation. Inviting Aizzy instead !
guests[0] = 'aizzy'

# New Invitations
name = guests[0].title()
print(f"Hey {name}!, let's have a dinner at 8 PM.")

name = guests[1].title()
print(f"Hey {name}!, let's have a dinner at 8 PM.")

name = guests[2].title()
print(f"Hey {name}!, let's have a dinner at 8 PM.")

print("\t\n The New guest list: \n\t", guests)

# The table didn't arrive in time, sadly, only two guests can be invited. 
print("Sorry, I can only invite two people.")

# Informing the other guests

name = guests.pop(2)
print(f"Sorry {name.title()} there's no space at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del (guests[0])

# Prove the list is empty.
print(guests)





