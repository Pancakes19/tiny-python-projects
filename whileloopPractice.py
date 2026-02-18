# while loop practice
# a program that counts even and odd numbers
even = 0
odd = 0

num = int(input('enter a number and enter 0 to stop\n'))

while num:
    if num % 2 == 0:
        even += 1
        num = int(input('enter a number and enter 0 to stop'))
    else:
        odd += 1
        num = int(input('enter a number and enter 0 to stop'))
print('odd: ',odd,'\neven: ',even)