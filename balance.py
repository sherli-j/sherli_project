class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Holder:", self.account_holder)
        print("Available Balance: ₹", self.balance)


# Create a sample bank account
account = BankAccount("Anu", 25000)

# Check bank balance
account.check_balance()