text = "I completely agree with you"

result = list(map(lambda word: len(word), text.split()))
print(result)