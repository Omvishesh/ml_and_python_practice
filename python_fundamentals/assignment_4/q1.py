class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def check_balance(self):
        print(f"your balance is {self.balance}")

person1 = BankAccount(456, "om", 40000)
person1.check_balance()
person1.deposit(10000)
person1.check_balance()
person1.withdraw(10000)
person1.check_balance()