# Add a LoanAccount class that:
    # Inherits from BankingSystem
    # Has __credit_limit set in __init__
    # Overrides withdraw() — can withdraw even if balance is 0, as long as total withdrawn doesn't exceed credit limit
    # Has get_info() that prints balance and remaining credit

class BankAccount():
    def __init__(self):
        self.__balance = 0
        self.__account_name = "John Doe"

    def deposit(self, amount):
        if amount <= 0:
            return "amount must be greater than zero"
        else:
            self.__balance += amount
            return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            return "amount must be greater than zero"
        if amount > self.__balance:
            return "insufficient balance"
        self.__balance -= amount
        return amount

    def get_balance(self):
        return self.__balance

    def get_info(self):
        return self.__account_name, self.__balance

class LoanAccount(BankAccount):
    def __init__(self, credit_limit):
        super().__init__()
        self.__credit_limit = credit_limit

    def withdraw(self, amount):
        if amount <= 0:
            return "amount must be greater than zero"

        balance = super().get_balance()
        if amount > (self.__credit_limit + balance):
            return "insufficient balance"
        
        if balance > 0:
            amount_to_withdraw = amount
            amount -= balance
            super().withdraw(balance)
            if amount > 0 :
                self.__credit_limit -= amount
                return amount_to_withdraw
            return amount_to_withdraw
        else:
            self.__credit_limit -= amount
            return amount

    def get_info(self):
        name, balance = super().get_info()
        return name, balance, self.__credit_limit

loan = LoanAccount(500)
print(f"""
       withdrawn: ${loan.withdraw(500)}
       deposited: ${loan.deposit(200)}
       withdrawn: ${loan.withdraw(600)}
       balance: {loan.get_info()[1]}
       credit_balance: {loan.get_info()[2]}
        
""")

