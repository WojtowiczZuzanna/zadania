def f(vname):

        if len(vname) not in range(1,6):
            return False
        else:
            if vname[0].isalpha() or vname[0] == "_":
                for char in vname[1:]:
                    if char.isalpha() or char.isdigit() or char == "_":
                        continue
                    else:
                        return False
                return True
            else:
                 return False
            

if __name__ == "__main__":
    print(f("abc")) 
    print(f("Abc"))
    print(f("aBC"))
    print(f("_ab_c"))
    print(f("abcdef"))
    print(f("8abc"))
    print(f("_aB8_"))
    print(f("_4x"))
