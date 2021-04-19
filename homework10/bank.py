# avery cunningham
# Scrooge McDuck's Bank


class Bank:
    def __init__(self, name, accounts, owner):
        self.name = name
        self.accounts = accounts
        self.owner = owner

    def withdraw(self, account, amount):
        print(f"{account.name} is withdrawing ${amount}")
        if amount > 0.1 * account.balance:
            print("transaction unsuccessful, insufficient account balance")
            account.withdraw(5)
            account.penalties += 1
        else:
            account.withdraw(amount)
            for a in self.accounts:
                if a is not account and a is not self.owner:
                    self.owner.withdraw(amount)
                    a.deposit(amount)
        print(self)

    def __str__(self):
        s = f"Here are the current account balances in {self.name}:\n"
        for a in self.accounts:
            s += a.__str__() + "\n"
        return s


class Account:
    def __init__(self, accountNumber, name, balance=0):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        self.deposits = 0
        self.withdrawls = 0
        self.penalties = 0

    def deposit(self, amount):
        self.balance += amount
        self.deposits += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.withdrawls += 1

    def __str__(self):
        s = f"{self.name}'s account #{self.accountNumber} has a balance of ${self.balance}, {self.penalties} penalties, {self.deposits} deposits, and {self.withdrawls} withdrawls"
        return s


huey = Account(accountNumber=700007, name="Huey Duck", balance=150)
dewey = Account(accountNumber=800008, name="Dewey Duck", balance=350)
louie = Account(accountNumber=900009, name="Louie Duck", balance=25)
scrooge = Account(accountNumber=100001, name="Scrooge McDuck", balance=1000000)

bank = Bank(name="Scrooge's bank",
            accounts=[huey, dewey, louie, scrooge],
            owner=scrooge)

print("Initial values:\n")
print(bank)

bank.withdraw(account=louie, amount=2)
bank.withdraw(account=dewey, amount=20)
bank.withdraw(account=huey, amount=20)
bank.withdraw(account=louie, amount=10)
bank.withdraw(account=dewey, amount=20)
bank.withdraw(account=huey, amount=30)
bank.withdraw(account=louie, amount=40)