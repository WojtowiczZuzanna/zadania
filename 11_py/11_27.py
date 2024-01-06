test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

results = list(filter(lambda x: 100>x["result"]>=50, test_results))

for student in results:
    print(f"{student['name']}: {student['result']}")