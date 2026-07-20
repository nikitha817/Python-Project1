Books = []
Borrowers =[]
def add_books():
    book_title = input("Enter book title: ")
    book_author = input("Enter book author: ")
    book_quantity = int(input("Enter book quantity: "))
    book_year = int(input("Enter book year: "))
    for book in Books:
        if book["title"] == book_title and book["author"] == book_author:
            print("Book already exists. \n Update the stock instead.\n")
            return
        elif book["title"] == book_title and book["author"] != book_author:
            print("Book already exists with a different author. \n Update the stock instead.\n")
            return
        elif book["title"] != book_title and book["author"] == book_author:
            print("Book already exists with a different title. \n Update the stock instead.\n")
            return
        else:
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

def add_borrowers():
    view_books()
    borrower_name = input("Enter borrower name: ")
    borrower_id = input("Enter borrower ID: ")
    Borrowers.append({
        "name": borrower_name,
        "id": borrower_id,
        "borrowed_books": [],
        "borrow_date": None
    })
    print("Borrower added successfully.\n")

def return_books():
    pass

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