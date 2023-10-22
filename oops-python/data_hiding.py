class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance  # Getter method for private attribute

# Creating an object of the class
account = BankAccount()

# Depositing and withdrawing money
account.deposit(1000)
account.withdraw(500)

# Accessing the balance using the getter method
print("Account Balance:", account.get_balance())  # Output: Account Balance: 500
