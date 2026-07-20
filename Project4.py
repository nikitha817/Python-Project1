from datetime import datetime, timedelta
Books = []
Borrowers =[]
def add_books():
    book_title = input("Enter book title: ")
    book_author = input("Enter book author: ")
    book_quantity = int(input("Enter book quantity: "))
    book_year = int(input("Enter book year: "))
    for book in Books:
        if book["title"] == book_title.lower() and book["author"] == book_author.lower():
            print("Book already exists. \n Update the stock instead.\n")
            return
        elif book["title"] == book_title.lower() and book["author"] != book_author.lower():
            print("Book title already exists with a different author. \n Please check the details and try again.\n")
            return
    Books.append({
        "title": book_title,    
        "author": book_author,
        "quantity": book_quantity,
        "year": book_year
    })
    print("Book added successfully.\n")

def view_books():
    for book in Books:
        print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}, Year: {book['year']}")
def borrow_books():
    view_books()
    borrower_name = input("Enter borrower name: ")
    borrowed_book_title = input("Enter book title to borrow: ").lower()
    for borrower in Borrowers:
        if borrower["name"] == borrower_name:
            for book in Books:
                if book["title"] == borrowed_book_title:
                    if book["quantity"] > 0:
                        book["quantity"] -= 1
                        borrower["borrowed_books"].append(borrowed_book_title)
                        print(f"{borrowed_book_title} borrowed successfully by {borrower_name}.\n")
                        borrower["borrow_date"] = datetime.now()
                        borrower["return_date"] = borrower["borrow_date"] + timedelta(days=14)
                        return
                    else:
                        print(f"{borrowed_book_title} is out of stock.\n")
                        return
            print(f"{borrowed_book_title} not found in the library.\n")
            return
    print(f"Borrower {borrower_name} not found.\n Add the borrower first before borrowing a book.\n")

def return_books():
    borrower_name = input("Enter borrower name: ")
    returned_book_title = input("Enter book title to return: ").lower()
    for borrower in Borrowers:
        if borrower["name"] == borrower_name:
            if returned_book_title in borrower["borrowed_books"]:
                for book in Books:
                    if book["title"] == returned_book_title:
                        book["quantity"] += 1
                        borrower["borrowed_books"].remove(returned_book_title)
                        print(f"{returned_book_title} returned successfully by {borrower_name}.\n")
                        return
                print(f"{returned_book_title} not found in the library.\n")
                return
            else:
                print(f"{borrower_name} did not borrow {returned_book_title}.\n")
                return
    print(f"Borrower {borrower_name} not found.\n There is no record of this borrower in the system.\n")
def delete_books():
    pass
def update_stock():
    pass
def main():
    while True:
        print("1. Add Books")
        print("2. View Books")
        print("3. Add Borrowers")
        print("4. Return Books")
        print("5. Delete Books")
        print("6. Update Stock")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_books()
        elif choice == '2':
            view_books()
        elif choice == '3':
            add_borrowers()
        elif choice == '4':
            return_books()
        elif choice == '5':
            delete_books()
        elif choice == '6':
            update_stock()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")