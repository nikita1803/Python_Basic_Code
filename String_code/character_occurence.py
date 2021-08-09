'''
@Author: Nikita Rai
@Date: 2021-08-09 4:00:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-09 4:00:30
@Title : Write a Python program to count the number of characters (character frequency) in a
string.

'''
def char_occurence(string1):
    '''
    Description:
     char_occurence is a function where i take a empty dictionary where i can store the string value with key vale
    Parameter:
      string1 is passes for count the occurance of character
    Return:
       List of variable values are returning from function
    '''
    dict = {}
    for n in string1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_occurence('NikitaRai'))