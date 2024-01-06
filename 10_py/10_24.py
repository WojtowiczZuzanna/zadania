class C():
    def __init__(self, points):
        self.points = points

    def m(self, n):
        #n -> number of points ++
            result = []
            for point in self.points:
                if point[0] > 0 and point[1] > 0:
                    result.append(point)
                    
            if len(result) == n:
                print(True)
            else:
                 print(False)
                

p = C([[2,3],[1,8],[-6,4],[3,-7]])
p.m(2)
p.m(3)