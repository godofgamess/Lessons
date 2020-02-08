from random import randint

numbers = []

i = 0
while i < 20:
    numbers.append(randint(1, 20))
    i += 1

print(f"Before: {numbers}")

new_numbers = []

i = 0
while i < len(numbers):
    if numbers[i] not in new_numbers:
        new_numbers.append(numbers[i])
    i += 1

print(f"After: {new_numbers}")
