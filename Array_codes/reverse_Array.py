'''
@Author: Nikita Rai
@Date: 2021-08-09 03:30:30
@Last Modified by: Nikita rai
@Last Modified time: 2021-08-09 03:30:30
@Title : Write a Python program to reverse the order of the items in the array.

'''
import array

new_arr = array.array('i',[1,2,3,4,5,6])
print("Original Array is :",new_arr)

new_arr.reverse()
print("Reversed Array:",new_arr)
