arr = [4,36,12,28,9,44,5] 

def bubblesort(arr):
    i = 0      
    for i in range(0,5):
        j = 0
        for j in range(1,6):
            if arr[i] <= arr[i+j]:
                #j = j + 1
                continue

            if arr[i] > arr[i+j]:
                arr[i], arr[i+j] = arr[i+j], arr[i]
            
    return arr

print(bubblesort(arr))