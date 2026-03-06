class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("After deposit:", self.balance)
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("After withdrawal:", self.balance)
    
    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

obj1 = BankAccount("Farhan", 5000)

obj1.show_balance()
obj1.deposit(2000)
obj1.withdraw(1000)