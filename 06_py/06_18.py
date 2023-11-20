arr = [[True,False],[True,True],[False,False]]

#for i in range(len(arr)):
for row in arr:
    #for n in row:
    for i, n in enumerate(row):
        if n == True:
            row[i] = False
        elif n == False:
            row[i] = True

print(arr)

    