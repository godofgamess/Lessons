from school import get_string

MIN_LENGTH = 10

password = get_string("Enter your password: ")

# Flags
found_upper = False
found_lower = False
found_digit = False

# Check password length >= MIN_LENGTH
if len(password) < MIN_LENGTH:
    return False
if not password.isalnum():
    return False

for letter in password:
    if letter.islower():
        found_lower = True
    elif letter.isupper():
        found_upper = True
    elif letter.isdigit():
        found_digit = True

if found_lower and found_upper and found_digit:

# Check password is only alphanumeric

# check all flags

