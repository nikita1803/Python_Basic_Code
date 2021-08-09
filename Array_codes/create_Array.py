'''
@Author: Nikita Rai
@Date: 2021-08-09 03:00:30
@Last Modified by: Nikita rai
@Last Modified time: 2021-08-09 03:00:30
@Title : Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.

'''
import array as arr
array_num = arr.array('i', [1,2,3,4,5])
for i in array_num:
    print(i)
print("Access the items individually through index")
print(array_num[0])
print(array_num[1])
print(array_num[2])
print(array_num[3])
print(array_num[4])