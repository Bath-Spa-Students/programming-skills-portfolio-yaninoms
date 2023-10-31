## Exercise 2: Favorite Book
'''Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
'''

# defining a function with one parameter
def fav_book(title):
    #the message
    print(f"One of my favorite books is {title} by Haruki Murakami.")

# the argumentin the function call
fav_book('Norwegian Wood')