def f(n):
    check = []
    odd = []
    even = []
    sn = str(n)

    for number in sn:
        check.append(int(number))
    
    for number in sn:
        number = int(number)
        if number%2 == 0:
            even.append(number)
        else:
            odd.append(number)

    if odd == []:
        return -1
    else: 
        return max(odd) - min(odd)
    
if __name__ == "__main__":
    print(f(10852))
    print(f(7235973))
    print(f(4388))
    print(f(846206))