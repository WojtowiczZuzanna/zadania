arr = [34,7,19,4,21,8]

arr1 = []
i = 0
while i in range(0,len(arr)+1):
    for i in arr:
        if i % 2 == 0:
            arr1.append(i)
        i = i + 1

print(arr1)