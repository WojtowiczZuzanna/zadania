file = open('power.txt', 'w')

for i in range(1,11):
    a = str(i)
    b = str(i**2)
    c = str(i**3)
    file.write(a + ', ' + b +', ' + c +' ' +'\n')

file.close()