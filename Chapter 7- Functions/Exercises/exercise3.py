## Exercise 3: T-Shirt  :ballot_box_with_check:

'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The functionshould print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

# making the function
def make_shirt(size, message):
    # the message
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

# calling the function
make_shirt('large', 'Hello World!')
make_shirt(message="Readability counts.", size='medium')




    