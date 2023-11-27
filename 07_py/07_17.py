file = open('sample1.txt')

#read_line = True
count = 0
#while read_line:
for line in file:
        print(line, end="")
        count += 1
        if count % 5 == 0:
            #read_line = False
            input("Press Enter...")        

file.close()