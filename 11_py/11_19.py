ecomonic_geography = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

numbers = list(filter(lambda x: x>2.0, ecomonic_geography))
aritmmean = round(sum(numbers) / len(numbers), 2)
print(aritmmean)