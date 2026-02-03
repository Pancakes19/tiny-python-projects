# compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('enter the principle amount: '))
    if principle <= 0:
        print('principle can\'t be less than or equal to zero')


# interest can be either more than zero or less than 100
while rate <= 0 or rate >= 100:
    rate = float(input('enter the interest rate: '))
    if rate <= 0 or rate >= 100:
        print('rate can\'t be less than or equal to zero or be greater than 100')


while time  <= 0:
    time = int(input('enter the time in years: '))
    if time <= 0:
        print('time can\'t be less than or equal to zero')
        
        
total = principle * pow((1 + rate /100), time)
print(f'balance after {time} years: ${total:.2f}')



