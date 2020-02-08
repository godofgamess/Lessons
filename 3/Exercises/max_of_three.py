from school import get_int

from sys import exit

numbers = []

i = 0
while i < 3:
    num = get_int("Enter a number: ")

    if num is None:
        print("Error: not a number!")
        exit(1)

    numbers.append(num)
    i += 1

maximum = numbers[0]

if numbers[1] > maximum:
    maximum = numbers[1]

if numbers[2] > maximum:
    maximum = numbers[2]

print(f"maximum is {maximum}")

