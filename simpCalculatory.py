# python calculator to practice if statements
print('------------------------------------------------')
print('------  Welcome to the CLI calculator  ---------')
print('------------------------------------------------')

firstnum = float(input('enter the first number: '))
secondnum = float(input('enter the second number: '))
operator = input('enter the operator: ')
result = 0

if operator == '*':
    result = firstnum * secondnum
    print(f'\n the result is {result}')
elif operator == '+':
    result = firstnum + secondnum
    print(f'\n the result is {result}')
elif operator == '-':
    result = firstnum - secondnum
    print(f'\n the result is {result}')
elif operator == '/':
    result = firstnum / secondnum
    print(f'\n the result is {round(result, 2)}')
else:
    print('Invalid operation')