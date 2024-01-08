def f(fnc,prods):
    a = list(map(fnc,prods))
    return ", ".join(a)

fnc1 = lambda x: "id:"+x[:2]
fnc2 = lambda x: (x[0]+x[-1]).upper() 

if __name__ == "__main__":
    print(f(fnc1, ["water", "cheese", "tomato"]))
    print(f(fnc2, ["water", "cheese", "tomato"]))
