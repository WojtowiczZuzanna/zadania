class bankAccount():
    def __init__(self, deposit, withdraw, number, balance = 0):
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.number = number

    def create(self, nr):
        self.number = nr

    def display(self):
        print(f"Account Number: {self.number}", "\n",f"Balance: {self.balance}")

    def Deposit(self, deposit):
        self.balance += deposit
    
    def Withdraw(self, withdraw):
        if withdraw > self.balance:
            print("Withdraw bigger than acoount balance")
        else:
            self.balance -= withdraw


account = bankAccount(deposit=0, withdraw=0, number=0)

account.create(nr=12345655559090111100007722)
account.display()
account.Deposit(25.30)
account.display()
account.Withdraw(31.70)
account.display()
account.Withdraw(14.00)
account.display()