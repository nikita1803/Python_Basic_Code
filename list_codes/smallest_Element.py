'''
@Author: Nikita Rai
@Date: 2021-08-07 8:30:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-07 8:30:00
@Title : Write a Python program to get the smallest number from a list.
'''
list = []

num_element = int(input("Enter number of elements : "))
for i in range(0, num_element):
    element = int(input())
    list.append(element) 
     
print(list)

smallest = list[0]

for i in range(len(list)):
    if list[i] < smallest :
        smallest = list[i]

print("The smallest element in the list is ", smallest)