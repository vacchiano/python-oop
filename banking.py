# Practicing classes
# A simulation banking app 

class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(self.name, "Deposited $"+str(amount))
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("ERROR; Not Enough Funds: you have", "$"+str(self.balance), "remaining")
            return
            #print('WARNING:', self.name, "your balance is", "$"+str(self.balance))
        self.balance -= amount
        print(self.name, "Withdrew $"+str(amount))
    def getBalance(self):
        print(self.name, "you have $" + str(self.balance), "in your account")

dom = User("Dom Vacchiano", "domo@dom.com")
jack = User("Jack Doe", "jack@mail.com")
tina = User("Tina Fry", "tina@msn.com")

spaces = "-"*10

dom.getBalance()
jack.getBalance()
tina.getBalance()
print(spaces)

dom.deposit(300)
dom.deposit(500)
dom.deposit(100)
dom.withdraw(100)
dom.getBalance()
print(spaces)

jack.deposit(500)
jack.deposit(150)
jack.withdraw(200)
jack.withdraw(150)
jack.getBalance()
print(spaces)
tina.deposit(600)
tina.withdraw(100)
tina.withdraw(50)
tina.withdraw(75)
tina.withdraw(500)
tina.getBalance()

