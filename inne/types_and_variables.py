#
#Data types:

#text: 
x="Hi"
str(x) #letters

#numeric: 
x=20
int(x) #whole numbers, 

x=20.5
float(x) #numers with decimal points, 

x=1j
complex(x) #letters and numbers

#sequence: 
x=["apple", "banana", "cherry"]
list(x) #words, 

range(6) #sequence of numbers, from 0 by default, 

x=("apple", "banana", "cherry") 
tuple(x) #ordered and unchangeable

bool(x) #x=True/False


#
#Variables     Output:
x = str(3)   #x -> '3'
y = int(3)   #y -> 3
z = float(3) #z -> 3.0

#Get the Data Type of a Variable
# type()
x = 5
print(type(x)) #x -> integer


#
#Operations: 

#Arithmetic Operations
print(4 + 2.5) #Addition
print(4 - 2) #Sustraction
print(4.4 * 2) #Multiplication
print(4.0 / 2) #Division
print(4 ** 2) #Exponent


print(11 // 3) #Floor Division Operator
print(11 % 3) #Modulus Operator (Reszta)

#Comparisons (True/False)
print(1 == 2) #False
print(1 != 2) #True
print(1 < 2) #True
print(1 >= 2) #False

#Other
print(abs(-9)) #Absolute Value
print(round(3.14159, 2)) #Round to a specified numer of decimal places