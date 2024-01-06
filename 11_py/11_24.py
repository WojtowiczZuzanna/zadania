results = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
    return "Min "+str(limit)+" pts: "+str(list(filter(lambda pts: pts>=limit, results)))

if __name__ == "__main__":
    print(min_pts(70))
    print(min_pts(40))
    print(min_pts(30))