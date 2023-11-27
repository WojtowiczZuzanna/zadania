tuple = (10,20,30,40,50)

j = len(tuple)-1
result = ""
while j in range(0, len(tuple)):
    result += str(tuple[j])
    result += ", "
    j -= 1

print(result[:-2])