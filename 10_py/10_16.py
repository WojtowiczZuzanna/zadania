class Phone():
    def __init__(self, send_message, battery_percentage, turn_on = False):
        self.turn_on = turn_on
        self.send_message = send_message
        self.battery_percentage = battery_percentage    

    def on(self):
        self.turn_on = True
    
    def off(self):
        self.turn_on = False

    def status(self):
        stats = "Phone is on" if self.turn_on==True else "Power is off"
        return stats
    
    def charge(self, percentage):
        percentage = int(percentage)
        if 0 <= percentage <= 100:
              #self.battery_percentage = min(100, self.battery_percentage + percentage)
              print(f'Battery charged to {self.battery_percentage}%')
        else:
            print("Error")

    def message(self):
        if self.turn_on == True:
            print(f"New message: {self.send_message}") 
        
phone1 = Phone("Message1", battery_percentage=67)
phone2 = Phone("Message2", battery_percentage=80)

phone1.status()
phone1.on()
phone1.charge(80)
phone1.status()
phone1.off()


phone2.status()
phone2.on()
phone2.message()
phone2.status()
phone2.off()
