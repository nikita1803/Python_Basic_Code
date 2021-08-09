'''

@Author: Nikita Rai
@Date: 2021-08-08 8:20:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-08 8:20:00
@Title : Write a Python program to remove an item from a set if it is present in the set.

'''
SET = {0, 1, 2, 3, 4, 5}
print("Original set is :" , SET)
SET.discard(2)  # discard is the keyword which is use to remove the element
print("After removing the element" ,SET)

SET = {0, 1, 2, 3, 4, 5, 6, 7}
print("Original set is :" , SET)
SET.remove(0)  # remove is also the keyword which is use to remove the element
print("After removing the element" ,SET)