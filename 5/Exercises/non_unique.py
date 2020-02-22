

numbers = [1, 2, 3, 1, 3]
duplicate_numbers = []

for number in numbers:
    if numbers.count(number) != 1:
        duplicate_numbers.append(number)

print(duplicate_numbers)
