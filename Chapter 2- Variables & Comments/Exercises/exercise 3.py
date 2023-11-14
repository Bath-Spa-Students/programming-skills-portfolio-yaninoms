# Exercise 3: Stripping Names
'''Use a variable to represent a person’s name, and include some whitespace characters at the beginning
and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().'''

# Assigning a name to a variable
print("Unmodified:")
name="\t\n Miliani Leopoldo \n\t"
print(name)

# Print using lstrip()
print("With .lstrip():")
print (name.lstrip())

# Print using rstrip()
print("With .rstrip()")
print (name.rstrip())

# Print using strip()
print("With .strip():")
print (name.strip())




