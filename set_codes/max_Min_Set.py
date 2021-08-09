'''

@Author: Nikita Rai
@Date: 2021-08-08 8:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-08 8:10:00
@Title : Write a Python program to find maximum and the minimum value in a set.

'''
Set = set()
num_Element = int(input("Enter number of Elements:"))

for i in range(num_Element):
    element = input("Enter Element")
    Set.add(element)

print(Set)

def MAX(Set):
    '''
    Description:
     MAX is function to calculate the maximum element  from the set
    Parameter:
      Set is the only parameter passes through which it check which element is maximum
    Return:
       Maximum element from the set should be return
    '''
    return (max(Set))

def MIN(Set):
    '''
    Description:
     MIN is function to calculate the minimum element  from the set
    Parameter:
      Set is the only parameter passes through which it check which element is minimum
    Return:
       smallest element from the set should be return
    '''
    return(min(Set))

print("Maximum value in the set is " ,MAX(Set))
print("Minimum value in the set is " ,MIN(Set))