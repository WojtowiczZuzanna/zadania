array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

result1 = list(filter(lambda x: x%2==0 and x%3==0, array))
result2 = list(filter(lambda x: x%2==0 or x%3==0, array))
print(f"NUmbers divisible by 2 and 3: {result1}","\n",f"Numbers divisible by 2 and numbers divisible by 3: {result2}")
