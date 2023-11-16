class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False


class SavingsAccount(Account):
    def __init__(self, account_number, initial_balance, interest_rate):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest


class CheckingAccount(Account):
    def withdraw(self, amount):
        self.balance -= amount
        return True


if __name__ == '__main__':
    print("Account:")
    account = Account("12345", 1000)
    print("Account number: ", account.account_number)
    print("Balance: ", account.balance)
    account.deposit(100)
    print("Balance + 100: ", account.balance)
    print("Can withdraw 100? ", account.withdraw(100))
    print("Balance - 100: ", account.balance)
    print("Can withdraw 5000? ", account.withdraw(5000))
    print("Balance - 5000: ", account.balance)

    print("\nSavings:")
    savings = SavingsAccount("12345", 1000, 0.02)
    print("Balance: ", savings.balance)
    print("Interest: ", savings.add_interest())
    print("Balance after interest: ", savings.balance)

    print("\nChecking:")
    checking = CheckingAccount("54321", 500)
    print("Can withdraw 5000? ", checking.withdraw(5000))
    print("Balance - 5000: ", checking.balance)