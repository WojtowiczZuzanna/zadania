# open file
file = open("countries.txt", "r")
file_content = file.read

# display text file, line by line
counter = 0
for line in file:
     counter += 1
     print(f"{counter}. {line}", end="")

# close file
file.close()
