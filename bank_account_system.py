"""
Bank Account Management System

This Python program simulates a basic Bank Account System that allows users to:
- Create a bank account with an initial balance
- Deposit money into the account
- Withdraw money (with balance check)
- Display account details
"""

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount >0:
            self.balance =+ amount
            print("Deposited amount successful.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount >0:
            if self.balance >= amount:
                print(f'Withdraw successful. New Balance: {self.balance}')
            else:
                print("Insufficient balance.")

    def display(self):
        print(f"Account holder: {self.account_holder}")
        print(f'Current Balance: {self.balance}')