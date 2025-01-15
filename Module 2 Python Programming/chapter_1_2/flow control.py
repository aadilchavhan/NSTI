
    # check whether a person is eligible to vote

# age = 16

# if age >= 18:
#     print("you are eligible to vote")

# else:
#     print("you are not eligible to vote")



    # check whether a person is minar , adult or senior citizen

# age = int(input("enter your age : "))

# if age < 18:
#     print("you are minar")
# elif age >= 18 and age < 65:
#     print("you are adult")
# else: 
#     print("you are senior citizen")

    # Printing elements of a list

# list = ['apple','banana','orange','mango']
# for friuit in list:
#     print(friuit)


        # Multiplication table

# num = int(input("enter the multiplication table : "))
# for i in range(1,12):
#     print(num,"+",i,"=",num+i)  OR
#     print(f"{num} + {i} = {num+i}")


        # Sum of numbers    
# x = list(map(int,input("enter the numbers : ")))
# total=0
# for sum in x:
#     total +=sum
# print("Sum is:",total)


        # print even numbers
# x = int(input("enter the number : "))
# for i in range(2 , x+1, 2): #(start, stop, stop)
#     print(i)


        # print odd numbers
# x = int(input("enter the number : "))
# for i in range(1 , x+1, 2):
#     print(i)

        # print factorial
# x = int(input("enter the number : "))
# fact = 1
# for i in range(1 , x+1):
#     fact = fact * i OR
#     fact *= i
# print(fact)


                    # LAB 22

        # Task 1:  Implement if statements to check single conditions, To solve the “Checking if a temperature is below freezing point”

# temperature = int(input("enter the temperature : "))
# if temperature < 0:
#     print("The temperature is below freezing point")


        # Task 2: if-else statements to check single conditions with else, To solve the “ To checks whether a number entered by the user is even or odd”. 

# number = int(input("enter the number : "))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

        # Task 3: if-elif-else Statement using Checks multiple conditions in sequence  “ To checks the Grading system based on marks”  

 # mark = int(input("enter the mark : "))

# if mark >= 90:
#     print("A")
# elif mark >= 80 and mark < 90:
#     print("B")
# elif mark >= 70 and mark < 80:
#     print("C")
# elif mark >= 60 and mark < 70:
#     print("D")
# else:
#     print("F")


        # Task 4: Nested if Statement for more complex conditions, To solve the “Checking if a number is positive, zero, or negative using nested if”  

# number = int(input("enter the number : "))
# if number >= 0:
#     if number == 0:
#         print("The number is zero")
#     else:
#         print("The number is positive")
# else:
#     print("The number is negative")


                    # LAB 23

        # Task 1:  Prompt the user to input two integers. 

# num1 = int(input("enter the first number : "))
# num2 = int(input("enter the second number : ")) 


        # Task 2:  Calculate the sum of the two integers.

# sum = num1 + num2


        # Task 3: Check if the computed sum lies between 10 and 20 (inclusive).
    
# if 10 <= sum <= 20:
#     print("The sum is within the range")
# else:
#     print("The sum is outside the range") 

                    
                    # LAB 24

        # Task 1:  To created two Boolean objects, bool1 and bool2, and used the and operator within an if statement to evaluate them

# bool1 = True
# bool2 = False

# if bool1 and bool2:
#     print("Both conditions are true")
# else:
#     print("At least one condition is false")


                # LAB 25
    
        # Task 1:  Implement the python code for Convert temperatures to and from fahrenheit  

# # temperature = int(input("Input the temperature you want to convert ? "))
# unit = input("Input 'C' for celsius or 'F' for fahrenheit ? ")

# if unit.upper() == "C":
#     fahrenheit = (temperature * 9/5) + 32
#     print("The temperature in fahrenheit is " + str(fahrenheit))
# elif unit.upper() == "F":
#     celsius = (temperature - 32) * 5/9
#     print("The temperature in celsius is " + str(celsius)) 
# else:
#     print("Invalid input")


            # Task 1:  Implement the Python program to convert a month name to a number of days 

# month = input("Input the name of month: ")
# year = int(input("Input the year: "))

# if month in ("January", "March", "May", "July", "August", "October", "December"):
#     print("31 days")
# elif month in ("April", "June", "September", "November"):
#     print("30 days")
# elif month == "February": 
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print("29 days")
#     else:
#         print("28 days")
# else:
#     print("Invalid input")




            # Task 1:  Implement the Python program to print "Assalamu alaikum"

# def aadil():
#     print("Assalamu alaikum")

# aadil()

            # Task 2:  Implement the Python program to calculate the sum of two numbers

# def xyz(num1,num2):
#     print(num1+num2)

# xyz(2,3)


        # Task 3:  Implement the Python program to calculate the product of two numbers
        
# def abc(num1,num2):
#     print(num1*num2)

# abc(5,4)


            # Task 4:  Implement the Python program to find the square of a number
# def xyz(num):
#     return num*num

# square = (xyz(5))
# print("Square of 5 is",square)


            # Task 5:  Implement the Python program to find the cube of a number

# def cube(num):
#     return num*num*num

# cube = (cube(8))
# print("Cube of 8 is",cube)

        # Task 6:  Implement the Python program to calculate substraction of two numbers

def mno(num1,num2):
    return num1/num2

mno = (mno(5,4))
print("Substraction of 5 and 4 is",mno)





