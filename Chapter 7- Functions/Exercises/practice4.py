# Practice Question : Q4
'''Write a Python program that defines a function to calculate the area of a circle, and then
calls that function with a given radius.'''

def cir_area(r):
    area = 3.14*(r**2)
    return area

r = float(input("Enter Radius:"))
result = cir_area(r)
print(f"The area of the circle is {result}")

