# Simple Banking System Simulation
# Features: Create Account, Check Balance, Deposit, Withdraw, View All Accounts, Highest Balance Account

accounts = []   # List of dictionaries to store accounts
next_account_number = 1001   # Auto-generated account number


def create_account(holder_name, initial_balance):
    #Create a new account with holder name and initial balance
    global next_account_number
    account = {
        "account_number": next_account_number,
        "holder_name": holder_name,
        "balance": initial_balance
    }
    accounts.append(account)
    print(f" Account created! Account Number: {next_account_number}")
    next_account_number += 1


def find_account(account_number):
    #Find an account by account number
    for account in accounts:
        if account["account_number"] == account_number:
            return account
    return None


def check_balance(account_number):
    #Check balance of an account
    account = find_account(account_number)
    if account:
        print(f" Balance for {account['holder_name']} (Acc {account_number}): {account['balance']}")
    else:
        print(" Account not found.")


def deposit_money(account_number, amount):
    #Deposit money into an account
    account = find_account(account_number)
    if account:
        account["balance"] += amount
        print(f" Deposited {amount}. New Balance: {account['balance']}")
    else:
        print(" Account not found.")


def withdraw_money(account_number, amount):
    #Withdraw money with balance check
    account = find_account(account_number)
    if account:
        if account["balance"] >= amount:
            account["balance"] -= amount
            print(f" Withdrawn {amount}. New Balance: {account['balance']}")
        else:
            print(" Insufficient balance.")
    else:
        print(" Account not found.")


def view_all_accounts():
    #Display all accounts with balances
    if not accounts:
        print(" No accounts available.")
    else:
        print("\n All Accounts:")
        for account in accounts:
            print(f"Acc No: {account['account_number']}, Name: {account['holder_name']}, Balance: {account['balance']}")


def highest_balance_account():
    #Find account with highest balance
    if not accounts:
        print(" No accounts available.")
    else:
        highest = max(accounts, key=lambda acc: acc["balance"])
        print(f"Highest Balance: {highest['holder_name']} (Acc {highest['account_number']}), Balance: {highest['balance']}")


def menu():
    #Menu-driven interface
    while True:
        print("\n===== Banking Menu =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View All Accounts")
        print("6. Highest Balance Account")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            create_account(name, balance)
        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            check_balance(acc_num)
        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            deposit_money(acc_num, amount)
        elif choice == "4":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            withdraw_money(acc_num, amount)
        elif choice == "5":
            view_all_accounts()
        elif choice == "6":
            highest_balance_account()
        elif choice == "7":
            print(" Exiting Banking System. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")


# Run the banking system
if __name__ == "__main__":
    menu()
