import re

# Email and password authenticator

user_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password = re.compile(r"^[a-zA-Z0-9$%#@]{7,}\d")

# Email Authenticator
while 1:
    try:
        email_input = str(input('Email address: '))
        test1 = user_email.fullmatch(email_input)
        1/int(test1 is not None)
        break
    except ZeroDivisionError:
        print('Please enter a valid email address!')

# Password Authenticator
print('Enter a password of at least 8 char, containing any Alphabet, number, or these characters $%#@')
while 1:
    try:
        password_input = str(input('Password: '))
        1/int(password.fullmatch(password_input) is not None)
        break
    except ZeroDivisionError:
        print('Please enter a valid email address!')

print('You\'re in')


