## Exercise 3: Glossary 2 :ballot_box_with_check:
'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) 
by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
When you’re sure that your loop works, add five more Python terms to your glossary.When you run your program again, 
these new words and meanings should automatically be included in the output.'''


# Assigning Glossary / Listing terms and definitions
print("Glossary:")
glossary = {
    'variable': 'A named storage location that holds data or values in a computer program.',
    'string': 'A data type used to represent text, consisting of a sequence of characters.',
    'float': 'A data type used to represent decimal or floating-point numbers in a computer program.',
    'integer': 'A data type used to represent whole numbers (positive or negative) without any fractional or decimal part.',
    'function': 'A reusable block of code that performs a specific task or set of tasks in a program, often with input parameters and a return value.',
}

# Adding new terms
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = 'A collection of key-value pairs.'
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'

# printing the glossary
for term, definition in glossary.items():
    print(f"\n{term}: {definition}")