import argparse
import csv
import pandas as pd
import numpy as np
import os
import datetime


class Transaction:
    def __init__(self, trans_type, category, amount, description):
        self.trans_type = trans_type
        self.category = category
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"{self.trans_type.capitalize()}: {self.category} - {self.amount:.2f} - {self.description}"
    
    def to_dict(self):
        return {
            'timestamp': datetime.datetime.now(),
            'type': self.trans_type,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }


def parse_arguments():
    parser = argparse.ArgumentParser(description="Command line expense tracker.")
    parser.add_argument("file", help="CSV Path")
    parser.add_argument("--expense", nargs=3, metavar=("category", "amount", "description"),
                        help="Add expense")
    parser.add_argument("--income", nargs=2, metavar=("amount", "description"),
                        help="Add income")
    parser.add_argument("--summary", action="store_true", help="Summary.")
    parser.add_argument("--stats", action="store_true", help="Statistics")
    return parser.parse_args()

def read_csv_file(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        data = pd.read_csv(file_path)
    else:
        data = pd.DataFrame(columns=['timestamp', 'type', 'category', 'amount', 'description'])
    return data

def write_csv_file(file_path, data):
    data.to_csv(file_path, index=False)

def add_expense(data, expense_data):
    category, amount, description = expense_data
    expense = Transaction("expense", category, float(amount), description)

    return data._append(expense.to_dict(), ignore_index=True)

def add_income(data, income_data):
    amount, description = income_data
    income = Transaction("income", "", float(amount), description)

    return data._append(income.to_dict(), ignore_index=True)

def display_summary(data):
    income = data[data["type"] == "income"]["amount"].sum()
    expenses = data[data["type"] == "expense"]["amount"].sum()
    print(f"Total Income: {income:.2f}")
    print(f"Total Expenses: {expenses:.2f}")
    print(f"Net: {income - expenses:.2f}")

def display_statistics(data):
    expenses = data[data["type"] == "expense"]["amount"]
    mean_expense = np.mean(expenses)
    std_expense = np.std(expenses)

    print("Expenses statistics:")
    print(f"Mean expense: {mean_expense:.2f}")
    print(f"Standard deviation: {std_expense:.2f}")

    expenses_by_category = data[data["type"] == "expense"].groupby("category")["amount"].sum()
    print("\nExpenses by category:")
    print(expenses_by_category)

def main():
    args = parse_arguments()

    data = read_csv_file(args.file)

    if args.expense:
        data = add_expense(data, args.expense)
        write_csv_file(args.file, data)

    if args.income:
        data = add_income(data, args.income)
        write_csv_file(args.file, data)

    if args.summary:
        display_summary(data)

    if args.stats:
        display_statistics(data)

if __name__ == "__main__":
    main()
