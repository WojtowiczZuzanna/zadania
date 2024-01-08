def f(uid):
    for i in range(0,len(uid)):
        for j in range(1, len(uid)): 
            if uid[i] == uid[j]:
                if i == j:
                    continue
                return False
    return True

if __name__ == "__main__":
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))
    print(f(["bob2","bob2"]))
    print(f(["bob2","BOB2"]))