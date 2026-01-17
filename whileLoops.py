# format specifiers = {value:flags} format a value based on what
#                            flags are inserted

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 300000000.14159
price2 = -987.65
price3 = 12.34

print(f'price 1 is: ${price1:03}')
print(f'price 2 is: ${price2:09}')
print(f'price 3 is: ${price3:+}')

# we can also mix and match the specifiers
print(f'price 1 is: ${price1:+,.2f}')

