         #  python keywords and identifiers
         
    # identify the invalid identifier from the following:
#  my_var= "Aadil_Chauhan"
#  print(my_var)

# _myVar= "Aadil_Chauhan"
# print(_myVar)

    # invalid  
# 2var="Aadil_Chauhan"
# print(2var)

# my-var="Aadil_Chauhan"
# print(my-var)

    # list 5 python keywords that cannot be used as a identifiers.
# and
# or
# not
# True
# False


         # Python Print Functions
         
    # Write a program to print "Welcome to Python Programming
# x= "Welcome to Python programming"
# print(x)

    # Use the print() function to display:
# Your name.
# Your favorite number

# y="Aadil Chauhan"
# z="0"
# print(y)
# print(z)


        # Python Variablesis
        
    # Assign the value 25 to a variable and print it.
# x=25
# print(x)

    # Swap two variables without using a temporary variable.
# a=10
# b=20
# a, b = b, a

# print("after swapping")
# print("a =", a )
# print("b =" , b)

    # Assign three values to three variables in a single line.
# x,y,z=10,20,30
# print(x,y,z)

    # Create a global variable and access it inside a function.
    
    
        # Python Data Types
        
    # Determine the data type of the following values:
# a=10
# b=10.5
# c="Hello"
# d=True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

    # Check whether the variable x is of type str.
# x="AI"
# print(isinstance(x, str))
    
    
        # Python Numbers
        
    # Write a program to add two integers.
# x=12
# y=59
# sum=12+59
# print(sum)

	# Find the remainder when 25 is divided by 4.
# a=25 
# b=4
# print(a%b)

	# Calculate the square of a number using an operator
# number=12
# square=number**2
# print(square)


        # Python Strings
        
    # Create a string and print its length.
# string= "Welcome to Python programming"
# print(len(string))

    # Write a program to slice a string: Extract "World" from "Hello World".
# string= "Hello World"
# print(string[6:])

    # Convert the string "python programming" to uppercase.
# string="python programming"
# print(string.upper())

    # Concatenate two strings: "Hello" and "Python".
# str1="Hello"
# str2="Python"
# print(str1+ " " +str2)

	# Use an escape character to print He said, "Python is fun!".
# print('He said, "Python is fun"'


                # Python Lists

    # Create a list with 5 elements and print the third element.
    # Replace the second element in the list with 10.

# list=[1,2,3,4,5]
# print (list[2])
 
# list [1] = 10
# print(list)

    # Add a new items to the end of the list
    # Remove the element 20 from the list

# list=[10, 20, 30]
# # list.append(40)
# # print(list)

# list.remove(20)
# print(list)

    # Sort the list [5,1,8,3] in ascending order
# list=[5,1,8,3]
# list.sort()
# print(list)

        # Python Operators

    # Demonstrate the use of arthimatic operators in Python
# a=10
# b=3
# print("addition", a+b)
# print("substraction", a-b)
# print("multiplication", a*b)
# print("modulus", a%b)

    # Write a program to compare two numbers and print the larger one
# num1=20
# num2=50
# if num1 > num2:
#     print(num1,"is larger")
# else:
#     print(num2, "is larger")

    # Combine logical operators to check if a number is greater than 10 and less then than 20.
# num=15
# if num>10 and num<20:
#     print(num,"is greater than 10 and less than 20")
# else:
#     print(num,"is not in the range")

        # Python Booleans

    # Write a program that returns true if a number is even and false otherwise.
    
# def is_even(num):
#     return num % 2 == 0

# num=10
# print(is_even(num))

# num=11
# print(is_even(num))

    # Use the bool function to check the truth value of an empty list

# list=[]
# print(bool(list))

# list=[1,2,3]
# print(bool(list))


        # Input and Output
        
    # Write a programm that asks for the user's name and prints a greeting.

# name = input("What is your name? ")
# print("Hello, " + name + "!")


    # Take two numbers as input from the user and display their sum.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# sum = num1 + num2
# print("The sum is:", sum)


        # Python Veriables
    
    
    # Assign a float value to a variable and print it.
# float=2.5
# print( float)

	# Assign the result of 10 + 20 to a variable and display it.
# result=10+20
# print(result)

    #  Create a program to demonstrate the use of both local and global variables.
# global_variable = 100
# local_variable = 50
# print( local_variable)
# print( global_variable)


    	# Python Type Conversion
     
	# Convert an integer to a float and print it.
# integar=10
# float=float(integar)
# print(float)
 
	# Convert a string "123" to an integer and add 10 to it.
# string="123"
# integar=int(string)
# result=integar+10
# print(result)

	# Write a program to check the type of input given by the user.
# user_input=input("enter a value")

# if user_input.isdigit():
#     print("You entered an integer.")
# elif user_input.replace('.', '', 1).isdigit():
#     print("You entered a float.")
# else:
#     print("You entered a string.")


        # Python Strings
        
	# Find the index of the first occurrence of the character "o" in "Hello World".
# string = "Hello World"
# index = string.find("o")
# print("Index of 'o':", index)

	# Replace "World" with "Python" in "Hello World".
# x= "Hello World"
# y= x.replace("World", "Python")
# print(y)

	# Reverse the string "Python".
# string = "Python"
# reversed = string[::-1]
# print(reversed)

	# Count the number of vowels in a string.
# string = "Hello World"
# vowels = "aeiou"
# count = 0
# for char in string:
#   if char.lower() in vowels:
#     count += 1
# print(count)

	# Check whether the string "madam" is a palindrome
# string = "madam"
# if string == string[::-1]:
#   print("Yes, it's a palindrome.")
# else:
#   print("No, it's not a palindrome.")
  
  
        # Python Lists
        
	# Create a list with elements of different data types.
 
# my_list = [1, "hello", 3.12, True, [1, 2, 3]]
# print(my_list)

    # Write a program to find the sum of all numeric elements in a list.

# list=[1,34,56,78,90]
# print(sum(list))

	# Remove all occurrences of the number 5 from the list [5, 10, 15, 5, 20].
 
# list = [5, 10, 15, 5, 20]
# list = [i for i in list if i != 5]
# print(list)

	# Create a nested list and access the innermost element.
 
	# Write a program to merge two lists.
 
# x=["aadil", "arbaz","faiz","sadique"]
# y=["saad","samir","karim"]
# x.extend(y)
# print(x)


        # Python Tuples
        
    
	# Create a tuple with 4 elements and print the second element.
 
# element=(22,33,44,55)
# print(element[1])

	# Convert the tuple (1, 2, 3, 4) into a list.
 
# tuple=(1,2,3,4)
# x=list[tuple]
# print(x)

	# Write a program to unpack a tuple into individual variables.
 
# tuple=(1,2,3,4)
# a, b, c, d = tuple
# print(a)
# print(b)
# print(c)
# print(d)
 
	# Check if the element 10 is present in the tuple (5, 10, 15).
 
# tuple = (5, 10, 15)

# if 10 in tuple:
#     print("10 is present in the tuple.")
# else:
#     print("10 is not present in the tuple.")


        # Python Dictionaries

    # Create a dictionary with three key-value pairs and print it.

# x= {"name": "Aadil_Chauhan", "age": 22"}
# print(x)


	# Access the value associated with the key "name" in the dictionary  = {"name": "John", "age": 25, "city": "New York"}

# x= {"name": "John", "age": 25,}
# print(x["name"])


 # Add a new key-value pair to the dictionary.
 
# x = {"Name": "Aadil_Chauhan", "Age": "22"}
# x["city"] = "Hyderabad"
# print(x)

	# Remove a key-value pair from a dictionary.
 
# x = {"Name": "Aadil_Chauhan", "Age": "22", "City": "Hyderabad"}
# del x["Age"]
# print(x)


	# Check whether the key "age" exists in the dictionary.


dict = {"name": "John", "age": 25, "city": "New York"}

if "age" in dict:
    print("The key 'age' exists in the dictionary.")
else:
    print("The key 'age' does not exist in the dictionary.")


    
    
    