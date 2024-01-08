def f(word):
    result = ""
    for i in range(len(word)):
        a = word[:i].lower() + word[i:].capitalize()
        result += a + "-"
    return result[:-1]

if __name__ == "__main__":
    print(f("book"))
    print(f("water"))
    print(f("ok"))
    print(f("a"))
    print(f(""))
