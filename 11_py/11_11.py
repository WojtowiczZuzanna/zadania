avg_speed = lambda a,b,c: a/(b+c/60)

a = int(input("Enter distance in km: "))
b = int(input("Enter number of travel hours: "))
c = int(input("Enter number of travel minutes: "))

print(f"Average speed: {avg_speed(a,b,c)}")