countries = [
    {"name":"Poland", "population":38000000},
    {"name":"RPA", "population": 59392000},
    {"name":"Spain", "population":41415000},
    {"name":"Venezuela", "population":28199000},
    {"name":"Kazakhstan", "population":19000000}
    ]

print("COUNTRY", "POPULATION")
i = 0
while i in  range(0,len(countries)):
    country = countries[i]
    #print(country["name"], country["population"])
    print(f'{countries[i]["name"]} {countries[i]["population"]}')
    i += 1

