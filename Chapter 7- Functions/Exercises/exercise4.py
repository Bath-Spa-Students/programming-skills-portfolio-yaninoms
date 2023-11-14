## Exercise 4:  Large Shirts :ballot_box_with_check:

'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and amedium shirt with the default message, and a shirt of any size with a different message.'''

# making the function
def make_shirt(size='large', message='I love Python!'):
    print(f"\nI'm going to make a {size} t shirt.")
    print(f'It will say, "{message}"')

# calling the function
make_shirt()
make_shirt(size='medium')
make_shirt('small','Print Hello World!')







