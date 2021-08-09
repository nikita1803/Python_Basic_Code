'''

@Author: Nikita Rai
@Date: 2021-08-08 8:00:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-08 8:00:00
@Title : Write a Python program to add member(s) in a set.

'''

Set = set()
num_Element = int(input("Enter number of Elements:"))

for i in range(num_Element):
    element = input("Enter Element")
    Set.add(element)

print(Set)

Set.add('s')
print('Sets elements are:', Set)