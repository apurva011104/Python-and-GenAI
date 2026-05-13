class Account:
    def __init__(self, holder: str, balance: float):
        self.holder = holder
        self.balance = balance

    def deposit(self: str, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


class SavingsAccount(Account):

    def add_interest(self):
        self.balance += self.balance * 0.05


s = SavingsAccount("Alex", 10000)

s.deposit(5000)
s.add_interest()

print(s.balance)