def f(d):
    cars = []
    for row in d:
        if row[1] == "in":
            cars.append(row[0])
        elif row[1] == "out":
            cars.remove(row[0])

    sort = sorted(cars)
    return sort    

if __name__ == "__main__":
    print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]))
    print(f([["KR234","in"],["KR234","out"]]))