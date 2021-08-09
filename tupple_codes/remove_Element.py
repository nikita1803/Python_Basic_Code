'''
@Author: Nikita Rai
@Date: 2021-08-07 6:20:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-07 6:20:00
@Title : Write a Python program to remove an item from a tuple.

'''
Tuple_element = input("Enter the elements for tuple : ")
list = Tuple_element.split(",")
tuple = tuple(list)
print('Tuple : ',tuple)

tuple = tuple[:3] + tuple[4:]
print(type(tuple))
print("After removing 4th element from the tuple", tuple)