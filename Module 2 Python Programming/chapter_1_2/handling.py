# file =open ("aadil.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open ("aadil.text", "r") as file:
#     content = file.read()
#     print(content)

# with open ("aadil.txt","r") as file:
#     for line in file:
#         print(line.strip())

# with open ("aadil.text", "r") as file:
#     content = file.read(13)
#     print(content)

# with open("aadil.txt", "w") as file:
#     file.write("hello , my name is aadil")

# with open ("aadil.txt", "a") as file:
#     file.write("\n this is second line. ")

# with open("aadil.txt", "r") as file:
#     file.read(5)
#     file.seek(8)
#     print(file.read())
#     print(file.tell())

# try:
#     with open ("aadil.txt" , "r") as file:\
#     print(file.read())
# except FileNotFoundError:
#     print("File is not availabe")
# finally:
#     print("code is executed")

# import os
# if os.path.exists("abc.txt"):
#     os.remove("abc.txt")
#     print("file is deleted")
# else:
#     print("file not found")


                    
                    # File Handling

import os

def menu():
    print("NSTI Book Store")
    print("1. Add a book:")
    print("2. view books:")
    print("3. search for book:")
    print("4. Delete a book") 
    print("5. Exit")

    #add a new book

def add_new_book(filename):
        try:
            with open(filename, "a") as file:
                title=input("Enter the book title: ")
                author=input("Enter the author:")
                price=input("Enter the price: ")
                book=f'{title},{author},{price}\n'
                file.write(book)
                print("Book added successfully.")
        except Exception as e:
            print(f' An Error Ocuured:{e}')
            
def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open (filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                            try:
                                title,author,price=book.strip().split(',')
                                print(f'Title: {title}, Author : {author}, Price: {price}')
                            except ValueError:
                                print(f"skipping malformed line: {book.strip()}")
                else:
                    print("No record found...")
        else:
            print("inventory file does not exists.")

    except Exception as e:
        print(f"An error ocuured: {e}:")

def search_book(filename):
    try:
        if os.path.exists(filename):
            search=input("Enter the book name: ")
            with open (filename, "r") as file:
                books=file.readlines()
                found=False
                for book in books:
                        title,author,price=book.strip().split(",")
                        if title==search:
                            print(f'Found-Title:{title}, Author is: {author}, PRICE OF THE BOOK: {price}\n ')
                            found=True
                            break
                if not found:
                    print("Book not found")
        else:
            print("Inventory file does not exist.")

    except Exception as e:
        print(f" An Error occured: {e}")

def delete_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the title of book:" ).lower()
            with open(filename, "r") as file:
                books = file.readlines()

            with open(filename, "w") as file:
                deleted = False
                for book in books:
                    title, author, price = book.strip().split(",")
                    if title != title1:
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

# In your main function, call the delete_book function

def main():
    filename = "aadil.txt"
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
            book_to_delete = input("Enter the book you want to delete: ")
            delete_book(filename)
        elif choice == "5":
            print("Exiting the code.")
        else:
            print("Invalid choice.")
            break

if __name__ == "__main__":
    main()



