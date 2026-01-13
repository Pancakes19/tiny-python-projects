# string methods and functions

# name = input('Enter your full name: ')
# 
# result = len(name)
# result = name.count('n')
# result = name.rfind('r')
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = name.replace('_', '')

# print(help(str)) 

# Exercise for string validation
# rules: no more than 12 characters
#        no spaces
#        no , or @ or # or $ or % ...

name = input('Enter a username: ')

special_chars = ",@#!$%^&*()"

if len(name) >= 12:
    print('Name cannot be more than 12 characters')
elif ' ' in name:
    print('Name cant contain spaces')
elif any(char in special_chars for char in name):
    print('Name cant contain special characters')
else:
    print('username created')


