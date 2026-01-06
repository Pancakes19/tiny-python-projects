# grade checker using if statments

total = int(input('what was the test out of: '))
score = int(input('\n And what mark did u get: '))

if total <= 0:
    print('\n the total test marks cannot be zero!')
elif score > total:
    print('\n U cannot get higher then the total test marks')
else:
    result = (score/total)*100
    print(f'\n your test percentage is {round(result, 2)}%')
    
if result >= 90:
    print('your grade for the test is A*')
elif result >= 80:
    print('your grade for the test is A')
elif result >= 70:
    print('your grade for the test is B')
elif result >= 60:
    print('your grade for the test is C')
elif result >= 50:
    print('your grade for the test is D')
else:
    print('your grade for the test is F')


