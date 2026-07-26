# Project9
# Expense Tracker

A simple command-line tool to track your daily expenses. You can add expenses, view them, delete specific ones, and see the total amount you've spent.

## What It Does

- **Add expenses** - Enter expense name and amount
- **View all expenses** - See all expenses in a nicely formatted list
- **Delete expenses** - Remove specific expenses by name
- **Calculate total** - See total amount spent across all expenses
- **Menu-driven interface** - Easy to navigate with numbered options

## Features

- Add unlimited expenses with name and amount
- View all expenses in formatted output
- Delete expenses by typing the expense name
- Calculate total spending instantly
- Input validation (checks if amount is a valid number)
- Case-insensitive expense names (converts to lowercase)
- Persistent menu (keeps running until you exit)

## How to Run

```bash
python expense_tracker.py
```

Then follow the menu to add, view, delete, or calculate expenses.

## Example Usage

```
========================================
Expense Tracker
========================================
1. Add Expenses
2. View Expenses
3. Delete Expenses
4. Total Expenses
5. Exit

Enter your choice: 1
Enter expenses name: groceries
Enter expense amount: 500
name      : groceries
amount    : 500

Enter your choice: 1
Enter expenses name: fuel
Enter expense amount: 300
name      : fuel
amount    : 300

Enter your choice: 2
========================================
Expenses
========================================
|Name      : groceries
|Amount    : 500
========================================
|Name      : fuel
|Amount    : 300
========================================

Enter your choice: 4
Total Expenses spent = 800
```

## What I Learned

- **Lists of dictionaries** - Storing multiple expenses as dictionaries in a list
- **Dictionary key-value pairs** - Organizing data (name and amount)
- **Try-except for validation** - Catching ValueError when user enters non-number for amount
- **String methods** - Using .strip() to remove whitespace, .lower() for case-insensitive comparison
- **Loop control** - While True loop with break to exit menu
- **Conditional logic** - If-elif-else for menu choices
- **List comprehension** - Using sum() with generator expression to calculate total
- **String formatting** - Using f-strings and .center() for nice output
- **Data structure iteration** - Looping through list of dictionaries

## Code Structure

```python
expenses = []  # Global list to store all expenses

def add_expenses():
    # Get expense name and amount
    # Validate amount is a number
    # Add to expenses list

def view_expenses():
    # Check if list is empty
    # Display all expenses nicely formatted

def delete_expenses():
    # Show all expenses
    # Ask which one to delete
    # Remove from list

def total_expenses():
    # Calculate sum of all expense amounts
    # Display total

def main():
    # Menu-driven loop
    # Call functions based on user choice
```

## Challenges I Faced

- **Dictionary in list iteration** - Learning how to access values from dictionaries inside a list
- **Input validation** - Making sure the amount is a number before adding
- **Case-insensitive matching** - Converting to lowercase so "Groceries" and "groceries" are treated the same
- **Formatted output** - Getting the table-like view with proper alignment
- **List removal while iterating** - Making sure I remove the right expense
- **Menu loop control** - Getting the menu to keep running until user chooses exit

## Things I Could Add Later

- Save expenses to a file (JSON or CSV) so they don't disappear
- Edit existing expenses (change amount or name)
- Filter expenses by date
- Monthly expense reports
- Expense categories (groceries, fuel, entertainment, etc.)
- Budget limit tracking
- Export to CSV or PDF

## Why This Matters

This project taught me how to build a practical app that actually does something useful! Unlike the calculator or game, this is something a real person could use.

Key learnings:
- Real apps need data storage (lists of dictionaries)
- User input validation is crucial
- Good formatting makes apps professional
- Menu-driven apps are common pattern in programming

This showed me how to combine multiple concepts (loops, conditionals, dictionaries, validation) into one useful tool.

Next: Add file persistence so expenses are saved! 💾