from school import get_int, error

num = get_int("Enter number from 1 to 9: ", force=True)

if num < 1 or num > 9:
    error("number must be from 1 to 9", fatal=True)

i = 1
while i < 10:
    print(f"{num} * {i} = {i * num}")
    i += 1

#i = 1
#while i < 10:
#    j = 1
#    while j < 10:
#        print(f"{i} * {j} = {i * j}")
#        j += 1
#    i += 1
#    print()
