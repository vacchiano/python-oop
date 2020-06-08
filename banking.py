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
        self.balance -= amount
        print(self.name, "Withdrew $"+str(amount))

dom = User("Dom Vacchiano", "domo@dom.com")
print ("$"+str(dom.balance))
dom.deposit(300)
print("$"+str(dom.balance))

