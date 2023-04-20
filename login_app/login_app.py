print('CREATE YOUR ACCOUNT HERE!')

username = input('Enter the username: ')
password = input('Enter the password: ')
dob = input('Select the dob: ')

print('your account has been created successfully!!')
print('login now!')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('you are logged in successfully!!')
else:
    print('Invalid credentials')
