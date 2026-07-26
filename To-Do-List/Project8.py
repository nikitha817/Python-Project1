tasks = []

def add_task():
    """Prompt the user to add a task and store it in the tasks list."""
    task = input("Enter task description: ").strip()
    if not task:
        print("No task entered. Cancelling.")
        return
    tasks.append(task)
    print(f"Task added: {task}")

def veiw_task():
    """Display current tasks."""
    if not tasks:
        print("No tasks in the list.")
        return
    print("Current tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def remove_task():
    """Remove a task by its number shown in veiw_task."""
    if not tasks:
        print("No tasks to remove.")
        return
    veiw_task()
    try:
        idx = int(input("Enter task number to remove: ").strip())
    except ValueError:
        print("Invalid number.")
        return
    if 1 <= idx <= len(tasks):
        removed = tasks.pop(idx - 1)
        print(f"Removed task: {removed}")
    else:
        print("Task number out of range.")
def main():
    while True:
        print("=" * 40)
        print("To-Do List".center(40))
        print("=" * 40)
        print("|1. Add Task")
        print("|2. Veiw Task")
        print("|3. Remove Task")
        print("|4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            veiw_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Thank you for using To-Do List!")
            break
        else:
            print("Invalid choice! Try again")
if __name__ == "__main__":
    main()