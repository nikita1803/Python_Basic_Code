'''
@Author: Nikita Rai
@Date: 2021-08-07 8:20:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-07 8:20:00
@Title : Write a Python program to remove duplicates from a list..
'''
list = []

num_element = int(input("Enter number of elements : "))
for i in range(0, num_element):
    element = int(input())
    list.append(element) 
     
print(list)

def Remove(list):
    '''
    Description:
     Remove is a function where i can take one empty list and compare the orignal list with empty list and using append 
     adding one by one element provided a condition , only store those element which is not in final list.
    Parameter:
      Orignal list is the passes as a parameter
    Return:
       Returning the final list after romiving the dublicate
    '''
    final_list = []
    for element in list:
        if element not in final_list :
            final_list.append(element)
    return final_list

print(Remove(list))
        