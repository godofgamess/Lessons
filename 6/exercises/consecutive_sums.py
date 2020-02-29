from school import get_int
from sys import exit

num = get_int("Enter a number: ", force=True)

total = 0
sums = 0
begin_num = 1
next_num = 1

while next_num != num:
    total += next_num

    # Если сумма стала больше введенного числа
    if total > num:
        begin_num += 1
        next_num = begin_num
        total = 0
        continue

    if total == num:
        begin_num += 1
        next_num = begin_num
        total = 0
        sums += 1
        continue

    next_num += 1

sums += 1  # num itself
print(f'sums: {sums}')
