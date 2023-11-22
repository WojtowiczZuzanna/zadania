file = open("numbers.txt","r")
file_content = file.read

sum = 0
for line in file:
    line = int(line)
    sum = sum + line
    
print(f'Numbers: {file_content}')
print(f'Sum: {sum}')

file.close()