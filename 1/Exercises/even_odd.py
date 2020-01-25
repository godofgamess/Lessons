# Эта программа определяет является ли число четным или нечетным

from sys import exit 

while True:
    # Попробовать получить ввод от пользователя
    try:
        num = input("Enter number: ")
    # Поймать сигнал конца ввода, Прекращения программы
    except (EOFError, KeyboardInterrupt):
        print()
        exit(0)

    # Попробовать выполнить опасную операцию 
    try:
        num = int(num)
    # Поймать ошибку ValueError
    except ValueError:
        print("Error:", num, "is not a number")
        print("You will not hack our program, noob!")
        exit(1)

    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
