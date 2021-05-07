class User:
    def __init__(self, username, email):
        self.user = username
        self.email = email
        self.account = []

    def make_deposit(self, amount, account_num):
        self.account[account_num].make_deposit(amount)
        return self

    def make_withdrawal(self, amount, account_num):
        self.account[account_num].make_withdrawal(amount)
        return self

    def display_user_balance(self, account_num):
        print(f"User: {self.user} \nAccount Balance: ${self.account[account_num].balance}")
        return self

    def transfer_money(self, receiving_user, amount, sending_acct_num, receiving_acct_num):
        # print(f"Giving account: {self.user}. Receiving account: {receiving_user}")
        self.account[sending_acct_num].make_withdrawal(amount)
        receiving_user.account[receiving_acct_num].make_deposit(amount)
        return receiving_user, self

    def create_account(self, balance=0, int_rate=0.01):
        self.account.append(BankAccount(balance, int_rate))
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    # METHODS
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You're broke and don't have that much!")
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.account.balance += amount
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self



bryce = User("virbil", "virbil@gmail.com")
bryce.create_account()
bryce.make_deposit(50, 0).make_deposit(350, 0).make_deposit(1025, 0).make_withdrawal(700, 0).display_user_balance(0)

print("-"*80)

stef = User("red", "red@gmail.com")
stef.create_account()
stef.make_deposit(75, 0).make_deposit(988, 0).make_withdrawal(57, 0).display_user_balance(0)

print("-"*80)

harvey = User("rugrat", "rugrat@gmail.com")
harvey.create_account()
harvey.make_deposit(8756, 0).make_withdrawal(33, 0).make_withdrawal(108, 0).make_withdrawal(4621, 0).display_user_balance(0)

print("-"*80)


transfer = bryce.transfer_money(harvey, 50, 0, 0)
print("Transferring from: ")
transfer[1].display_user_balance(0)
print("Transferring to: ")
harvey.display_user_balance(0)