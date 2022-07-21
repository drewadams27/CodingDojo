class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

account1 = BankAccount(.05, 50000)
account2 = BankAccount(.01, 10000)

account1.deposit(100).deposit(200).deposit(300).withdraw(1000).yield_interest().display_account_info()
account2.deposit(1000).deposit(700).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()