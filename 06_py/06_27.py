arr = [12, 6, 4, 9, 10]
n = range(0,5)
result = ""

def star(n):
    for n in arr:
        result = result + "*" * n
        n = n + 1
    return result

    
print(star(n))
