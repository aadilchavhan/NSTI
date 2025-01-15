                    # Date:- 18-12-2024

#  Task 1: Define a class Student with attributes name and roll_number. Create an object of this class and print its attributes.

# class Student:
#     # institute="NSTI"

#     def __init__(self,name,roll_number):
#         self.name=name
#         self.roll_number=roll_number

# NSTI=Student("Aadil_Chauhan",22)

# print(f'{NSTI.name},{NSTI.roll_number}')

 

# # Task 2: Define a class Rectangle with attributes length and width. Add a method area to calculate the area of the rectangle. Create an object and call the method.

# class Rectangle:

#     def __init__(self,length,width):
#         self.length= length
#         self.width= width
    
#     def area(self):
#         return self.length * self.width

# rect = Rectangle(5, 3)

# print("Area of the rectangle:", rect.area())


# # Task 3: Define a class Circle with a method circumference to calculate the circumference and another method area to calculate the area. Use π = 3.14.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def circumference(self):
#         return 2 * 3.14 * self.radius

#     def area(self):
#         return 3.14 * (self.radius ** 2)


# c = Circle(5)
# print("Circumference:", c.circumference())
# print("Area:", c.area())



# # Task 4: Define a class Employee with a class attribute company_name and instance attributes name and salary. Print both class and instance attributes.

# class Employee:
#     company_name = "TCS"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# e = Employee("Aadil", 50000)
# print("Company Name:", e.company_name)
# print("Employee Name:", e.name)
# print("Employee Salary:", e.salary)


# # Task 5: Create a base class Animal with a method sound. Create a derived class Dog that overrides the sound method. Call the method from an object of Dog.

# class Animal:
#     def sound(self):
#         return "Some sound"

# class Dog():
#     def sound(self):
#         return "Bark"

# d = Dog()
# print("Dog Sound:", d.sound())


# Task 6: Create a class Book with attributes title and author. Add a method is_same_author that compares the authors of two book objects.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def is_same_author(self, other_book):
#         return self.author == other_book.author


# book1 = Book("Book One", "Author A")
# book2 = Book("Book Two", "Author A")
# book3 = Book("Book Three", "Author B")

# print("Book1 and Book2 have the same author:", book1.is_same_author(book2)) 
# print("Book1 and Book3 have the same author:", book1.is_same_author(book3))  


#  # Task 1 Write a class BankAccount with a private balance attribute. 
#         Implement methods to deposit, withdraw, and check the balance, ensuring that the balance cannot be directly accessed from outside the class.

# Create a class Student with private attributes __name and __grade. Write a method to check if the student has passed (grade >= 50) and use a setter method to update the grade.


# class Student:
#     def __init__(self, name, grade):
#         self.name= name
#         self.grade= grade

#     # def __name
