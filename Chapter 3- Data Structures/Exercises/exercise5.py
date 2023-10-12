## Exercise 5: Change Guest List 

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