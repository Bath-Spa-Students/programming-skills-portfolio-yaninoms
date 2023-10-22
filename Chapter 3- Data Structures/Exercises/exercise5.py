## Exercise 5: Change Guest List 
'''You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.'''

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