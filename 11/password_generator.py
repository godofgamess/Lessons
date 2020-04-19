import random
import string

import school


MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 20

password_length = school.get_int('Enter password length: ', force=True)
if password_length < MIN_PASSWORD_LENGTH:
    school.error(
        'password length is too short. '
        f'Must be at least {MIN_PASSWORD_LENGTH} characters long.',
        fatal=True
    )

if password_length > MAX_PASSWORD_LENGTH:
    school.error(
        'password lenght is too long. '
        f'Must be at most {MAX_PASSWORD_LENGTH} characters long.',
        fatal=True
    )

password = []

for _ in range(password_length // 4):
    random_digit = random.choice(string.digits)
    password.append(random_digit)

for _ in range(password_length // 4):
    random_punctuation = random.choice(string.punctuation)
    password.append(random_punctuation)

for _ in range(password_length // 2):
    random_letter = random.choice(string.ascii_letters)
    password.append(random_letter)

random.shuffle(password)

print(''.join(password))
