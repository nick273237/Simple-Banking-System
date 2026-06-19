class Account:
    def __init__(self, name, account_number, initial_deposit=0):
        self.name = name
        self.account_number = account_number
        self.balance = float(initial_deposit)
        self.transactions = []

        if initial_deposit > 0:
            self.transactions.append(f"Initial deposit: ${initial_deposit:.2f}")

    def deposit(self, amount):
        if 0 >= amount:
            raise ValueError("Invalid amount")
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")



    def withdraw(self, amount):
        if amount > self.balance or amount < 1:
            raise ValueError("Invalid amount")
        self.balance -= amount
        self.transactions.append(f"Withdrawal: ${amount}")



    def transfer(self, other, amount):
        if amount > self.balance or amount <= 0:
            raise ValueError("Invalid amount")
        self.balance -= amount
        other.balance += amount
        self.transactions.append(f"Transaction sent to {other.account_number}: - ${amount}")
        other.transactions.append(f"Transaction received from {self.account_number}: + ${amount}")

    def show_info(self):
        print("-------Account Information-------")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

    def show_transactions(self):
        if len(self.transactions) > 0:
            print("-------Transaction History-------")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, name, initial_deposit):
        account = Account(name, self.next_account_number, initial_deposit)


        self.accounts[self.next_account_number] = account
        self.next_account_number += 1
        return account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def list_accounts(self):
        if not self.accounts:
            print("There are no available accounts")
        else:
            for account in self.accounts.values():
                print(account.account_number)
                print(account.name)
                print(round(account.balance, 2))
def main():
    bank = Bank()
    try:
        while True:
            print("--- Simple Banking System ---")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. View Account")
            print("6. Transaction History")
            print("7. List Accounts")
            print("8. Exit")
            choice = input("Enter your choice: ").strip()
            match choice:
                case "1":
                    name = input("What is your name? ")
                    initial_deposit = int(input("Initial deposit:"))
                    if not name.strip() or not initial_deposit or initial_deposit < 0:
                        raise ValueError("Invalid input")
                    account = bank.create_account(name, initial_deposit)
                    print("Account created successfully! ")
                    print(f"New bank account number: {account.account_number}")
                    continue
                case "2":
                    number = int(input("Account number: "))
                    amount = float(input("How much do you want to deposit? "))
                    account = bank.find_account(number)
                    if not account:
                        print("Sorry, no account found")
                        continue
                    account.deposit(amount)
                    print(f"Successfully deposited ${amount}")
                    continue
                case "3":
                    number = int(input("Account number: "))
                    amount = float(input("How much do you want to withdraw? "))
                    account = bank.find_account(number)
                    if not account:
                        print("Sorry, no account found")
                        continue
                    account.withdraw(amount)
                    print(f"Successfully withdrawn ${amount}")
                    continue
                case "4":
                    number = int(input("Account number: "))
                    number2 = int(input("What is the account number of the person you want to transfer money to? "))
                    amount = float(input("How much do you want to transfer? "))
                    account = bank.find_account(number)
                    account2 = bank.find_account(number2)
                    if not account or not account2:
                        print("Sorry, no account found")
                        continue
                    account.transfer(account2, amount)
                    print(f"Successfully transfered ${amount}")
                    continue
                case "5":
                    number = int(input("Account number: "))
                    account = bank.find_account(number)
                    if not account:
                        print("Sorry, no account found")
                    else:
                        account.show_info()
                    continue
                case "6":
                    account = bank.find_account(int(input("What is your account number? ")))
                    if not account:
                        print("Sorry, we couldn't find your account")
                    else:
                        account.show_transactions()
                    continue

                case "7":
                    bank.list_accounts()
                    continue
                case "8":
                    print("Goodbye")
                    break

    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()