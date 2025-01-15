import os

def menu():
    print("Library")
    print("1. Add a book")
    print("2. View books")
    print("3. Search for a book")
    print("4. Delete a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

# Task 1: Add a new book
def add_new_book(filename):
    try:
        with open(filename, "a") as file:
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            publication_year = input("Enter the year: ")
            book = f'{title},{author},{publication_year},available\n'
            file.write(book)
            print("Book added successfully.")
    except Exception as e:
        print(f'An Error Occurred: {e}')

# Task 2: Search for a book
def search_book(filename):
    try:
        if os.path.exists(filename):
            search = input("Enter the book name: ")
            with open(filename, "r") as file:
                books = file.readlines()
                found = False
                for book in books:
                    title, author, publication_year, status = book.strip().split(",")
                    if title.lower() == search.lower():
                        print(f'Found - Title: {title}, Author: {author}, Year of publication: {publication_year}, Status: {status}')
                        found = True
                        break
                if not found:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f"An Error occurred: {e}")

# Task 3: View all books
def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                books = file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                        try:
                            title, author, publication_year, status = book.strip().split(',')
                            print(f'Title: {title}, Author: {author}, Year of publication: {publication_year}, Status: {status}')
                        except ValueError:
                            print(f"Skipping malformed line: {book.strip()}")
                else:
                    print("No record found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 4: Delete a book
def delete_book(filename):
    try:
        if os.path.exists(filename):
            title1 = input("Enter the title of the book: ").lower()
            with open(filename, "r") as file:
                books = file.readlines()

            with open(filename, "w") as file:
                deleted = False
                for book in books:
                    title, author, publication_year, status = book.strip().split(",")
                    if title.lower() != title1:
                        file.write(book)
                    else:
                        deleted = True
                
                if deleted:
                    print("Book deleted successfully.")
                else:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 5: Borrow a book
def borrow_book(filename, borrowed_filename):
    try:
        if os.path.exists(filename):
            book_to_borrow = input("Enter the title of the book you want to borrow: ").lower()
            with open(filename, "r") as file:
                books = file.readlines()

            with open(filename, "w") as file:
                borrowed = False
                for book in books:
                    title, author, publication_year, status = book.strip().split(",")
                    if title.lower() == book_to_borrow and "available" in status:
                        file.write(f'{title},{author},{publication_year},borrowed\n')
                        with open(borrowed_filename, "a") as borrowed_file:
                            borrowed_file.write(f'{title},{author},{publication_year}\n')
                        borrowed = True
                    else:
                        file.write(book)
                
                if borrowed:
                    print("Book borrowed successfully.")
                else:
                    print("Book not available for borrowing or not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Task 6: Return a book
def return_book(filename, borrowed_filename):
    try:
        if os.path.exists(filename) and os.path.exists(borrowed_filename):
            book_to_return = input("Enter the title of the book you want to return: ").lower()
            with open(filename, "r") as file:
                books = file.readlines()

            with open(filename, "w") as file:
                returned = False
                for book in books:
                    title, author, publication_year, status = book.strip().split(",")
                    if title.lower() == book_to_return and "borrowed" in status:
                        file.write(f'{title},{author},{publication_year},available\n')
                        returned = True
                    else:
                        file.write(book)

            if returned:
                with open(borrowed_filename, "r") as borrowed_file:
                    borrowed_books = borrowed_file.readlines()
                with open(borrowed_filename, "w") as borrowed_file:
                    for book in borrowed_books:
                        if book_to_return not in book.lower():
                            borrowed_file.write(book)
                print("Book returned successfully.")
            else:
                print("Book not found in borrowed list.")
        else:
            print("Inventory or borrowed file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    filename = "books.txt"
    borrowed_filename = "borrowed_books.txt"
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_new_book(filename)
        elif choice == "2":
            view_inventory(filename)
        elif choice == "3":
            search_book(filename)
        elif choice == "4":
            delete_book(filename)
        elif choice == "5":
            borrow_book(filename, borrowed_filename)
        elif choice == "6":
            return_book(filename, borrowed_filename)
        elif choice == "7":
            print("Exiting the code.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

