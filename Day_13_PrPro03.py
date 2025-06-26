#Combination (Encapsulation,Inheritance, Poly)

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest}")

# Usage
acc = SavingsAccount("Vishnu", 1000)
acc.deposit(500)
acc.add_interest()
acc.withdraw(200)

