class BankAccount:
    bank_accounts = {"Current": {}, "Saving": {}}

    """ This class creates a bank account that can be either a currents or savings account."""

    def __init__(self, account_number, balance=0, interest=0):
        self.account_number = account_number
        self.balance = balance
        self.interest = interest

    def currents_account(self, account_number, balance):
        if account_number not in BankAccount.bank_accounts.keys():
            BankAccount.bank_accounts["Current"][account_number] = balance

    def savings_account(self, account_number, balance, interest):
        if account_number not in BankAccount.bank_accounts.keys():
            BankAccount.bank_accounts["Saving"][account_number] = [balance, interest]


class Actions:
    def __init__(self, type_of_acc, amount, interest=0):
        self.amount = amount
        self.interest = interest
        self.type_of_acc = type_of_acc

    def deposit(self, amount, account_number):
        if self.type_of_acc == "Current":
            BankAccount.bank_accounts["Current"][account_number] += amount
        elif self.type_of_acc == "Saving":
            BankAccount.bank_accounts["Saving"][account_number][0] += amount

    def withdraw(self, amount, account_number_current, account_number_savings=''):
        if self.type_of_acc == "Current":
            BankAccount.bank_accounts["Current"][account_number_current] -= amount
        elif self.type_of_acc == "Saving":
            BankAccount.bank_accounts["Saving"][account_number_savings][0] -= amount
            BankAccount.bank_accounts["Current"][account_number_current] += amount

    def get_balance(self, account_number):
        if self.type_of_acc == "Current":
            current_balance = BankAccount.bank_accounts["Current"][account_number]
            return current_balance
        elif self.type_of_acc == "Saving":
            return BankAccount.bank_accounts["Saving"][account_number][0]

    def calculate_interest(self, account_number):
        balance = BankAccount.bank_accounts["Saving"][account_number][0]
        interest_percent = BankAccount.bank_accounts["Saving"][account_number][1]
        interest = balance * (interest_percent / 100)
        BankAccount.bank_accounts["Saving"][account_number][0] += interest
        return interest


def __main__():
    while True:
        print("---Welcome to our atm!---")
        print("---If you would like to access your current account---\n   Press 1")
        print("---If you would like to access your savings account---\n   Press 2")
        print("---To exit---\n   Press 3")
        user_action = input()
        if user_action == "1":
            while True:
                if not BankAccount.bank_accounts["Current"]:
                    acc_num = input("Please enter an account number:")
                    balance = int(input("Please enter your starting balance:"))
                    bank_acc_instance = BankAccount(acc_num, balance)
                    bank_acc_instance.currents_account(acc_num, balance)
                acc_number = acc_num
                acc_balance = balance
                print("---If you would like to deposit---\n   Press 1")
                print("---If you would like to withdraw---\n   Press 2")
                print("---If you would like to get your balance---\n   Press 3")
                print("---To exit---\n   Press 4")
                current_task = input()
                if current_task == "1":
                    amount = int(input("Please enter an amount to deposit:"))
                    bank_acc_action = Actions("Current", amount)
                    bank_acc_action.deposit(amount, acc_number)
                    print(f"Successfully deposited {amount} bgn in currents account with account number: {acc_number}")
                elif current_task == "2":
                    amount = int((input("Please enter an amount to withdraw:")))
                    if amount <= BankAccount.bank_accounts["Current"][acc_number]:
                        bank_acc_action = Actions("Current", amount)
                        bank_acc_action.withdraw(amount, acc_number)
                        print(f"Successfully withdrawn {amount} "
                              f"bgn from currents account with account number: {acc_number}")
                    else:
                        print("Insufficient funds!")
                elif current_task == "3":
                    bank_acc_action = Actions("Current", acc_number, acc_balance)
                    balance = bank_acc_action.get_balance(acc_number)
                    print(f"Account with account number: {acc_number} has a current balance: {balance} bgn.")
                elif current_task == "4":
                    break
                else:
                    print("Please enter a valid option!")
        elif user_action == "2":
            while True:
                if not BankAccount.bank_accounts["Saving"]:
                    acc_num_savings = input("Please enter an account number:")
                    balance_savings = int(input("Please enter your starting balance:"))
                    interest_rate = int(input("Please enter your interest rate:"))
                    bank_acc_instance = BankAccount(acc_num_savings, balance_savings, interest_rate)
                    bank_acc_instance.savings_account(acc_num_savings, balance_savings, interest_rate)
                acc_number_savings = acc_num_savings
                acc_balance_savings = balance_savings
                interest_rate_percent = interest_rate

                print("---If you would like to deposit---\n   Press 1")
                print("---If you would like to withdraw---\n   Press 2")
                print("---If you would like to get your balance---\n   Press 3")
                print("---If you would like to get your interest---\n   Press 4")
                print("---To exit---\n   Press 5")
                current_task_savings = input()
                if current_task_savings == "1":
                    amount = int(input("Please enter an amount to deposit:"))
                    bank_acc_action = Actions("Saving", amount)
                    bank_acc_action.deposit(amount, acc_number_savings)
                    print(f"Successfully deposited {amount} bgn "
                          f"in savings account with account number: {acc_number_savings}")
                elif current_task_savings == "2":
                    amount = int((input("Please enter an amount to withdraw:")))
                    if amount <= BankAccount.bank_accounts["Saving"][acc_number_savings][0]:
                        bank_acc_action = Actions("Saving", amount, interest_rate_percent)
                        bank_acc_action.withdraw(amount, acc_number, acc_number_savings)
                        print(
                            f"Successfully withdrawn {amount} bgn from savings "
                            f"account with account number: {acc_number_savings}")
                    else:
                        print("Insufficient funds!")
                elif current_task_savings == "3":
                    bank_acc_action = Actions("Saving", acc_number_savings, acc_balance_savings)
                    balance = bank_acc_action.get_balance(acc_number_savings)
                    print(f"Account with account number: {acc_number_savings} has a current balance: {balance:.2f} bgn.")
                elif current_task_savings == "4":
                    bank_acc_action = Actions("Saving", acc_balance_savings, interest_rate_percent)
                    interest = bank_acc_action.calculate_interest(acc_number_savings)
                    print(f"{interest:.2f} bgn of interest has been added to your savings account!")
                elif current_task_savings == "5":
                    break
                else:
                    print("Please enter a valid option!")
        elif user_action == "3":
            print("Have a nice day!")
            break
        else:
            print("Please enter a valid option!")


if __name__ == "__main__":
    __main__()
