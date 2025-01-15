# try:
#     result=10/8
# except ZeroDivisionError:
#     print("Number can not be division by zero ")

#     result=10/0
#     print(result)


    # try:
    #     res=10/8
    # except ZeroDivisionError:
    #     print("You can divide a number by zero")
    # else:
    #     print("the result is :",res)

    # finally:
    #     print("It will print regardless of whether the issue is raised or not")


# if age < 18:
#     print("you are minar")
# elif age >= 18 and age < 65:
#     print("you are adult")
# else: 
#     print("you are senior citizen")

# def check_(age):
#     if age<18 
#     raise ValueError("Age must be 18")
#  return "you are allowed to vote "
# try:
#     result=check _age(18)
#     print(result)
# except ValueError as ve:
#     print(ve)


# try:
#     num=int(input("enter a number:"))
#     result=10/num

# except ValueError:
#     print("inavlid input")
# except ZeroDivisionError:
    # print("you can't divide by zero")
# else:
#     print(result)
# finally:
#     print("you are donr.")


                        # Exceptional handling


# 1-Write a Python program that defines a custom exception NegativeNumberError. Raise this exception if the user inputs a negative number and handle it gracefull


# class NegativeNumberError(Exception):
#     pass

# def get_user_input():
#     try:
#         num = float(input("Enter a number: "))
#         if num < 0:
#             raise NegativeNumberError("Negative numbers are not allowed")
#         print("You entered a positive number:", num)
#     except NegativeNumberError as e:
#         print("Error:", e)
#     except ValueError:
#         print("Error: Invalid input. Please enter a number.")

# get_user_input()


# 2-Write a Python program that takes two numbers as input and performs division. Handle the case where the divisor is zero using exception handling.

def divide_numbers():
    try:
        num1 = float(input("Enter the dividend: "))
        num2 = float(input("Enter the divisor: "))
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except ValueError:
        print("Error: Invalid input. Please enter a number")

divide_numbers()

