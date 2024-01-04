class TV():
    def __init__(self, volume = 0):
        self.is_on = False
        self.volume = volume

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print(f"TV is on, volume: {self.volume}")
        elif self.is_on == False:
            print("TV is off")

    def vol_increase(self):
        if self.volume in range(0,10):
            self.volume += 1
        else:
            print("Volume at the highest")

    def vol_decrease(self):
        if self.volume in range(1,11):
            self.volume -= 1
        else: 
            print("Volume at the lowest")

tv1 = TV()
tv1.show_status()
tv1.turn_on()
tv1.show_status()
tv1.vol_increase()
tv1.vol_increase()
tv1.vol_increase()
tv1.show_status()
tv1.vol_decrease()
tv1.show_status()
tv1.turn_off()
tv1.show_status()