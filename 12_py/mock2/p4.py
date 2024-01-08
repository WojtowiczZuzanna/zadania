def f(fnc, res):
    result = list(filter(fnc, res))
    return max(result) - min(result)

fnc1 = lambda x: x>50
fnc2 = lambda x: x>30 and x<90


if __name__ == "__main__":
    print(f(fnc1,[95,90,20,50,70] ))
    print(f(fnc2,[95,90,20,50,70] ))