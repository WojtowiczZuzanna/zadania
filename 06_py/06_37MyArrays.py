arr = [7,3,8,5,2]

def fa():
    arr.remove(max(arr))
    return max(arr)

def fb():
    result = max(arr) - min(arr)
    return result 

def fc():
    n = len(arr)
    i = 0
    for i in range(0,4):
        for j in range(1, n-i):
            if arr[i] <= arr[i+j]:
                continue

            if arr[i] > arr[i+j]:
                arr[i],arr[i+j] = arr[i+j],arr[i]
        i = i + 1
        result = arr[len(arr)//2]
    return result

def fd():
    arr0 = []
    arr0.append(min(arr))
    arr0.append(max(arr))
    return arr0

def fe():
    result = ""
    for element in arr:
        result += str(element) + '-'
    return result[:-1]

print(f'Second largest number: {fa()}')
print(f'THe difference between the largest and smallest values: {fb()}')
print(f'The median of the array: {fc()}')
print(f'Two element array of the smallest and the largest values: {fd()}')
print(f'Array as a string with minus sign: {fe()}')