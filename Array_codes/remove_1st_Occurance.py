'''
@Author: Nikita Rai
@Date: 2021-08-09 03:20:30
@Last Modified by: Nikita rai
@Last Modified time: 2021-08-09 03:20:30
@Title : Write a Python program to remove the first occurrence of a specified element from an
array.

'''
from array import *
array_num = array('i', [1, 8, 5, 8, 10, 1, 9, 8])
print("Original array: "+str(array_num))
print("Remove the first occurrence of 8 from the said array:")
array_num.remove(3)
print("New array: "+str(array_num))