'''
@Author: Nikita Rai
@Date: 2021-08-07 8:40:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-07 8:40:00
@Title :Write a Python program to sum all the items in a list.
'''
TOTAL_ELEMENT = 0
LIST = [2,4,6,8,10]
print(LIST[::-1])

for element in range(0,len(LIST)):
    TOTAL_ELEMENT = TOTAL_ELEMENT + LIST[element]

print("Sum of all elements in the given list:", TOTAL_ELEMENT)
