# Exercise 2 : Glossary
'''A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, lets call it a glossary.

* Think of five programming words youve learned about in the previous chapters. Use these words as the keys in your glossary, 
and store their meanings as values.

* Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print 
the word on one line and then print its meaning indented on a second line.
 Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

# Assigning Glossary / Listing words and definition
print("Glossary:")
glossary = {
    'variable': 'A named storage location that holds data or values in a computer program.',
    'string': 'A data type used to represent text, consisting of a sequence of characters.',
    'float': 'A data type used to represent decimal or floating-point numbers in a computer program.',
    'integer': 'A data type used to represent whole numbers (positive or negative) without any fractional or decimal part.',
    'function': 'A reusable block of code that performs a specific task or set of tasks in a program, often with input parameters and a return value.',
}

# Printing the list
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")





