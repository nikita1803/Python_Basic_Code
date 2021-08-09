'''
@Author: Nikita Rai
@Date: 2021-08-09 03:10:30
@Last Modified by: Nikita rai
@Last Modified time: 2021-08-09 03:10:30
@Title : Write a Python program to get the number of occurrences of a specified element in an
array.

'''
Array = [1, 16, 1, 11, 1, 22, 12, 1, 1]
x = 8

def count_X(Array, x):
    '''
    Description:
     count_X is a function which is use to check that the predefine value 8 is occure how many times 
    Parameter:
      Array and x is the paramater where x is 8 which i want to check that how many times the 8 is occured in the array
    Return:
       total count is return 
    '''
    count = 0
    for element in Array:
        if (element == x):
            count = count + 1
    return count

print('{} has occurred {} times'.format(x, count_X(Array, x)))