'''
@Author: Nikita Rai
@Date: 2021-08-07 6:40:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-07 6:40:00
@Title : Write a Python program to reverse a tuple.

'''
Tuple_element = input("Enter the elements for tuple : ")
list = Tuple_element.split(",")
tuple = tuple(list)
print('Tuple : ',tuple)

def Reverse(tuple):
    Reversed_tuple = tuple[::-1]
    return Reversed_tuple

print("The reverse tupple is : " ,Reverse(tuple))