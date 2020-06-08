# Continueing practice with class, attributes, and methods
# bank app

class bankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        return self.balance
    def yield_interest(self):
        return self.int_rate

X001 = bankAccount()
X002 = bankAccount(0.02, 0)

print("*"*10)
print("Account: #X001")
X001.deposit(100).deposit(200).deposit(300).withdraw(100)
print("Interest Rate:", str(float(X001.yield_interest())*100)+"%,", "Balance:", "$"+str(X001.display_account_info()))

print("="*25)

X002.deposit(500).deposit(250).withdraw(20).withdraw(100).withdraw(25).withdraw(75)
print("*"*10)
print("Account: #X002")
print("Interest Rate:", str(float(X002.yield_interest())*100)+"%,", "Balance:", "$"+str(X002.display_account_info()))