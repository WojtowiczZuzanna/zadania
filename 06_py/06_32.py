array = [15, 38, 7, 23, 14]

number = int(input("Enter a number: "))
def occurs(number, array):
    for element in array:
        if number == element:
            return f'Number {number} appears in the array '
        else:
            continue
    return f'Number {number} does not appear in the array'
        
print(occurs(number, array))