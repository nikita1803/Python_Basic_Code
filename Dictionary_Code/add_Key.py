'''
@Author: Nikita Rai
@Date: 2021-08-08 06:10:00
@Last Modified by: Nikita Rai
@Last Modified time: @Date: 2021-08-08 06:10:00
@Title : Write a Python script to add a key to a dictionary.
'''
dictionary = {'key1':'Nikita', 'key2':'MCA'}
print("original dictionary" , dictionary)

dictionary.__setitem__('Key3', '2020')  #__setitem__ is the keyword which is used to set or add the key and value in the existing dictionary.
print("After adding the another key value" ,dictionary)