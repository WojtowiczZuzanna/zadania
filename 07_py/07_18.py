file = open('sample2.txt')
file_content = file.read()

copy = open('copy.txt', 'w')
copy.write(file_content)

file.close()
copy.close()