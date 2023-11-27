import csv
file = open('studentslist.csv')
file.read

with open('studentslist.csv', newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['age']) < 30:
            print(row)

file.close()