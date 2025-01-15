            # write a program to calculate the add,sub,mul,div,mod,power

#  def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# def mod(a,b):
#     return a%b

# def power(a,b):
#     return a**b
    
# a=int(input("enter the first number : "))
# b=int(input("enter the second number : "))

# print("addition of",a,"and",b,"is",add(a,b))
# print("substraction of",a,"and",b,"is",sub(a,b))
# print("multiplication of",a,"and",b,"is",mul(a,b))
# print("division of",a,"and",b,"is",div(a,b))
# print("modulus of",a,"and",b,"is",mod(a,b))
# print("power of",a,"and",b,"is",power(a,b))     



# def keyWord(myname,myage,myclass):
#     print("My name is",myname)
#     print("My age is",myage)
#     print("My class is",myclass)

# keyWord(myname="Aadil",myage=22,myclass="AIPA")


# def sum(*args):
#     return sum(args)

# print(sum(1,2,3,4,5))
# print(sum(1,2,3,4,5,6,7,8,9,10))


                # Positional Arguments

# def mul(a, b):
#     """
#     Multiply two numbers.

#     Parameters:
#     a (int, float): The first number.
#     b (int, float): The second number.

#     Returns:
#     int, float: The product of the two numbers.
#     """
#     # Return the product of a and b
#     return a * b

# print(mul(2,3))

                # Keyword Arguments

# def keyword(name,age,place):
#     print("My name is",name)
#     print("My age is",age)
#     print("My place is",place)

# keyword(name="Aadil",age=22,place="Hyderabad")     


                # Default Arguments

# def default(name="Aadil",age=22,place="Hyderabad"):
#     print("My name is",name)
#     print("My age is",age)
#     print("My place is",place)

# default()


                # Variable-Length Arguments

# def variable_length(*args):
#     for arg in args:
#         print(arg)

# variable_length(1,2,3,4,5,6,7,8,9,10)


                # LOCAL VARIABLES

# def xyz():
#     a = 10
#     print(a)

# xyz()

        #  global variables

# a = 10
# def xyz():
#     global a
#     a = 20
#     print(a)

# xyz()
# print(a)


# x=10
# global func():
#     x=20
#     print(x)


#             KEYWORD ARGUMENTS
def xyz(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

xyz(name="Aadil", age=22, place="Hyderabad")









