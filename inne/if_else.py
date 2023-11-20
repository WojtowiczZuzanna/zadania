# "=" przypisanie
# "==" porównanie

#1
age = int(input("Enter your age: "))

if 18 <= age <= 99:
    print("You are now signed up.")
elif age >= 100:
    print("Congrats from Queen Elizabeth II.")
else: 
    print("You do not meet the requirements.")

#2
online = True   

if online: 
   print("The user is online")
else:
    print("The user is offline") #if online = False


#3
temperature = int(input("Enter the temperature(in Celsius degrees): "))

if temperature <= -20:
    print("It's freezing!")
elif -20 < temperature < 15:
    print ("It's cold.")
elif 15 <= temperature <= 30:
    print ("It's warm.")
else:
    print("It's hot!")

#4
#if not
#if ... or
#if ... and
