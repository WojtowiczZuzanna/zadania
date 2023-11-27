file = open('numbers.txt', 'w')

numbers = range(1,51)

for number in numbers:
    number = str(number)
    file.write(number + "\n")

    
file.close()