import json
movie = {
    "title":"Venom 2",
    "year":2021,
    "actor":{"leading":"Tom Hardy","supporting":"Woody Harrelson"},
    "oscar":False,
    "length":97
    }

with open("favourite.json","w") as file:
    json.dump(movie, file, indent = 5)