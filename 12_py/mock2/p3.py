def f(d):
    avg = 0
    count = 0
    for key, value in d.items():
        avg += value
        count += 1
    avg_n = avg/count

    counter = 0
    for key, value in d.items():
        if value > avg_n:
            counter += 1

    return counter


if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print(f({"LO231":150,"BA787":20,"NZ15":30}))