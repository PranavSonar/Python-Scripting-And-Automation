class Account:
    def __init__(self, AccountHolder, Money):
        self.accountholder = AccountHolder
        self.money = Money

    def __str__(self):
        self.info = """
        Account Holder: {}
        Account Balance: {}
        """.format(self.accountholder, self.money)
        return self.info

    def deposit(self, Dbalance):
        self.money = self.money+Dbalance
        print("Deposit Accepted")
        return self.money

    def withdraw(self, Wbalance):
        if Wbalance < self.money:
            self.money = self.money-Wbalance
            print("Withdrawal Accepted")
        else:
            print("Funds Unavilable!")

        return self.money


Account1 = Account("Vivek Kumar", 1000)
# print(Account1)
# print(Account1.accountholder)
# print(Account1.money)
Account1.deposit(50)
Account1.withdraw(100)
print(Account1)
Account1.deposit(3000)
print(Account1)
