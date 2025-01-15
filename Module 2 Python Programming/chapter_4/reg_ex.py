# Find all occurrences of 'name':

import re
xyz = r'name'
text = "Hello What is your name? My name is Aadil Chauhan"
match = re.findall(xyz, text)
print(match)

'''____________________________________________________________'''


# Find sequences of 'q':

# xyz= r'q{3}'
# text= "q qq qqq qqqq qqqqq qqqqqq"
# match= re.findall(xyz,text)
# print(match)

'''____________________________________________________________'''

# Different patterns with 'xyz':

# xyz=r'xyz?'
# xyz=r'xyz+' 
# xyz=r'xyz*'
# xyz=r'xyz{}'

# text= "xyz xyzyxzabc xyzxyzxzyxzydef qqqq qqqqqqq qq"
# match = re.findall(xyz,text)
# print(match)

'''____________________________________________________________'''

# Search for a specific name:

# import re
# xyz= r'Aadil Chauhan'
# x= 'My name is Aadil Chauhan'
# match= re.search(xyz,x)
            # OR 
# match = re.findall(xyz, x)

# if match:
#     print("Match : ", match.group())
# else:
#     print("No match found")

'''____________________________________________________________'''


# '''Special Sequence with examples

# import re

# text = "Hello 786_ World!"

# # \d: Matches digits (0-9).
# print(re.findall(r'\d', text))  # ['7', '8', '6']

# # \D: Matches non-digits.
# print(re.findall(r'\D', text))  # ['H', 'e', 'l', 'l', 'o', ' ', '_', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# # \w: Matches word characters (letters, digits, and underscore).
# print(re.findall(r'\w', text))  # ['H', 'e', 'l', 'l', 'o', '7', '8', '6', '_', 'W', 'o', 'r', 'l', 'd']

# # \W: Matches non-word characters.
# print(re.findall(r'\W', text))  # [' ', ' ', '!']

# # \s: Matches whitespace characters.
# print(re.findall(r'\s', text))  # [' ', ' ']

# # \S: Matches non-whitespace characters.
# print(re.findall(r'\S', text))  # ['H', 'e', 'l', 'l', 'o', '7', '8', '6', '_', 'W', 'o', 'r', 'l', 'd', '!']

# # \b: Matches word boundaries.
# print(re.findall(r'\bWorld\b', text))  # ['World']

# # \B: Matches non-word boundaries.
# print(re.findall(r'\BWorld\B', text))  # []

# # \A: Matches the start of the string.
# print(re.findall(r'\AHello', text))  # ['Hello']

# # \Z: Matches the end of the string.
# print(re.findall(r'!\Z', text))  # ['!']


'''____________________________________________________________'''

# Sub patter for replacement

# import re
# xyz= "Aadil"
# replace= "Chauhan"

# x= "Aadil is the trainee in NSTI"

# z= re.sub(xyz,replace,x)
# print(z)

'''____________________________________________________________'''


# Splitting the string of the pattern

# import re

# xyz = r'\d+'
# x = 'dfhfjgsdfiyuew7866457275642'

# z = re.split(xyz, x)
# num = re.findall(xyz, x)

# print('numbers:', num)
# print(z)


'''____________________________________________________________'''


# import re

#         # Phone number validation
# mob_no = "+91-7709499655"    # valid number
# # mob_no = "+91 67g78uy923g82"    # invalid number
# pattern_phone = r'^\+?\d{1,2}[-\s]?\d{10}$'
# if re.match(pattern_phone, mob_no):
#     print("Number is valid.")
# else:
#     print("Invalid number.")


        # Email validation

# email = "aadilchauhan441@gmail.com"         # valid email
# email = "aadilchauhan441.!$%&@gmail.com"  # invalid email
# pattern_email = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
# if re.match(pattern_email, email):
#     print("Valid email.")
# else:
#     print("Invalid email.")


        # Password Validation

# password= "G3n@!r1cP@ssw0rd!2"
# xyz= r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%&])[A-Za-z\d@$!%]{10,}'

# if re.match(xyz,password):
#     print("Strong Password")
# else:
#     print("Weak Password")

'''____________________________________________________________'''
