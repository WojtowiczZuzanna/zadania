import math

class C():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        if self.x > 0 and self.y > 0:
            result1 = 1
        elif self.x < 0 and self.y > 0:
            result1 = 2
        elif self.x < 0 and self.y < 0:
            result1 = 3
        elif self.x > 0 and self.y < 0:
            result1 = 4
        elif self.x == 0 or self.y == 0:
            result1 = 0
        return (result1)
    
    def m2(self, a, b):
        if self.m1() == C(a,b).m1():
            print(True)
        else:
            print(False)
        
    def m3(self, a, b):
        s = math.sqrt((self.x - a)**2 + (self.y - b)**2)
        if s > 5:
            print(True)
        else:
            print(False)

# Example usage
p = C(2,3)
p.m1()
p.m2(7,4)
p.m2(-3,1)
p.m3(8,5)
p.m3(4,7)

p1 = C(0,5)
p1.m1()
p1.m2(4,7)
p1.m2(-7,0)
