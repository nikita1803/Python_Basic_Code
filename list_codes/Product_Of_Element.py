'''
@Author: Nikita Rai
@Date: 2021-08-07 8:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-07 8:10:00
@Title : Write a Python program to multiplies all the items in a list.
'''
TOTAL_ELEMENT = 1
list = []

num_element = int(input("Enter number of elements : "))
for i in range(0, num_element):
    element = int(input())
 
    list.append(element) 
     
print(list)

for element in range(0,len(list)):
    TOTAL_ELEMENT = TOTAL_ELEMENT * list[element]

print("Product of all elements in the given list:", TOTAL_ELEMENT)