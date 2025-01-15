### Calling Methods of same name through Function ###

# class A:
#     def x(self):
#         return "hi"
    
# class B:
#     def x(self):
#         return "Aadil Chauhan"
    
# def z(s):
#     return s.x()

# r = A()
# a = B()

# print(z(r))
# print(z(a))



# calling Methods of same name through isinstance ######


# class Maths:
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

#     def circunference(self):
#         pass


# class Rectangle(Maths):
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b

#     def area(self):
#         return self.l * self.b
    
#     def perimeter(self):
#         return 2 * (self.l + self.b)
#     def volume(self):
#         return (self.l * self.b * self.h)

# class squre(Maths):
#     def __init__(self,a):
#         self.a=a

#     def area(self):
#         return self.a * self.b

#     def perimeter(self):
#         return 4 * (self.a)

# class circle(Maths):
#     def __init__(self,pie,r):
#         self.pie=pie
#         self.r=r

#     def area(self):
#         return self.pie * self.r * self.r

#     def circunference(self):
#         return 2* self.pie * self.r

# x=[Rectangle(5,6),squre(4)]
# y=[circle(3.14,4)]        
# for result in x:
#     print(result.perimeter())
# for result in y:
#     print(result.circunference())
        

        # Abstract base class in polymorphism

# from abc import ABC, abstractmethod

# class NSTI(ABC):
#     @abstractmethod
#     def xyz(self):
#         pass

# class AI(NSTI):
#     def xyz(self):
#         return " Artificial Intelligence "

# class CHNM(NSTI):
#     def xyz(self):
#         return " computer hardware , Networking and maintance "

# x=[AI(),CHNM()]

# for result in x :
#     print(result.xyz())


#  #################### 1 one #############

# from abc import ABC,abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius =radius

#     def calculate_area(self):
#         return 5.678 * self.radius**2

# class Rectangle(shape):
#     def __init__(self, width, height):
#         self.width=width
#         self.height=height

#     def calculate_area(self):
#         return self.width * self.height

# class Triangle(shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def calculate_area(self):
#         return 0.5 * self.base * self.height

# shape = [circle(5),Rectangle(6,8),Triangle(6,8)]

# for shape in shape:
#     print(f"The area of the {shape.__class__.__name__} is:{shape.calculate_area()}")




#########################################   2 #####################

# from abc import ABC, abstractmethod

# class MainItem(ABC):
#     def __init__(self, name, price, prep_time):
#         self.name =name
#         self.price =price
#         self.prep_time = prep_time
#     @abstractmethod
#     def calculate_price(self):
#         pass

# class MainCourse(MainItem):
#     def calculate_price(self):
#         return self.price * 1.15

# class Beverage(MainItem):
#     def calculate_price(self):
#         return self.price * 1.10

# class Dessert(MainItem):
#     def calculate_price(self):
#         return self.price * 1.20

# main_course =MainCourse("Spaghetti Carbonara", 360, 20)
# beverage =Beverage("Latte", 120, 5)
# dessert = Dessert("Cake", 70, 10)

# print(f"Main Course:{main_course.name}, Price: {main_course.calculate_price()}, Prep Time: {main_course.prep_time} mins")
# print(f"Beverage:{beverage.name}, price:{beverage.calculate_price()}, Prep Time{beverage.prep_time} mins")
# print(f"Dessert:{dessert.name}, price: {dessert.calculate_price()}, Prep Time:{dessert.prep_time} mins")
        





#Parents class 

# class Animal:
#         def speak(self):
#                 print("The animal make a sound")

# # Subclass 

# class Dog(Animal):
#         def speak(self):
#                 print("The dog barks")

# # create objects

# x=Animal()
# y=Dog()


# # call the speak method on boath objects

# x.speak()
# y.speak()
                











# prents class 


class Animal:
        def speak(self):
                print("The animal speak sound ")

# sub class

class Dog(Animal):
        def speck(self):
                print("The dog is barks")


# create object

x=Animal()
y=Dog()


# call the speck method object

x.speak()
y.speak()


