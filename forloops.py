# for loops in python
# u can iterate over a range, string, sequence etc.

# counter = 10
# for i in range(counter):
#     print('*')

# or print without a counter using range
# we can use range with a step to count in steps e.g range(1, 11, 2)
# for x in reversed(range(1,11)):
#     print(x)
# print("Happy New year!")    
    
# we can also iterate thru a string
# myNumber = '0815649939'
# 
# for x in myNumber:
#     print(x,end='')
    


# continue and break key words
# we can use continue to skip over stuff

creditCard = '5746-4682-4721-5647'
# for x in creditCard:
#     if x == '-':
#         continue
#     else:
#         print(x,end='')

# break can break the loop after a certain contion is met
for x in creditCard:
    if x == '-':
        break
    else:
        print(x,end='')







    