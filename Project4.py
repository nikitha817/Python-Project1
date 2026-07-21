from datetime import datetime, timedelta
import json
try:
    with open("books.json", "r") as f:
        Books = json.load(f)
    with open("borrowers.json", "r") as f:
        Borrowers = json.load(f)
except FileNotFoundError:
    Books = []
    Borrowers = []
    def save_books():
        with open("books.json","w") as f:
            json.dump(Books,f,indent=4)
    def save_borrowers():
        with open("borrowers.json","w") as f:
            json.dump(Borrowers,f,indent=4)
def add_books():
    book_title = input("Enter book title: ").lower().strip()
    book_author = input("Enter book author: ").strip().lower()  
    try:
        book_quantity = int(input("Enter book quantity: "))
        book_year = int(input("Enter book year: "))
        if book_quantity < 0 or book_year < 0:
            print("Quantity and year cannot be negative. Please enter valid values.\n")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for quantity and year.\n")
        return
    
    for book in Books:
        if book["title"] == book_title and book["author"] == book_author:
            print("Book already exists. \n Update the stock instead.\n")
            return
        elif book["title"] == book_title and book["author"] != book_author:
            print("Book title already exists with a different author. \n Please check the details and try again.\n")
            return
    Books.append({
        "title": book_title,    
        "author": book_author,
        "quantity": book_quantity,
        "year": book_year
    })
    save_books()
    print("Book added successfully.\n")

def view_books():
    if not Books:
        print("No books available in the library.\n")
        return
    for book in Books:
        print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}, Year: {book['year']}")
def add_borrowers():
    borrower_name = input("Enter borrower name: ").strip().lower()
    if borrower_name == "":
        print("Borrower name cannot be empty.")
        return
    for borrower in Borrowers:
        if borrower["name"] == borrower_name:
            print("Borrower already exists.\n")
            return
    Borrowers.append({
        "name": borrower_name,
        "borrowed_books": []
    })
    save_borrowers()
    print("Borrower added successfully.\n")
def borrow_books():
    view_books()
    borrower_name = input("Enter borrower name: ").strip().lower()
    if borrower_name == "":
        print("Borrower name cannot be empty.")
        return
    borrowed_book_title = input("Enter book title to borrow: ").lower().strip()
    if borrowed_book_title == "":
        print("Borrowed book cannot be empty. ")
    borrower_book_author = input("Enter book author: ").lower().strip()
    if borrower_book_author == "":
        print("Borrower author cannot be empty.")
    for borrower in Borrowers:
        if borrower["name"] == borrower_name:
            for book in Books:
                if book["title"] == borrowed_book_title and book["author"] == borrower_book_author:
                    if (borrowed_book_title, borrower_book_author) in [(b["title"], b["author"]) for b in borrower["borrowed_books"]]:
                        print(f"{borrower_name} has already borrowed {borrowed_book_title}.\n")
                        return
                    if book["quantity"] > 0:
                        book["quantity"] -= 1
                        borrower["borrowed_books"].append({
                                "title": borrowed_book_title,
                                "author": borrower_book_author,
                                "borrowed_date": datetime.now().strftime("%Y-%m-%d"),
                                "due_date": (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")                                                                                                                                                                                                                               
                        })
                        save_books()
                        save_borrowers()
                        print(f"{borrowed_book_title} borrowed successfully by {borrower_name}.\n")
                        return
                    else:
                        print(f"{borrowed_book_title} is out of stock.\n")
                        return
            print(f"{borrowed_book_title} not found in the library.\n")
            return
    print(f"Borrower {borrower_name} not found.\n Add the borrower first before borrowing a book.\n")

def return_books():
    borrower_name = input("Enter borrower name: ").strip().lower()
    if borrower_name == "":
        print("Borrower name cannot be empty.")
        return
    returned_book_title = input("Enter book title to return: ").strip().lower()
    returned_book_author = input("Enter book author: ").strip().lower()
    for borrower in Borrowers:
        if borrower["name"] == borrower_name:
            if (returned_book_title, returned_book_author) in [(b["title"], b["author"]) for b in borrower["borrowed_books"]]:
                for book in Books:
                    if book["title"] == returned_book_title and book["author"] == returned_book_author:
                        book["quantity"] += 1
                        borrower["borrowed_books"].remove(next(b for b in borrower["borrowed_books"] if b["title"] == returned_book_title and b["author"] == returned_book_author))
                        print(f"{returned_book_title} by {returned_book_author} returned successfully by {borrower_name}.\n")
                        save_books()
                        save_borrowers()
                        return
                print(f"{returned_book_title} by {returned_book_author} not found in the library.\n")
                return
            else:
                print(f"{borrower_name} did not borrow {returned_book_title} by {returned_book_author}.\n")
                return
    print(f"Borrower {borrower_name} not found.\n There is no record of this borrower in the system.\n")
def delete_books():
    book_title = input("Enter book title to delete: ").lower().strip()
    book_author = input("Enter book author to delete: ").lower().strip()
    for book in Books:
        if book["title"] == book_title and book["author"] == book_author:
            confirmation = input("Are you sure you want to delete this book? (yes/no): ")
            if confirmation.lower() == "yes":
                if book["quantity"] == 0 and any(borrower for borrower in Borrowers if (book_title, book_author) in [(b["title"], b["author"]) for b in borrower["borrowed_books"]]):
                    print(f"Book '{book_title}' is currently borrowed and cannot be deleted.\n")
                    return
                Books.remove(book)
                print(f"Book '{book_title}' deleted successfully.\n")
                save_books()
                save_borrowers()
                return
            else:
                print("Book deletion canceled.\n")
                return
    print(f"Book '{book_title}' by '{book_author}' not found in the library.\n")
def update_stock():
    book_title = input("Enter book title to update stock: ").lower().strip()
    book_author = input("Enter book author to update stock: ").lower().strip()
    if not Books:
        print("No books available to update stock.\n")
        return
    for book in Books:
        if book["title"] == book_title and book["author"] == book_author:
            try:
                new_stock = int(input("Enter new stock quantity: "))
                if new_stock < 0:
                    print("Stock quantity cannot be negative. Please enter a valid quantity.\n")
                    return
                book["quantity"] = new_stock
                save_books()
                save_borrowers()
                print(f"Stock for {book_title} by {book_author} updated successfully.\n")
                return
            except ValueError:
                print("Invalid input. Please enter a valid number for stock quantity.\n")
                return
    print(f"Book '{book_title}' by '{book_author}' not found in the library.\n")
def main():
    while True:
        print("1. Add Books")
        print("2. View Books")
        print("3. Add Borrower")
        print("4. Borrow Books")
        print("5. Return Books")
        print("6. Delete Books")
        print("7. Update Stock")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_books()
        elif choice == '2':
            view_books()
        elif choice == '3':
            add_borrowers()
        elif choice == '4':
            borrow_books()
        elif choice == '5':
            return_books()
        elif choice == '6':
            delete_books()
        elif choice == '7':
            update_stock()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")