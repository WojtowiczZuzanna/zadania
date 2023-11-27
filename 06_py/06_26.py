arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
result = arr[0]

for element in arr:
    if len(element) > len(result):
        result = element
    else:
        continue

print(result)