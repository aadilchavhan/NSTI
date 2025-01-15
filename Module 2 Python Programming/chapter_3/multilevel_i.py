# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

# class Car(Vehicle):
#     def __init__(self, make, model, year, doors):
#         super().__init__(make, model, year)

#         self.doors = doors

#     def disp(self):
#         print(f'make: {self.make}')
#         print(f'model: {self.model}')
#         print(f'year: {self.year}')
#         print(f'doors: {self.doors}')

# x = Car("Honda", "Civic", 2021, 4)
# x.disp()

"""________________________________________________"""



# class Device:
#     def __init__(self, brand, power):
#         self.brand = brand
#         self.power = power

# class Computer(Device):
#     def __init__(self, brand, power, processor, ram):
#         super().__init__(brand, power)
#         self.processor = processor
#         self.ram = ram

#     def disp(self):
#         print(f'Brand: {self.brand}')
#         print(f'Power: {self.power}W')
#         print(f'Processor: {self.processor}')
#         print(f'RAM: {self.ram}GB')

# class Laptop(Computer):
#     def __init__(self, brand, power, processor, ram, battery_life):
#         super().__init__(brand, power, processor, ram)
#         self.battery_life = battery_life

#     def disp(self):
#         super().disp()
#         print(f'Battery Life: {self.battery_life} hours')

# x = Laptop("Apple", 100, "M1", 8, 10)
# x.disp())

"""________________________________________________"""



class Material:
    def __init__(self, title, pub_year):
        self.title = title
        self.pub_year = pub_year

    def disp(self):
        print(f'Title: {self.title}')
        print(f'Publication Year: {self.pub_year}')


class Book(Material):
    def __init__(self, title, pub_year, author, book_number):
        super().__init__(title, pub_year)
        self.author = author
        self.book_number = book_number

    def disp(self):
        super().disp()
        print(f'Author: {self.author}')
        print(f'Library Book Number: {self.book_number}')


class Magazine(Material):
    def __init__(self, title, pub_year, issue_number):
        super().__init__(title, pub_year)
        self.issue_number = issue_number

    def disp(self):
        super().disp()
        print(f'Issue Number: {self.issue_number}')


book = Book("Atomic Habits", 2018, "Aadil Chuahan", "BN12345")
magazine = Magazine("Death Note", 2023, "MG34567")

book.disp()
print()  
magazine.disp()
