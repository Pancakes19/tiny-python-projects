# madlipz game
# place = input('enter a place ')
# name = input('enter a name ')
# age = input('enter an age ')
# age = int(age)
# nationality = input('enter a nationality ')
# reason = input('enter a reason')
# print()
# 
# print(f"Hello, I'm from {place}, and i'm {age} years old ")
# print(f"My name is {name} and i am an {nationality}. ")
# print(f"I came here to {reason}. ")

#shopping
item = input('enter an item u want to buy ')
price = float(input('enter the price of that item '))
quantity = int(input('how many of these items do u want to buy '))
cost = price * quantity

choice = input(f'the amount is {cost}, Do u still want to purchase these items ? ')
if choice =='yes':
    print(f'You have bought {quantity} {item} for {cost}!!')
else :
    print('you are a cheap bastard!!')




