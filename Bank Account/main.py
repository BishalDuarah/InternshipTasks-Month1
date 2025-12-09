class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance! Withdrawal cancelled.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance = {self.balance}")

    def display_balance(self):
        print(f"Account owner: {self.owner}, Current balance: {self.balance}")


# Example usage (you can show this as your demo)
if __name__ == "__main__":
    # Create an object of BankAccount
    account = BankAccount("Bishal", 1000)

    account.display_balance()   # Show starting balance
    account.deposit(500)        # Add money
    account.withdraw(300)       # Take out money
    account.withdraw(2000)      # Try to over-withdraw (should fail)
    account.display_balance()   # Final balance
