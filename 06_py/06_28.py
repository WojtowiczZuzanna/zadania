"""array1 = list(input("enter the array: "))
array2 = list(input("enter the array: "))

def compare(array1, array2):
    i = 0
    #element = array1[i]
    for element in array1:
        while i <= (len(array1)):
            for element in array1:
                while element == array2[i]:
                    i = i + 1
            else:
                    return False
        return True    
print(compare(array1, array2))
"""
array1 = list(input("enter the array: "))
array2 = list(input("enter the array: "))

def compare(array1, array2):
    if array1 == array2:
        return True
    else:
        return False
print(compare(array1, array2))