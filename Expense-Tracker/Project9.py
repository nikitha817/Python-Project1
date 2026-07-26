expenses = []
def add_expenses():
    expense_name = input("Enter expenses name: ").strip().lower()
    try:
        expense_amount = float(input("Enter expense amount: ").strip())
    except ValueError:
        print("Invalid Amount!")
        return
    expenses.append({
        'name':expense_name,
        'amount':expense_amount
    }) 
    print(f"{'name':<10}: {expense_name}\n{'amount':<10}: {expense_amount}")
def view_expenses():
    if not expenses:
        print("There are no expenses in the list")
        return
    print("=" * 40)
    print("Expenses".center(40))
    print("=" * 40)
    for expense in expenses:
        print(f"{'|Name':<10}: {expense['name']}\n{'|Amount':<10}: {expense['amount']}\n{'=' * 40}")
def delete_expenses():
    if not expenses:
        print("There are no expenses to delete")
        return
    view_expenses()    
    delete_expense = input("Enter name to delete: ").strip().lower()
    for expense in expenses:
        if delete_expense == expense['name']:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return
    print("No expenses found to delete")
def total_expenses():
    if not expenses:
        print("There are no expenses in the list")
        return
    total_sum = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses spent = {total_sum}")    
def main():
    while True:
        print("=" * 40)
        print("Expense Tracker".center(40))
        print("=" * 40)
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Total Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expenses()
        elif choice == '4':
            total_expenses()
        elif choice == '5':
            print("Thank you for using expense tracker")
            break
        else:
            print("Invalid Choice! Try again")
if __name__ == "__main__":
    main()