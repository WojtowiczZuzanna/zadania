class TV():
    def __init__(self,channel_no):
        self.is_on = False
        self.channel_no = 1

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self,channel_no):
        if self.is_on:
            print(f"TV is on, channel: {channel_no}")
        elif self.is_on == False:
            print("TV is off")



tv1 = TV(channel_no)
tv1.show_status(channel_no)
tv1.turn_on()
tv1.show_status()
tv1.turn_off()
tv1.show_status()