# time calculator

first_time = input('enter time: ')
Second_time = input('enter time: ')
operator = input('enter operator(+,-): ')
# when we split a string, it becomes a
# list so we access the list items with indexing
# and turn them from string to int for operations

fhours, fminutes = first_time.split(':')
Shours, Sminutes = Second_time.split(':')


fhours = int(fhours)
fminutes = int(fminutes)
Shours = int(Shours)
Sminutes = int(Sminutes)

total_fminutes = fhours * 60 + fminutes
total_Sminutes = Shours * 60 + Sminutes

if operator =='+':
    result = total_fminutes + total_Sminutes
else:
    result = total_fminutes - total_Sminutes

# for 24 hour wrapping
result = result % (24 * 60)
    
# // is an integer divisin that discards the remainder
# and mod only gives the remainder which are the minutes
Nhours = result // 60
Nminutes = result % 60

print(f"New time: {Nhours}:{Nminutes:02d}")




