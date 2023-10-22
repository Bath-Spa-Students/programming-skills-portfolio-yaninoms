## Exercise 6: Shrinkin
'''You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.   '''

# Initial guest list
guests = ['mc', 'river', 'jhunnie']

# Send dinner invitations
def send_invitation(guest):
    print(f"Hey {guest.title()}!, let's have a dinner at 8 PM.")

for guest in guests:
    send_invitation(guest)

# Mc turned down the invitation, so invite Aizzy instead
guests[guests.index('mc')] = 'aizzy'

# Send new invitations
for guest in guests:
    send_invitation(guest)

# Limit to two guests
print("\nThe New guest list:\n", guests)
print("Sorry, I can only invite two people.")

# Inform the other guests
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest.title()}, there's no space at the table.")

# Invite the remaining two guests
for guest in guests:
    print(f"{guest.title()}, please come to dinner.")

# Empty out the list
guests.clear()

# Prove the list is empty
print(guests)