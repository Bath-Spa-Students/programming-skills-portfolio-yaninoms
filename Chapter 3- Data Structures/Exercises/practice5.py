# PRACTICE QUESTIONS 3
'''You have given a Python list. Write a program to find value 20 in the list, and if it is present,
replace it with 200. Only update the first occurrence of an item.'''

# creating a list with values of 20
list = ['10','20','45','2','89','20']

# if statement to replace the first occurence of 20 with 200
if '20' in list:
    index = list.index('20')
    list[index] = '200'
    
print(list) # printing results


