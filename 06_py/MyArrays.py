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
        for j in range(1,5):
            if arr[i] <= arr[i+j]:
                continue

            if arr[i] > arr[i+j]:
                arr[i],arr[i+j] = arr[i+j],arr[i]
        i = i + 1
    return arr

#print(f'Second largest number: {fa()}')
#print(f'THe difference between the largest and smallest values: {fb()}')
print(f'{fc()}')