class User:
    def __init__(self, username, email):
        self.user = username
        self.email = email
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.user}, Account Balance: {self.balance}")

    def transfer_money(self, receiving_user, amount):
        # print("Hit transfer Method.")
        # print(f"Giving account: {self.user}. Receiving account: {receiving_user}")
        self.balance -= amount
        receiving_user.balance += amount
        return receiving_user.balance

bryce = User("virbil", "virbil@gmail.com")
stef = User("red", "red@gmail.com")
harvey = User("rugrat", "rugrat@gmail.com")

bryce.make_deposit(50)
bryce.make_deposit(350)
bryce.make_deposit(1025)
bryce.make_withdrawal(700)
bryce.display_user_balance()

stef.make_deposit(75)
stef.make_deposit(988)
stef.make_withdrawal(57)
stef.display_user_balance()

harvey.make_deposit(8756)
harvey.make_withdrawal(33)
harvey.make_withdrawal(108)
harvey.make_withdrawal(4621)
harvey.display_user_balance()

bryce.transfer_money(harvey, 56)
bryce.display_user_balance()
harvey.display_user_balance()