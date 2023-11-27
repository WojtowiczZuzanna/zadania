file = open('sample2.txt', 'r')
copyline = open('copyline.txt', 'w')

for line in file:
    copyline.write(line)

file.close()
copyline.close()