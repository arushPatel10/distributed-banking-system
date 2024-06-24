class Customer:
    def __init__(self, customer_id, initial_balance=0):
        self.customer_id = customer_id
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return "Deposit successful"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return "Withdrawal successful"
        else:
            return "Insufficient funds"

    def query(self):
        return self.balance
