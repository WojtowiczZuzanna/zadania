Recorded_values = [48,47,54,50,42,68,39,46]
higher = list(filter(lambda x: x > 50, Recorded_values))

print("Speed too high: ", end=" ")
print(", ".join(map(str, higher)))