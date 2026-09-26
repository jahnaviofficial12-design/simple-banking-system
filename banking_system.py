import random
from datetime import datetime

accounts = {}


def generate_account_number():
    return str(random.randint(100000, 999999))


def create_account():
    print("\n===== CREATE ACCOUNT =====")

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    pin = input("Create a 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("Please enter a valid 4-digit PIN.")
        return

    account_number = generate_account_number()

    while account_number in accounts:
        account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)
    print("Please remember your account number and PIN.")


def add_transaction(account_number, message):
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    transaction = current_time + " - " + message
    accounts[account_number]["transactions"].append(transaction)


def login():
    print("\n===== LOGIN =====")

    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])
            account_menu(account_number)
        else:
            print("Incorrect PIN.")
    else:
        print("Account not found.")


def check_balance(account_number):
    balance = accounts[account_number]["balance"]
    print("\nCurrent Account Balance: ₹", balance)


def deposit_money(account_number):
    print("\n===== DEPOSIT MONEY =====")

    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        accounts[account_number]["balance"] += amount

        add_transaction(
            account_number,
            "Deposited ₹" + str(amount)
        )

        print("Money deposited successfully.")
        print("Current Balance: ₹", accounts[account_number]["balance"])
    else:
        print("Enter a valid amount.")


def withdraw_money(account_number):
    print("\n===== WITHDRAW MONEY =====")

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[account_number]["balance"] -= amount

        add_transaction(
            account_number,
            "Withdrawn ₹" + str(amount)
        )

        print("Money withdrawn successfully.")
        print("Current Balance: ₹", accounts[account_number]["balance"])


def transfer_money(account_number):
    print("\n===== TRANSFER MONEY =====")

    receiver = input("Enter receiver account number: ")

    if receiver not in accounts:
        print("Receiver account not found.")
        return

    if receiver == account_number:
        print("You cannot transfer money to the same account.")
        return

    amount = float(input("Enter amount to transfer: ₹"))

    if amount <= 0:
        print("Enter a valid amount.")
    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[account_number]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        add_transaction(
            account_number,
            "Transferred ₹" + str(amount) + " to account " + receiver
        )

        add_transaction(
            receiver,
            "Received ₹" + str(amount) + " from account " + account_number
        )

        print("Money transferred successfully.")
        print("Current Balance: ₹", accounts[account_number]["balance"])


def transaction_history(account_number):
    print("\n===== TRANSACTION HISTORY =====")

    transactions = accounts[account_number]["transactions"]

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)


def change_pin(account_number):
    print("\n===== CHANGE PIN =====")

    old_pin = input("Enter current PIN: ")

    if old_pin == accounts[account_number]["pin"]:
        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            accounts[account_number]["pin"] = new_pin

            add_transaction(
                account_number,
                "PIN changed successfully"
            )

            print("PIN changed successfully.")
        else:
            print("Please enter a valid 4-digit PIN.")
    else:
        print("Incorrect current PIN.")


def account_menu(account_number):
    while True:
        print("\n===== ACCOUNT MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit_money(account_number)

        elif choice == "3":
            withdraw_money(account_number)

        elif choice == "4":
            transfer_money(account_number)

        elif choice == "5":
            transaction_history(account_number)

        elif choice == "6":
            change_pin(account_number)

        elif choice == "7":
            print("\nLogged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n==============================")
        print("     SIMPLE BANKING SYSTEM")
        print("==============================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            print("\nThank you for using Simple Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()s