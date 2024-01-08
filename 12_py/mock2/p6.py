def f(mnumbers):

    a =  ["1","2","3","4","5","6","7"]
    b = ["a", "b", "c", "d", "A", "B", "C", "D"]
    valid = 0

    for element in mnumbers:
        if element[0] in a or element[0] in b or element[0] == "+" or element[0] == "-":
            if all(char in a or char in b for char in element[1:]):
                valid += 1
    

    return valid

if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-gH"]))
    print(f(["A05","-3+1","7ab8C","+D1","-22k"]))