# Project8
# To-Do List

A simple command-line tool to manage your daily tasks. You can add tasks, view all tasks, remove completed ones, and keep track of what you need to do.

## What It Does

- **Add tasks** - Enter new tasks to your to-do list
- **View tasks** - See all tasks with numbers for easy reference
- **Remove tasks** - Delete completed or unwanted tasks by number
- **Menu-driven interface** - Easy navigation with numbered options

## Features

- Add unlimited tasks
- View all tasks with numbering (numbered 1, 2, 3, etc.)
- Remove tasks by their number (not by typing the whole name)
- Input validation (checks for empty task entry)
- Case-sensitive task handling (preserves how you typed it)
- Persistent menu (keeps running until you exit)
- Clean, formatted output

## How to Run

```bash
python todo_list.py
```

Then follow the menu to add, view, or remove tasks.

## Example Usage

```
========================================
To-Do List
========================================
|1. Add Task
|2. Veiw Task
|3. Remove Task
|4. Exit

Enter your choice: 1
Enter task description: Buy groceries
Task added: Buy groceries

Enter your choice: 1
Enter task description: Complete Python project
Task added: Complete Python project

Enter your choice: 1
Enter task description: Call mom
Task added: Call mom

Enter your choice: 2
Current tasks:
1. Buy groceries
2. Complete Python project
3. Call mom

Enter your choice: 3
Current tasks:
1. Buy groceries
2. Complete Python project
3. Call mom

Enter task number to remove: 2
Removed task: Complete Python project

Enter your choice: 2
Current tasks:
1. Buy groceries
2. Call mom
```

## What I Learned

- **Lists for storing data** - Storing tasks in a simple list (not dictionaries)
- **Enumerate function** - Using enumerate() to get both index and value when printing
- **String validation** - Checking if input is empty with `if not task:`
- **Try-except for user input** - Catching ValueError when user enters non-number
- **List indexing** - Using list.pop(idx - 1) to remove by index
- **User-friendly numbering** - Showing tasks numbered 1-N instead of 0-based indexing
- **Menu-driven design** - While True loop with break to control program flow
- **Conditional logic** - If-elif-else for menu choices and range checking
- **String methods** - Using .strip() to remove whitespace from input

## Code Structure

```python
tasks = []  # Global list to store all tasks

def add_task():
    # Get task description
    # Validate input is not empty
    # Add to tasks list

def veiw_task():
    # Check if list is empty
    # Display all tasks with numbers (1, 2, 3...)

def remove_task():
    # Show all tasks
    # Ask which number to remove
    # Validate number is in range
    # Remove from list

def main():
    # Menu-driven loop
    # Call functions based on user choice
```

## Challenges I Faced

- **Index vs Display number** - Showing tasks as 1, 2, 3 but removing by index 0, 1, 2
- **Enumerate function** - Learning how to use enumerate() with start parameter
- **Input validation** - Catching ValueError and checking if task is empty
- **List bounds checking** - Making sure task number is between 1 and list length
- **Persistent menu** - Getting the menu to keep showing and accepting input
- **Task not found** - Handling when user enters a task number that doesn't exist

## Things I Could Add Later

- Mark tasks as complete without deleting
- Edit existing tasks
- Task priority levels (high, medium, low)
- Due dates for tasks
- Save tasks to a file (so they persist)
- Search for specific tasks
- Sort tasks by priority or date
- Category/project organization
- Task completion percentage

## Why This Matters

This project taught me a practical tool that people actually use! Unlike game projects, this is something a student could actually use to track their assignments.

Key learnings:
- Simple data structures (lists) can solve real problems
- User-friendly numbering matters (1-based vs 0-based)
- Validation prevents crashes
- Menu-driven apps are a common pattern
- Good organization (functions) makes code reusable

This showed me how to combine:
- Lists and iteration
- User input and validation
- Conditional logic
- Menu-driven design
- Error handling

Next: Add file persistence and task priorities! ✅