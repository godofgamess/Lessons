from school import get_int

from sys import exit
from random import randint

max_number = 1

numbers = []

i = 0
while i < 100:
    numbers.append(randint(1, max_number))
    i += 1

num = get_int(f"Give me a number (from 1 to {max_number}): ")

if num is None:
    print("Error: not an integer!")
    exit(1)

found = False

i = 0
while i < len(numbers):
    if numbers[i] == num:
        found = True
        break
    i += 1

if found:
    print(f"I have found {num}!")
else:
    print(f"I have not found {num}")
