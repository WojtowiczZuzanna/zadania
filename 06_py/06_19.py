import random
arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)

arr10 = []
arr10.append(4)
arr10.append(0)
arr10.append(3)
print(arr10)

arr11 = []
for i in range(15):
    arr11.append(0)
print(arr11)

arr12 = []
for i in range(1,31):
    arr12.append(i)
print(arr12)

arr13 = []
for i in range(20):
    n = random.randint(0,1)
    arr13.append(n)
print(arr13)

arr14 = []
arr = []
for i in range(2):    
    arr.append(False)
for j in range(5):
    arr14.append(arr)
print(arr14)