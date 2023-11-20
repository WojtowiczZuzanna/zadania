arr = [-15, 8, -31, 47, -2, 19]
max = -15
min = -15

i = 0
while i in range(0,len(arr)):
    if arr[i] > max:
        max = arr[i]
        i = i + 1
    elif arr[i] <= max:
        i = i + 1
        continue
i = 0
while i in range(0,len(arr)):
    if arr[i] < min:
        min = arr[i]
        i = i + 1
    elif arr[i] >= min:
        i = i + 1
        continue
    
print(max, min)