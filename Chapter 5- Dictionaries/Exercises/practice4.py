# Practice Question : Q4
'''Write a Python program to iterate through both the keys and values of a dictionary and printthem'''
# the orginal dictionary
me = {
    'first_name':'Miliani',
    'last_name':'Leopoldo',
    'age':17,
    'cat':'Nacci',
    }

# printing each piece of information stored
for key, value in me.items():
    print(f"Key: {key}, Value: {value}")

