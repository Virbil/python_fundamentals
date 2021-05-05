class User:
    def __init__(self, username, email):
        self.user = username
        self.email = email
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.user}, Account Balance: {self.balance}")
        return self

    def transfer_money(self, receiving_user, amount):
        # print("Hit transfer Method.")
        # print(f"Giving account: {self.user}. Receiving account: {receiving_user}")
        self.balance -= amount
        receiving_user.balance += amount
        return receiving_user.balance, self

bryce = User("virbil", "virbil@gmail.com")
stef = User("red", "red@gmail.com")
harvey = User("rugrat", "rugrat@gmail.com")

bryce.make_deposit(50).make_deposit(350).make_deposit(1025).make_withdrawal(700).display_user_balance()

stef.make_deposit(75).make_deposit(988).make_withdrawal(57).display_user_balance()

harvey.make_deposit(8756).make_withdrawal(33).make_withdrawal(108).make_withdrawal(4621).display_user_balance()

print("-"*80)
print("Update with Transferred Funds")
transfer = bryce.transfer_money(harvey, 50)
transfer[1].display_user_balance()
harvey.display_user_balance()

# output = transfer[1].display_user_balance
# print(f"virbil account transfer. {output}")
# new_balance = harvey.display_user_balance()
# print(f"rugrat account update. {new_balance}")