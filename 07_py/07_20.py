file = open('allproducts.txt', 'w')
file1 = open('MeatAndFish.txt')
file2 = open('GrainsAndBread.txt')

file1_cont = file1.read()
file2_cont = file2.read()

file.write(file1_cont)
file.write(file2_cont)

file.close()
file1.close()
file2.close()