# simple login with python if statements
import time
print('~~~~~~ Welcome to Dreamland ~~~~~~')
username = input('\n Please enter your dreamer name: ')
password = input('\n Now enter your dreamer passcode: ')

# little loading animation

spinner = ["|", "/", "-", "\\"]
print("\nLoading ", end="", flush=True)

for i in range(12):
    print(spinner[i % 4], end="\r", flush=True)
    time.sleep(0.2)

print("Loading complete!")

# -------------------------------

if username == 'hex' and password == '1234':
    
    print(f'\n hello {username}! \n have a wonderful time in your dreams✨')
else:
    print('Access Denied. We dont allow witches!!!')
    


# other loading animations
# import time
# 
# print("\nLogging in", end="", flush=True)
# for _ in range(3):
#     time.sleep(0.5)
#     print(".", end="", flush=True)
# 
# print("\n")

 