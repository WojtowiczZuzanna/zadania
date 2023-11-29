import json

with open("data.json") as file:
    data = json.load(file)
"""
for key,value in data.items():

    print(f"{key} : {value}")
"""
i = 0
while i in  range(0,len(data)):
    item = data[i]
    print(f'{key} : {value}')
    i += 1
