def f(uid):
    for i in range(len(uid)):
        for j in range(i+1,len(uid)):
            for element_i in uid[i]:
                for element_j in uid[j]:
                    if element_i == element_j:
                        return False
                else:
                    continue
    return True

if __name__ == "__main__":
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))
    print(f(["bob2","bob2"]))
    print(f(["bob2","BOB2"]))