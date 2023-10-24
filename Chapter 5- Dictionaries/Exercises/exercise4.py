# Exercise 4: Rivers 

'''Make a dictionary containing three major rivers and the country each river runs through.
One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

rivers = {
    'nile':'egypt',
    'amazon':'peru',
    'yangtze':'china',
    'danube':'germany',
    'mississippi':'usa',
}

for river, country in rivers.items():
    print(f"{river.title()} flows through {country.title()}.")

print("\n The rivers included in the dictionary are:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\n The countries included in the dictionary are:")
for country in rivers.values():
    print(f"- {country.title()}")
