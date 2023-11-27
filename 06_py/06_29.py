arr1 = [4,36,12,28,9,44,5] 
arr2 = [5,1,36]

arr1 = [x for x in arr1 if x not in arr2]

"""for element in arr1:
    i = 0

    if element == arr2[i]:
        arr1 = arr1 - [element]
    elif element != arr2[i]:
        continue
    i = i + 1
"""
print(arr1)
