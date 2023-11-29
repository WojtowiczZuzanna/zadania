person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

#w tablicy indeksem jest numer
#w słowniiku indeksem jeste nazwa klucza

print(person)
print(person["name"])
print(person['hobby'])

person['surname'] = "Nowak"
person['married'] = not person["married"]
person['gender'] = "Male"
person['hobby'].append("bicycle")
person["phone"]["work phone"] = "777888999"

print(person)