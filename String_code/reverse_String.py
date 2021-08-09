'''
@Author: Nikita Rai
@Date: 2021-08-09 4:40:30
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-09 4:40:30
@Title : Write a Python program to reverse a string..

'''
def reverse(str): 
    '''
    Description:
     reverse is a function which is use to reverse the string using slice operator
    Parameter:
      string is passes as a parameter
    Return:
       returned the reverse string 
    '''  
    str = str[::-1]   
    return str   
    
String = "NikitaRai"  
print ("The original string  is : ",String)   
print ("The reversed string using extended slice operator  is : ",reverse(String))