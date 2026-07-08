# Build a BankAccount class with:

# Private __balance starting at 0
# Private __account_holder set from __init__
# get_balance() → returns balance
# deposit(amount) → adds to balance, validates amount > 0
# withdraw(amount) → subtracts from balance, validates amount > 0 and sufficient balance
# get_account_info() → prints holder name and balance


class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_holder = "John Doe"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"${amount} deposited successfully"
        else:
            return "error: please check the amount"

    def get_balance(self):
        balance = self.__balance
        return f"available balance: ${balance}"

    def withdraw(self, amount):
        if amount < 0:
            return "amount must be positive"
        if amount > self.__balance:
            return "insufficient balance"
        self.__balance -= amount
        return f"withdrawn ${amount}"

    def get_account_info(self):
        return(f"""
        Name: {self.__account_holder}
        Balance: ${self.__balance}
        """)

system = BankAccount()
print(
system.deposit(50),
system.withdraw(49),
system.get_balance(),
system.withdraw(2),
system.deposit(99),
system.get_account_info(),
sep="\n"
)