arr = [2,5,4,7]
bruh = list(filter(lambda x: x>4,arr))
print(*bruh)

bruh2 = list(filter(lambda x: x%2==0,arr))
print(*bruh2)
