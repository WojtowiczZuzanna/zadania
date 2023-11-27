t = (50,20,40,50,30,50)

number = int(input("Enter a number: "))
count = 0
for element in t:
    if element == number:
        count += 1

print(f'{number} occurs {count} times in the tuple')