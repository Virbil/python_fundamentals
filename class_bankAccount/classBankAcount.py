class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    # METHODS
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}, Account Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self.balance

print("Main account:")
my_main_account = BankAccount(0.01, 1000)
my_main_account.deposit(500).deposit(300).deposit(2896).withdraw(57).display_account_info()
my_main_account.yield_interest() #.display_account_info()  can't get this to chain
my_main_account.display_account_info()
print("-"*80)


print("Savings account:")
my_savings_account = BankAccount(0.05, 5750)
my_savings_account.deposit(1379).deposit(442).withdraw(29).withdraw(106).withdraw(252).withdraw(13).display_account_info()
my_savings_account.yield_interest()
my_savings_account.display_account_info()