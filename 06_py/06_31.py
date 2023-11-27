arr = [2,3,2,5,8,1,9,8]
arr0 = []

for element in arr:
    if element not in arr0:
        arr0.append(element)
    elif element in arr0:
        arr0.remove(element)

print(*arr0)