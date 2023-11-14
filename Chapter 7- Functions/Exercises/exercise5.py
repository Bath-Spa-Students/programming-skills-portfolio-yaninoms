# Exercise 5: Cities

'''Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.'''

# making the function
def describe_city(city, country='Philippines'):
    # the message
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

# calling the function
describe_city('manila')
describe_city('reyjavik','iceland')
describe_city('cebu')








