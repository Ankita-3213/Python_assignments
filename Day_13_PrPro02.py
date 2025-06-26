#Encapsulation Method in Python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")


account = BankAccount("John", 100)
account.deposit(50)
account.withdraw(30)

acc = BankAccount("Sam", 200)
acc.deposit(300)
acc.withdraw(0)
# Accessing private attribute will throw an error
#print(account.__balance)
print(account.owner)
print(acc.owner)