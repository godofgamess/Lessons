from school import get_int, error

MIN_HEIGHT = 1
MAX_HEIGHT = 27

height = get_int("Enter pyramid height: ", force=True)

if height < MIN_HEIGHT or height > MAX_HEIGHT:
    error(f"height must be from {MIN_HEIGHT} to {MAX_HEIGHT}", fatal=True)

row = 1
while row <= height:
    num = 1
    while num <= row:
        print(row, ' ', end="")
        num += 1
    print()
    row += 1
