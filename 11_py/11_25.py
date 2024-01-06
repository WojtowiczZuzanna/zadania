stats = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

temp = list(filter(lambda x: stats[x]>0, stats))
print("Cities with positive temperstures: ", end="")
print(*temp)