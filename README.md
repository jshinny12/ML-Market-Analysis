# Expense Tracker CLI

A simple command-line expense tracker that allows users to record their income and expenses in a CSV file. The app provides summaries and simple statistics on the user's financial data.

## Installation

No additional installation steps required. Just make sure you have Python 3.x and the required libraries installed.

## Required Libraries

1. pandas (third-party)
2. numpy (third-party)

To install the required libraries, run the following command:

```bash
pip3 install pandas numpy
```

## Usage
1. <file>: Path to the CSV file to store the financial data.
2. --expense category amount description: Add an expense with category, amount, and description.
3. --income amount description: Add an income with amount and description.
4. --summary: Display a summary of income and expenses.
5. --stats: Display simple statistics on the financial data.

## Examples

Add an expense:
```bash
python3 expense_tracker.py finances.csv --expense groceries 25.50 "Weekly groceries"
```

Add an income:

```bash
python3 expense_tracker.py finances.csv --income 1000 "Salary"
```

Display a summary of income and expenses:

```bash
python3 expense_tracker.py finances.csv --summary
```

Display simple statistics on the financial data:

```bash
python3 expense_tracker.py finances.csv --stats
```

## Code Structure
1. expense_tracker.py: The main script that contains the command-line interface and functions for the expense tracker.
2. Transaction class: A class to represent individual financial transactions.
3. Functions: parse_arguments, read_csv_file, write_csv_file, add_expense, add_income, display_summary, and display_statistics for managing and analyzing financial data.
