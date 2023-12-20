def avg_speed(a,b,c):
    time = b + c/60
    return a/time

a = int(input("Enter distance in km: "))
b = int(input("Enter number of travel hours: "))
c = int(input("Enter number of travel minutes: "))

print(f"Average speed: {avg_speed(a,b,c)}")