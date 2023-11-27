arr = [30, 17, -3, 44, -10, 9, 89]
arr0 = []
for element in arr:
    if element % 2 == 0:
        arr0.append(element)

for element in arr:
    if element % 2 != 0:
        arr0.append(element)

print(arr0)