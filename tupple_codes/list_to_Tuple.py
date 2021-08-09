'''
@Author: Nikita Rai
@Date: 2021-08-07 6:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-07 6:10:00
@Title : Write a Python program to convert a list to a tuple.

'''
list = []

num_element = int(input("Enter number of elements : "))
for i in range(0, num_element):
    element = int(input())
 
    list.append(element) 
     
print(list)

def convert(list):
    '''
    Description:
     covert is a function which is use to convert the list
    Parameter:
      list is the parameter which we have to convert into the tuple
    Return:
       converted list into tuple
    '''
    return tuple(list)

print(convert(list))