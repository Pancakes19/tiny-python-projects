# while loop = execute some code while some conditions are true

# name = input('Enter a name: ')


# as long as name is an empty string the loop will keep on prompting
# while name =='':
#     print('Please enter a name')
#     name = input('Enter a name: ')
# print(f'hello {name}!')

# another example using age

# age = int(input('Enter you age: '))
# 
# while age <= 0:
#     print('u cannot enter a negative age bruh')
#     age = int(input('Enter you age again: '))
# print('yes thats the right age!')

# if u dont give an escape route the loop will go on forever
# age = int(input('Enter you age: '))
# 
# while age <= 0:
#     print('u cannot enter a negative age bruh')
  
# the one above is an infinite loop because if we dont
# re-prompt the user, the age will always be 0 and the
# loop wont stop printing


# a while loop that keeps on asking u your fav song, till u quit
# song = input('Enter ur fave song(enter "stop" to quit): ')
# 
# while not song =='stop':
#     print(f'You like {song}!')
#     song = input('Enter ur fave song again(enter "stop" to quit): ')
# print('bye, u weirdo')
    
 
# another example using OR

# num = int(input('Enter a number (1 - 10): '))
# 
# while num < 1 or num > 10:
#     print(f'{num} is not valid')
#     num = int(input('Enter a number again (1 - 10): '))
# print(f'your number is {num}')
# 

color = input('Enter a color (w/b): ')

while not color == 'w' or not color == 'b':
    print(f'{color} is not valid')
    color = input('Enter a number again (1 - 10): ')
if color =='w':
    print(f'you are an angel')
elif color =='b':
    print('you are evil')
        
print('goodluck')


