# class Animal:
#     def animal(self):
#         print("This is Main/Base/Parent Class")

# class Dog(Animal):
#     def dog(self):
#         print("This is Child/Derived Class")

# x=Dog()

# x.animal()
# x.dog()

"""________________________________________________"""

# class Birds:
#     def bird(self):
#         print("This is Main/Base/Parent Class")

# class Peacock(Birds):  # Inherit from Birds class
#     def peacock(self):
#         print("This is the Peacock class")


# if __name__ == "__main__":
#     b = Birds()
#     p = Peacock()

#     b.bird()  
#     p.bird() 
#     p.peacock() 

"""________________________________________________"""


# class Maths:
#     def addition(self, a, b):
#         return a + b
    
# class Multi(Maths):
#     def multi(self, a, b):
#         return a * b

# class Sub(Maths):
#     def sub(self, a, b):
#         return a - b

# class Div(Maths):
#     def div(self, a, b):
#         if b != 0:
#             return a / b
#         else:
#             return "Division by zero is not allowed"

# if __name__ == "__main__":
#     b = Maths()  

#     D1 = int(input("Enter number: "))
#     D2 = int(input("Enter number: "))

#     print("Addition =", b.addition(D1, D2)) 

"""________________________________________________"""



class Library:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')

class Book(Library):
    def __init__(self, title, author, price, year):
        super().__init__(title, author, price)
        self.year = year

    def display(self):
        super().display()
        print(f'Year: {self.year}')


if __name__ == "__main__":

    book = Book("Automic Habit", "Aadil Chauhan", 499, 2018)
    book.display()
































