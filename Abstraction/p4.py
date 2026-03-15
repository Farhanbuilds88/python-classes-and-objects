class Account:
    def __init__(self, bal, acc):
        self.__balance = bal
        self.__account_no = acc

    def debit(self, amount):
        self.__balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance:", self.get_balance())

    def credit(self, amount):
        self.__balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance:", self.get_balance())

    def get_balance(self):
        return self.__balance


acc1 = Account(10000, 12345)

acc1.debit(1000)
acc1.credit(500)