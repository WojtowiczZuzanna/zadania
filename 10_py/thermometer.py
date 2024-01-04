import random 

class Thermometer():
    def __init__(self, on = False):
        self.temp = round(random.uniform(34.0, 42.0), 1)
        self.is_on = on

    def ON(self):
        self.is_on = True

    def OFF(self):
        self.is_on = False

    def temperature(self):
        print(f"Temperature: {self.temp}", end=" ")

    def fever(self):
        if 41.0 > self.temp >= 37.0:
            print("FEVER")
        elif 41.0 <= self.temp:
            print("CRITICAL TEMPERATURE")
            