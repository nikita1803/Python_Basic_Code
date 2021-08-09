Tuple_element = input("Enter the elements for tuple : ")
list = Tuple_element.split(",")
tuple = tuple(list)
print("Orignal Tuple : " + str(tuple))

Num = 6
result = False
for element in tuple : 
    if Num == element :
        result = True
        break
    
print("Element is exist in the tuple or not ?" + str(result))