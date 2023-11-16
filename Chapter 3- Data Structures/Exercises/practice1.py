# PRACTICE QUESTIONS CHAPTER 3
'''1. Given a Python list, write a program to remove all occurrences of item 20.
Given list:
 list1 = [5, 20, 15, 20, 25, 50, 20]'''

lists1 = [5, 20, 15, 20, 25, 50, 20]

# while loop to remove all 20s
while 20 in lists1:
    lists1.remove(20)
# print new list
print(lists1)

