import random

file = open("random.txt", "w")

for i in range (0,50):
    file.write(str(random.randint(100,999)) + '\n')

file.close()