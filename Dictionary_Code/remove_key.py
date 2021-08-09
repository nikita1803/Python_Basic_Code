'''
@Author: Nikita Rai
@Date: 2021-08-08 06:40:00
@Last Modified by: Nikita Rai
@Last Modified time: @Date: 2021-08-08 06:40:00
@Title : Write a Python program to remove a key from a dictionary.
'''
Dictionary = {'a':'apple','b':'ball','c':'cat','d':'dog'}
print("Original Dictionary is :" , Dictionary)
if 'a' in Dictionary: 
    del Dictionary['a']
print("After removing the key :" , Dictionary)