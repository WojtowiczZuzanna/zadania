class Phone():
    def __init__(self,brand,model,color,mess):
        self.brand = brand
        self.model = model
        self.color = color
        self.is_on = False
        self.mess = mess
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def send_mess(self,mess):
        self.mess = mess

phone = Phone(
    "Samsung","Galaxy A33","black", "TAK")

print(f"Brand: {phone.brand}, ", end = " ")
print(f"model: {phone.model}, ", end = " ")
print(f"color: {phone.color}")

phone.on()
phone.send_mess(phone.mess)

if phone.is_on:
    print(f"ON, message {phone.mess}")
else:
    print(f"OFF")