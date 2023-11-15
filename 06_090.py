#
#one dimension arrays
arr = [44, 33, 22, 77, 88]

for n in arr:
    if n % 2 == 0:
        print(n)

i = 0
while i < len(arr):
    print(arr[i])
    i = i + 1

for i in range(len(arr)):
    print(arr[i])


##
#two+ dimensional arrays

#najpierw wiersz, potem kolumna

arr = [[44, 77], [22, 99], [11, 55]]

arr = [
    [44, 77],
    [22, 99],
    [11, 55]
]

arr[2][0] #wskazuje wartość 11

