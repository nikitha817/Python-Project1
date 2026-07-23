# Library Management System

This is my biggest and most complex project so far! It's a complete system where you can manage a library—add books, borrow them, return them, and everything saves permanently.

## What It Does

- **Add books** - Add new books to the library inventory
- **View all books** - See all books and how many copies are available
- **Add borrowers** - Register new borrowers
- **Borrow books** - Check out a book (and it tracks who borrowed it)
- **Return books** - Return a book you borrowed
- **Update stock** - Change how many copies of a book you have
- **Delete books** - Remove a book from the system
- **Automatic tracking** - Saves borrow date and calculates due date
- **Error checking** - Won't let you do impossible things (like borrow a book that's out of stock)

## Features

✓ Add books and borrowers  
✓ Check book availability  
✓ Track who borrowed what  
✓ Calculate due dates automatically  
✓ Prevent duplicate books and borrowers  
✓ **Save data permanently in JSON files**  
✓ Error handling so it doesn't crash  
✓ Nice formatted menu interface  

## How to Run

```bash
python Project4.py
```

Choose an option from the menu and follow the instructions!

## What Makes This Project Cool

The biggest thing: **The data doesn't disappear when you close the program!**

When you add a book or borrow something, it saves to JSON files (`books.json` and `borrowers.json`). When you run the program again, all your data is there. This is how real systems work!

## What I Learned

- **JSON files** - How to save Python dictionaries to files and load them back
- **File handling** - Reading from files, writing to files, handling errors
- **Exception handling** - Using try-except to catch errors
- **Datetime module** - Working with dates and calculating due dates
- **Complex data structures** - Nested dictionaries and lists
- **Data validation** - Checking for duplicates, availability, etc.
- **CRUD operations** - Create, Read, Update, Delete (all 4 operations!)
- **Error messages** - Telling users what went wrong in a friendly way

## Code Structure

**Key functions:**
- `add_book()` - Add a new book
- `view_books()` - Display all books
- `add_borrower()` - Register a new borrower
- `borrow_book()` - Check out a book
- `return_book()` - Return a borrowed book
- `update_stock()` - Change inventory count
- `delete_book()` - Remove a book
- `save_data()` - Save to JSON files
- `load_data()` - Load from JSON files

## Data Stored in JSON

```json
{
  "books": {
    "1984": {
      "author": "George Orwell",
      "copies": 5,
      "borrowed": 2
    }
  },
  "borrowers": {
    "Raj": {
      "book": "1984",
      "borrow_date": "2026-07-23",
      "due_date": "2026-08-06"
    }
  }
}
```

## Challenges I Faced

- **JSON handling** - Learning how to convert Python objects to JSON and back
- **Datetime** - Calculating due dates correctly
- **Error handling** - Deciding what errors to catch and how to handle them
- **Duplicate prevention** - Making sure the same book isn't added twice
- **Data persistence** - Making sure data actually saves and loads correctly
- **Menu management** - Making a responsive menu that handles all operations

## Example Workflow

```
===== Library Management =====
1. Add Book
2. View Books
3. Add Borrower
4. Borrow Book
5. Return Book
6. Update Stock
7. Delete Book
8. Exit

Choose: 1

Enter book name: Python Basics
Enter author: John Smith
How many copies? 3

Book added! ✓

Choose: 4
Enter borrower name: Priya
Enter book to borrow: Python Basics

Book borrowed until 2026-08-06 ✓
```

## Things I Could Add Later

- Search for books by name or author
- View borrower history (all books they've ever borrowed)
- Calculate fines for overdue books
- Renew a book (extend due date)
- Display library statistics

## Why This Matters

This is a real-world project structure. Libraries, banks, hospitals—they all use systems like this! The main skills here are:
- **Persistence** - Data survives after the program closes
- **Scalability** - Can handle many books and borrowers
- **Reliability** - Error handling so nothing breaks
- **User-friendly** - Menu system that's easy to navigate

## Lessons Learned

1. **File I/O is important** - Most real programs save and load data
2. **Error handling saves you** - JSON files can get corrupted; good error handling prevents crashes
3. **Validation matters** - Checking for duplicates prevents data corruption
4. **Good structure = easy maintenance** - When code is organized into functions, it's easy to fix bugs and add features

This project took me from "coding practice" to "actually building something useful." I'm proud of it! 🚀