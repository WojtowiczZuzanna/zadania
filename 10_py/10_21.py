class Statistics():
    def __init__(self, numbers):
        self.numbers = numbers

    def add(self):
        n = int(input("Enter a number: "))
        (self.numbers).append(n)
        return self.numbers

    def display1(self):
        print(*self.numbers)

    def theGreatest(self):
        g = max(self.numbers)
        return g
    
    def theSmallest(self):
        s = min(self.numbers)
        return s

    def aritmMean(self):
        sum = 0
        for element in self.numbers:
            sum += element
        return sum/len(self.numbers)

    def median(self):
        m = sorted(self.numbers)

        if len(m) % 2 == 0:
            a = len(m)//2 - 1
            b = len(m)//2 + 1
            return (m[a]+m[b])/2
        else:
            c = round(len(m)/2)
            return m[c]

    def display2(self):
        print(f"The greatest number: {self.theGreatest()}")
        print(f"The smallest number: {self.theSmallest()}") 
        print(f"Arithmetic mean: {self.aritmMean()}")
        print(f"Median: {self.median()}")
        


array = Statistics([12, 37, 6, 9, 17])

array.add()
array.display1()
array.theGreatest()
array.theSmallest()
array.aritmMean()
array.median()
array.display2()
