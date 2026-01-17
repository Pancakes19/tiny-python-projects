# indexing = accessing elements of a sequence using [] which
# is the indexing operator
# in strings only

phone_num = '+2648-1564-9939'

# just one index means its just the starting position
# print(phone_num[2])

# printing the first 4 numbers, the end index is exclusive
# this prints 0815 cause its the first 4 numbers, u can start from any index
# u can even remove the 0 and python assumes the starting index is 0
# print(phone_num[:4])
# print(phone_num[2:7])


# if u need to start from a random index until the end
# print(phone_num[3:])

# if u need the last index in a number||string
# -1 is the last, -2 is the second last and so on
# print(phone_num[-1])

# using step only gives the number ad a certain place(step) in the seqeunce
# basically skipping indexes
# it starts with the first index then counts
# print(phone_num[::2])

# getting the last 4 digits from a
# number without revealing the other numbers(exercise)
# last4digits = phone_num[-4:]
# print(f'XXXX-XXXX-{last4digits}')

# if we need to reverse the string we use a step of -1 index
reversed_phone_num = phone_num[::-1]
print(reversed_phone_num)








